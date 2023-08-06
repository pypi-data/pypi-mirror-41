#ifndef IMAGE_DATA_H
#define IMAGE_DATA_H

// Background stuff

{% for map_name, map in maps.items() %}
#define {{ map_name }}PaletteLen {{ 2 * map.palette|length }}
extern const unsigned short {{ map_name }}Palette[{{ map.palette|length }}];

#define {{ map_name }}TilesetLen {{ 4 * map.tileset|length }}
extern const unsigned int {{ map_name }}Tileset[{{ map.tileset|length }}];

extern const int {{ map_name }}Size[2];

extern const int {{ map_name }}Specials[{{ map.specials|length }}];

{%- for i in range(map.layer_tile_maps|length) %}

#define {{ map.layer_names[i] }}Len {{ 2 * map.layer_tile_maps[i]|length }}
extern const int {{ map.layer_names[i] }}Size[2];
extern const unsigned short {{ map.layer_names[i] }}[{{ map.layer_tile_maps[i]|length }}];
{%- endfor %}
{% endfor %}

// Sprite stuff

{%- for sprite_image_name, sprite_image in sprite_images.items() %}

#define {{ sprite_image_name }}Shape {{ sprite_image.shape_size[0] }}
#define {{ sprite_image_name }}Size {{ sprite_image.shape_size[1] }}
extern const unsigned short {{ sprite_image_name }}RealSize[2];

#define {{ sprite_image_name }}PaletteLen {{ sprite_image.palette|length }}
extern const unsigned short {{ sprite_image_name }}Palette[{{ sprite_image.palette|length }}];

#define {{ sprite_image_name }}TilesetLen {{ sprite_image.tileset|length }}
extern const unsigned {{ sprite_image_name }}Tileset[{{ sprite_image.tileset|length }}];
{% endfor %}

const unsigned int BorderTextTileset[24];
const unsigned short BorderTextPal[4];
char default_font[128][8];
#endif
