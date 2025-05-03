from engine.settings import *
import csv
import os

class MapData():
    def __init__(self, mapName: str) -> None:
        self.mapName: str = mapName

        self.tileset: list[pygame.Surface] = []
        self.__makeTileset()

        self.layers: list[list[list[int]]] = []
        self.__makeLayerData()

        self.drawMap()

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

        self.mapImage: pygame.Surface = pygame.Surface((64 * TILE_SIZE, 64 * TILE_SIZE))

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

    def drawMap(self) -> None:
        for _i, _layer in enumerate(self.layers):
            for _section in _layer:
                _x: int = 128
                _y: int = 0
                for _row in _section:
                    for _col in _row:
                        self.mapImage.blit(self.tileset[int(_col)], (_x - _y, (_x + _y) / 2))
                        _x += TILE_SIZE / 2
                    _y += TILE_SIZE / 2
                    _x: int = 128
