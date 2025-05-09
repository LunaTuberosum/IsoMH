from engine.settings import *
from engine.keyHandler import KeyHandler
from engine.mapHandler import MapHandler
from engine.tileData import TileData

import math

class EventHandler():
    def __init__(self, client) -> None:
        from client import Main
        self.client: Main = client
        
        self.keyHandler: KeyHandler = KeyHandler(client)
        self.mapHandler: MapHandler = MapHandler(client)

        self.drag: bool = False
        self.offset: pygame.Rect = pygame.Rect(0, 0, 0, 0)

        self.currentTile: TileData = None

    def checkEvent(self, delta: float) -> None:

        self.keyHandler.keydown(delta)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.client.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.drag = True

            if event.type == pygame.MOUSEMOTION:

                if self.drag:
                    self.offset.move_ip(event.rel[0] / 2, event.rel[1] / 2)
                    for _tile in self.mapHandler.currentMap.tiles:
                        _tile.rect.move_ip(event.rel[0] / 2, event.rel[1] / 2)


            if event.type == pygame.MOUSEBUTTONUP:
                self.drag = False

        self.keyHandler.keyup()

        self.mapHandler.draw(self.offset.x, self.offset.y)

        self.checkTile()

    def checkTile(self):
        self.currentTile = None

        _mousePos: list[float] = pygame.mouse.get_pos()
        _mouseScale: list[float] = [display_width / SCREEN_WIDTH, display_height / SCREEN_HEIGHT]
        _mousePos: list[float] = [_mousePos[0] / _mouseScale[0], _mousePos[1] / _mouseScale[1]]

        _collidedTiles: list[TileData] = []
        for _tile in self.mapHandler.currentMap.tiles:
            if _tile.rect.collidepoint(_mousePos):
                _collidedTiles.append(_tile)

        _closestTile: TileData = None
        _tileDist: float = 99999

        for _tile in _collidedTiles:
            _x: float = _tile.rect.centerx - _mousePos[0]
            _y: float = _tile.rect.centery - _mousePos[1]
            _dist: float = math.sqrt(pow(_x, 2) + pow(_y, 2))

            if _dist < _tileDist:
               _closestTile = _tile
               _tileDist = _dist
               
        if _closestTile:
            self.currentTile = _closestTile
