import os
from engine.settings import *
from engine.mapData import MapData

class MapHandler():
    def __init__(self, client: object, starterMap='None') -> None:
        from client import Main
        self.client: Main = client

        self.maps: list[str] = os.listdir('.\\engine\\maps')
        self.currentMapName: str = starterMap if starterMap != 'None' else self.maps[0] ## Temp
        self.currentMap: MapData = self.createMap()

    def createMap(self) -> MapData:
        return MapData(self.currentMapName)
    
    def draw(self, x_offset: int, y_offset: int) -> None:
        self.currentMap.drawMap()
        self.client.screen.blit(self.currentMap.mapImage, (0 + x_offset, 0 + y_offset))