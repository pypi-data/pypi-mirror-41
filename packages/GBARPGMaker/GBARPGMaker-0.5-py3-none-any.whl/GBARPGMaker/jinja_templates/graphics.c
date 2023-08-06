#include <gba.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "imageData.h"
#include "graphics.h"

static int lastscreentx;
static int lastscreenty;
static bool forceMapVRAMUpdate;

static const int* currentMapSize;
static const int* currentSpecials;
static const unsigned short* currentBottomMap;
static const int* currentBottomMapSize;
static const unsigned short* currentMiddleMap;
static const int* currentMiddleMapSize;
static const unsigned short* currentTopMap;
static const int* currentTopMapSize;

void moveScreen(int screenx, int screeny) {
    int screentx = (screenx) / 8;
    int screenty = (screeny) / 8;

    if (screentx != lastscreentx || screenty != lastscreenty || forceMapVRAMUpdate) {
        for (int i = 0; i < 22; ++i) {
            dmaCopy(currentBottomMap + (i + screenty - 1) * currentBottomMapSize[0] + screentx - 1, MAP_BASE_ADR(28) + 32 * 2 * i, 32 * 2);
        }
        for (int i = 0; i < 22; ++i) {
            dmaCopy(currentMiddleMap + (i + screenty - 1) * currentTopMapSize[0] + screentx - 1, MAP_BASE_ADR(29) + 32 * 2 * i, 32 * 2);
        }
        for (int i = 0; i < 22; ++i) {
            dmaCopy(currentTopMap + (i + screenty - 1) * currentTopMapSize[0] + screentx - 1, MAP_BASE_ADR(30) + 32 * 2 * i, 32 * 2);
        }
    }

    REG_BG0HOFS = screenx % 8 + 8;
    REG_BG0VOFS = screeny % 8 + 8;
    REG_BG1HOFS = screenx % 8 + 8;
    REG_BG1VOFS = screeny % 8 + 8;
    REG_BG2HOFS = screenx % 8 + 8;
    REG_BG2VOFS = screeny % 8 + 8;

    lastscreentx = screentx;
    lastscreenty = screenty;
}

void forceMoveScreen(int screenx, int screeny) {
    forceMapVRAMUpdate = true;
    moveScreen(screenx, screeny);
}

{% for map_name, map in maps.items() %}
void loadMap{{ map_name }}() {
    currentMapSize = {{ map_name }}Size;
    currentSpecials = {{ map_name }}Specials;
    dmaCopy({{ map_name }}Palette, BG_PALETTE, {{ map_name }}PaletteLen);
    dmaCopy({{ map_name }}Tileset, TILE_BASE_ADR(0), {{ map_name }}TilesetLen);
    currentBottomMap = {{ map.bottom_layer_name }};
    currentBottomMapSize = {{ map.bottom_layer_name }}Size;
    currentMiddleMap = {{ map.middle_layer_name }};
    currentMiddleMapSize = {{ map.middle_layer_name }}Size;
    currentTopMap = {{ map.top_layer_name }};
    currentTopMapSize = {{ map.top_layer_name }}Size;

    forceMoveScreen(0, 0);
}
{%- endfor %}

// each sprite has its 3 attrs, a size and a position
static u16 spriteAttrs[128][3];
static int spriteRealSizes[128][2];
static int spritePositions[128][2];

static u16* spritePaletteIndex = (u16*)SPRITE_PALETTE;
static u32* spriteTilesetIndex = (u32*)OBJ_BASE_ADR;

static int currentLastSpriteImageIndex;
{% for sprite_image_name in sprite_images.keys() %}
static bool {{ sprite_image_name }}loaded = false;
static int {{ sprite_image_name }}Location;

void loadSpriteImage{{ sprite_image_name }}() {
    if ({{ sprite_image_name }}loaded == true) {
        return;
    }
    {{ sprite_image_name }}Location = (spriteTilesetIndex - (u32*)OBJ_BASE_ADR) / 8;

    dmaCopy({{ sprite_image_name }}Palette, spritePaletteIndex, {{ sprite_image_name }}PaletteLen * 2);
    long colorOffset = spritePaletteIndex - (u16*)SPRITE_PALETTE;
    long val = colorOffset + (colorOffset << 8) + (colorOffset << 16) + (colorOffset << 24);
    for (int i = 0; i < {{ sprite_image_name }}TilesetLen; ++i) {
        spriteTilesetIndex[i] = {{ sprite_image_name }}Tileset[i] + val;
    }

    spritePaletteIndex += {{ sprite_image_name }}PaletteLen;
    spriteTilesetIndex += {{ sprite_image_name }}TilesetLen;
    {{ sprite_image_name }}loaded = true;
    currentLastSpriteImageIndex = {{ loop.index }};
}

void unloadSpriteImage{{ sprite_image_name }}() {
    if (({{ sprite_image_name }}loaded == false) || (currentLastSpriteImageIndex != {{ loop.index }})) {
        return;
    }
    spritePaletteIndex -= {{ sprite_image_name }}PaletteLen;
    spriteTilesetIndex -= {{ sprite_image_name }}TilesetLen;
    {{ sprite_image_name }}loaded = false;
}
{%- endfor %}

void clearSpriteGraphics() {
    spritePaletteIndex = (void*)SPRITE_PALETTE;
    spriteTilesetIndex = (void*)OBJ_BASE_ADR;
    memset(spritePaletteIndex, 0, 512);
    // TODO: zjistit jestli odpovida cislo 512 - jestli ne tak to budou hoooodne random bugy :D
    memset(spriteTilesetIndex, 0, 512);
    {% for sprite_image_name in sprite_images.keys() %}
    {{ sprite_image_name }}loaded = false;
    {{ sprite_image_name }}loaded = false;
    {{ sprite_image_name }}loaded = false;
    {% endfor %}
}

static void setSpriteAttr0(int spriteIndex) {
    OAM[spriteIndex].attr0 = spriteAttrs[spriteIndex][0] + spritePositions[spriteIndex][1];
}

static void setSpriteAttr1(int spriteIndex) {
    OAM[spriteIndex].attr1 = spriteAttrs[spriteIndex][1] + spritePositions[spriteIndex][0];
}

static void setSpriteAttr2(int spriteIndex) {
    OAM[spriteIndex].attr2 = spriteAttrs[spriteIndex][2];
}

void setSpriteX(int spriteIndex, int x) {
    spritePositions[spriteIndex][0] = x;
    setSpriteAttr1(spriteIndex);
}

void setSpriteY(int spriteIndex, int y) {
    spritePositions[spriteIndex][1] = y;
    setSpriteAttr0(spriteIndex);
}

void setSpriteDisable(int spriteIndex) {
    spriteAttrs[spriteIndex][0] = OBJ_DISABLE | spriteAttrs[spriteIndex][0];
    setSpriteAttr0(spriteIndex);
}

void setSpriteEnable(int spriteIndex) {
    spriteAttrs[spriteIndex][0] = ~OBJ_DISABLE & spriteAttrs[spriteIndex][0];
    setSpriteAttr0(spriteIndex);
}

void setSpritePriority(int spriteIndex, int p) {
    spriteAttrs[spriteIndex][2] = (spriteAttrs[spriteIndex][2] & ~OBJ_PRIORITY(3)) | OBJ_PRIORITY(p);
    setSpriteAttr2(spriteIndex);
}

{% for sprite_image_name in sprite_images.keys() %}
void setSpriteGraphics{{ sprite_image_name }}(int spriteIndex) {
    spriteAttrs[spriteIndex][0] = (spriteAttrs[spriteIndex][0] & ~OBJ_SHAPE(3)) | ({{ sprite_image_name }}Shape << 14);
    spriteAttrs[spriteIndex][1] = (spriteAttrs[spriteIndex][1] & ~ATTR1_SIZE_64) | ({{ sprite_image_name }}Size << 14);
    spriteAttrs[spriteIndex][2] = (spriteAttrs[spriteIndex][2] & ~OBJ_CHAR(1023)) | OBJ_CHAR({{ sprite_image_name }}Location);
    setSpriteAttr0(spriteIndex);
    setSpriteAttr1(spriteIndex);
    setSpriteAttr2(spriteIndex);
    spriteRealSizes[spriteIndex][0] = {{ sprite_image_name }}RealSize[0];
    spriteRealSizes[spriteIndex][1] = {{ sprite_image_name }}RealSize[1];
}
{% endfor %}

int spriteCheckForSpecials(int spriteIndex, int spritex, int spritey, bool justOne) {
    int spritetx = (spritex) / 8;
    int spritety = (spritey) / 8;
    int spritetex = (spritex - 1) / 8;
    int spritetey = (spritey - 1) / 8;

    int result = 0;

    for (int i = spritetx; i <= spritetex + spriteRealSizes[spriteIndex][0]; ++i) {
        for (int o = spritety; o <= spritetey + spriteRealSizes[spriteIndex][1]; ++o) {
            result = result | currentSpecials[i + o * currentMapSize[0]];
            if (justOne & (result != 0)) {
                return result;
            }
        }
    }
    return result;
}

bool checkSpriteCollision(int spriteIndex1, int sprite1x, int sprite1y, int spriteIndex2, int sprite2x, int sprite2y) {
    return (sprite1x <= sprite2x + spriteRealSizes[spriteIndex2][0] * 8) &&
           (sprite2x <= sprite1x + spriteRealSizes[spriteIndex1][0] * 8) &&
           (sprite1y <= sprite2y + spriteRealSizes[spriteIndex2][1] * 8) &&
           (sprite2y <= sprite1y + spriteRealSizes[spriteIndex1][1] * 8);
}

void moveHero(int* herox, int* heroy) {
    int screenx = 0;
    int screeny = 0;
    static int lastherox;
    static int lastheroy;

    // mapm boundry check
    if (*herox < 0) {
        *herox = 0;
    } else if (*herox > currentMapSize[0] * 8 - spriteRealSizes[0][0] * 8) {
        *herox = currentMapSize[0] * 8 - spriteRealSizes[0][0] * 8;
    }
    if (*heroy < 0) {
        *heroy = 0;
    } else if (*heroy > currentMapSize[1] * 8 - spriteRealSizes[0][1] * 8) {
        *heroy = currentMapSize[1] * 8 - spriteRealSizes[0][1] * 8;
    }

    // collision check
    int specials = spriteCheckForSpecials(0, *herox, *heroy, false);
    if (specials & 1) {
        *herox = lastherox;
        *heroy = lastheroy;
    }
    if (specials & 2) {
        *herox = 0;
        *heroy = 0;
    }

    // move the sreen and the sprite
    if (*herox <= 120 - spriteRealSizes[0][0] * 4) {
        setSpriteX(0, *herox);
    } else if (*herox >= currentMapSize[0] * 8 - 120 - spriteRealSizes[0][0] * 4) {
        screenx = currentMapSize[0] * 8 - 240;
        setSpriteX(0, OBJ_X(*herox - (currentMapSize[0] * 8 - 120 - spriteRealSizes[0][0] * 4) + 120 - spriteRealSizes[0][0] * 4));
    } else {
        screenx = *herox - (120 - spriteRealSizes[0][0] * 4);
        setSpriteX(0, 120 - spriteRealSizes[0][0] * 4);
    }
    if (*heroy <= 80 - spriteRealSizes[0][1] * 4) {
        setSpriteY(0, *heroy);
    } else if (*heroy >= currentMapSize[1] * 8 - 80 - spriteRealSizes[0][1] * 4) {
        screeny = currentMapSize[1] * 8 - 160;
        setSpriteY(0, *heroy - (currentMapSize[1] * 8 - 80 - spriteRealSizes[0][1] * 4) + 80 - spriteRealSizes[0][1] * 4);
    } else {
        screeny = *heroy - (80 - spriteRealSizes[0][1] * 4);
        setSpriteY(0, 80 - spriteRealSizes[0][1] * 4);
    }
    moveScreen(screenx, screeny);
    lastherox = *herox;
    lastheroy = *heroy;
}

static void printPart(char* text) {
    u16 *text_out = (u16*)MAP_BASE_ADR(31);
    text_out += 380;
    for (int i = 0; i < 156; ++i) {
        if (i % 26 == 0) {
            text_out += 6;
        }
        if ((text[i] > 31) & (text[i] < 127)) {
            *text_out = (15 << 12) + text[i] - 31;
        } else {
            *text_out = (15 << 12) + 32 - 31;
        }
        text_out++;
    }

    while (true) {
        VBlankIntrWait();
        scanKeys();
        if (keysDown() & KEY_UP) {
            break;
        }
    }
}

void printText(char* text) {
    REG_DISPCNT = REG_DISPCNT | BG3_ON;

    int index = 0;
    int partLen = 0;
    char part[156] = {0};
    int wordLen = 0;
    char word[156] = {0};

    while (text[index] != 0) {
        if (partLen == 156) {
            printPart(part);
            for (int i = 0; i < 156; ++i) {
                part[i] = 0;
            }
            partLen = 0;
        }
        if ((text[index] == ' ') | (text[index] == 0)) {
            if (((partLen) % 26) + wordLen > 26) {
                for (int i = ((partLen) % 26); i < 26; ++i) {
                    part[partLen] = '!';
                    partLen++;
                }
            }
            if (partLen + wordLen >= 156) {
                printPart(part);
                for (int i = 0; i < 156; ++i) {
                    part[i] = 0;
                }
                partLen = 0;
            }
            for (int i = 0; i < wordLen; ++i) {
                part[partLen] = word[i];
                partLen++;
            }
            part[partLen] = ' ';
            partLen++;
            for (int i = 0; i < 156; ++i) {
                word[i] = 0;
            }
            wordLen = 0;
        } else {
            word[wordLen] = text[index];
            wordLen++;
        }
        index++;
    }
    printPart(part);

    REG_DISPCNT = REG_DISPCNT & ~BG3_ON;
}

void initText(char font[][8]) {
    REG_BG3CNT = TILE_BASE(3) | MAP_BASE(31) | BG_PRIORITY(0);

    if (font == NULL) {
        font = default_font;
    }

    u32 *font_out = (u32*)TILE_BASE_ADR(3);

    font_out += 8;

    for (int symbol_index = 32; symbol_index < 128; ++symbol_index) {
        for (int part_index = 0; part_index < 8; ++part_index) {
            u32 val = 0;
            char part = font[symbol_index][part_index];
            for (int bit_index = 0; bit_index < 8; ++bit_index) {
                if ((part >> bit_index) & 1) {
                    val += 15 << (4 * bit_index);
                } else {
                    val += 13 << (4 * bit_index);
                }
            }
            *font_out = val;
            font_out++;
        }
    }

    dmaCopy(BorderTextPal, BG_PALETTE + 252, 8);
    dmaCopy(BorderTextTileset, font_out, 24 * 4);

    *(((u16*)MAP_BASE_ADR(31)) + 353) = (15 << 12) + 97;
    *(((u16*)MAP_BASE_ADR(31)) + 380) = (61 << 10) + 97;
    *(((u16*)MAP_BASE_ADR(31)) + 577) = (31 << 11) + 97;
    *(((u16*)MAP_BASE_ADR(31)) + 604) = (63 << 10) + 97;
    for (int i = 354; i < 380; ++i) {
        *(((u16*)MAP_BASE_ADR(31)) + i) = (15 << 12) + 98;
    }
    for (int i = 412; i < 604; i += 32) {
        *(((u16*)MAP_BASE_ADR(31)) + i) = (61 << 10) + 99;
    }
    for (int i = 578; i < 604; ++i) {
        *(((u16*)MAP_BASE_ADR(31)) + i) = (31 << 11) + 98;
    }
    for (int i = 385; i < 576; i += 32) {
        *(((u16*)MAP_BASE_ADR(31)) + i) = (15 << 12) + 99;
    }
}

void initGraphics() {
    irqInit();
    irqEnable(IRQ_VBLANK);
    SetMode(BG0_ON | BG1_ON | BG2_ON | OBJ_ENABLE | OBJ_1D_MAP);

    REG_BG0CNT = TILE_BASE(0) | MAP_BASE(28) | BG_256_COLOR | BG_PRIORITY(3);
    REG_BG1CNT = TILE_BASE(0) | MAP_BASE(29) | BG_256_COLOR | BG_PRIORITY(1);
    REG_BG2CNT = TILE_BASE(0) | MAP_BASE(30) | BG_256_COLOR | BG_PRIORITY(0);

    // Don't show any sprites except for the first one
    for (int i = 0; i < 128; ++i) {
        spriteAttrs[i][0] = OBJ_DISABLE | OBJ_256_COLOR;
        setSpriteAttr0(i);
    }
}
