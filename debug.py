from engine.settings import *

class Debug():
    def __init__(self, client: object) -> None:
        from client import Main
        self.client: Main = client

        self.__active: bool = False
        self.changed: bool = False

        self.font: pygame.Font = pygame.font.SysFont("Arial", 10)

        self.__sections: dict[str, bool] = {
            'Tile': False
        }

        self.tileSelector: int = '-1'

        self.components: list[str] = self.updateComponents()

    def updateComponents(self) -> None:
        return [
            f'FPS: {round(self.client.clock.get_fps())}',
            f'MAP: {self.client.eventHandler.mapHandler.currentMapName}',
            f'[X, Y]: {self.client.eventHandler.currentTile.gridCords if self.client.eventHandler.currentTile else "[-1, -1]"}',
            f'',
            f'Tiles: {self.__sections["Tile"]}',
            f'T ID: {self.tileSelector}'
        ]

    def toggleActive(self) -> None:
        self.__active = not self.__active

    def getActive(self) -> bool:
        return self.__active

    def getChanged(self) -> bool:
        return self.changed
    
    def checkChanged(self) -> bool:
        return False == self.changed

    def setChanged(self) -> None:
        self.changed = True

    def resetChanged(self) -> None:
        self.changed = False

    def toggleSectionActive(self, sectionName: str) -> None:
        self.__sections[sectionName] = not self.__sections[sectionName]

    def draw(self) -> None:
        ## Checking if not on
        if not self.__active: return

        ## Resting Components
        self.components = self.updateComponents()

        ## Drawing Components
        _x: int = 5
        _y: int = 2
        for _item in self.components:
            self.client.screen.blit(self.font.render(_item, False, '#ffffff'), (_x, _y))
            _y += 10

        ## Drawing Mouse Square
        _mousePos: list[float] = pygame.mouse.get_pos()
        _mouseScale: list[float] = [display_width / SCREEN_WIDTH, display_height / SCREEN_HEIGHT]
        _mousePos: list[float] = [_mousePos[0] / _mouseScale[0], _mousePos[1] / _mouseScale[1]]
        _rect: pygame.Rect = pygame.Rect(0, 0, 4, 4) 
        _rect.center = [_mousePos[0], _mousePos[1]]

        pygame.draw.rect(self.client.screen, '#ff00ff', _rect)

        ## Drawing tile hit boxes
        if self.__sections['Tile']:
            for _tile in self.client.eventHandler.mapHandler.currentMap.tiles:
                match (self.tileSelector):
                    case '-1': 
                        pygame.draw.rect(self.client.screen, pygame.color.Color(255, 0, 0, 100), _tile.rect, 1)
                    case _:
                        if _tile.imageID == self.tileSelector:
                            pygame.draw.rect(self.client.screen, pygame.color.Color(255, 0, 0, 100), _tile.rect, 1)

            if self.client.eventHandler.currentTile: pygame.draw.rect(self.client.screen, '#00ff00', self.client.eventHandler.currentTile.rect, 1)