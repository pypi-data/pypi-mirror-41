#ifndef GRAPHICS_H
#define GRAPHICS_H

void moveScreen();

void forceMoveScreen(int screenx, int screeny);

{% for map_name in maps.keys() %}
void loadMap{{ map_name }}();
{% endfor %}
{% for sprite_image_name in sprite_images.keys() %}
void loadSpriteImage{{ sprite_image_name }}();

void unloadSpriteImage{{ sprite_image_name }}();
{% endfor %}

void clearSpriteGraphics();

void setSpriteX(int spriteIndex, int x);

void setSpriteY(int spriteIndex, int y);

void setSpriteDisable(int spriteIndex);

void setSpriteEnable(int spriteIndex);

void setSpritePriority(int spriteIndex, int p);

{% for sprite_image_name in sprite_images.keys() %}
void setSpriteGraphics{{ sprite_image_name }}(int spriteIndex);
{% endfor %}

int spriteCheckForSpecials(int spriteIndex, int spritex, int spritey, bool justOne);

bool checkSpriteCollision(int spriteIndex1, int sprite1x, int sprite1y, int spriteIndex2, int sprite2x, int sprite2y);

void moveHero(int* herox, int* heroy);

void printText(char* text);

void initText(char font[][8]);

void initGraphics();

#endif
