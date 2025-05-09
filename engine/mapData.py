from engine.settings import *
from engine.tileData import TileData

import csv
import json
import os

class MapData():
    def __init__(self, mapName: str) -> None:
        self.mapName: str = mapName

        self.tileset: list[pygame.Surface] = []
        self.__makeTileset()

        with open(f'.\\engine\\maps\\{self.mapName}\\TilesetData.json', 'r') as _json:
            self.tilesetData: dict[dict[str, str]] = json.load(_json)

        self.layers: list[list[list[list[int]]]] = []
        self.__makeLayerData()

        self.tiles: list[TileData] = []
        self.__makeMap()

    def __makeLayerData(self) -> None:
        _numOfLayers: list[str] = os.listdir(f'.\\engine\\maps\\{self.mapName}\\Map Data')
        for _layer in _numOfLayers:
            _layerArr = []
            for _section in os.listdir(f'.\\engine\\maps\\{self.mapName}\\Map Data\\{_layer}'):
                _sectionArr = []
                with open(f'.\\engine\\maps\\{self.mapName}\\Map Data\\{_layer}\\{_section}') as _data:
                    _data = csv.reader(_data, delimiter=',')

                    for _row in _data:
                        _sectionArr.append(list(_row))

                _layerArr.append(_sectionArr)

            self.layers.append(_layerArr)

        self.mapImage: pygame.Surface = pygame.Surface((100 * TILE_SIZE, 100 * TILE_SIZE))

    def __makeTileset(self) -> None:
        _image: pygame.Surface = pygame.image.load(f'.\\engine\\maps\\{self.mapName}\\Tileset.png').convert_alpha()
        
        for _y in range(_image.get_height() // TILE_SIZE):
            for _x in range(_image.get_width() // TILE_SIZE):
                _tile: pygame.Surface = pygame.surface.Surface((TILE_SIZE, TILE_SIZE))
                _tile.set_colorkey('#000000')
                _tile.blit(_image, (0, 0), pygame.rect.Rect(
                    _x * TILE_SIZE,
                    _y * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE,
                ))

                self.tileset.append(_tile)

    def __makeMap(self) -> None:
        for _layer in self.layers:
            for _section in _layer:
                _x: int = 0
                _y: int = 0
                for _row in _section:

                    for _col in _row:
                        if _col != '-1':
                            self.tiles.append(TileData([_x // 16, _y // 16], [_x + (TILE_SIZE * 32), _y], self.tileset[int(_col)], _col, self.tilesetData[_col]))
                        _x += TILE_SIZE // 2
                    _y += TILE_SIZE // 2
                    _x: int = 0

    def drawMap(self) -> None:
        self.mapImage.fill('#000000')
        for _tile in self.tiles:
            _tile.draw(self.mapImage)
