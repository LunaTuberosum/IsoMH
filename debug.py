from engine.settings import *

class Debug():
    def __init__(self, client: object) -> None:
        self.client: object = client
        self.__active: bool = False
        self.changed: bool = False

        self.font: pygame.Font = pygame.font.SysFont("Arial", 10)

        self.components: list[str] = [
            f'FPS: {round(self.client.clock.get_fps())}',
            f'MAP: {self.client.eventHandler.mapHandler.currentMapName}',
            f'[X, Y]: {self.client.eventHandler.currentGrid}'
        ]

    def toggleActive(self) -> None:
        self.__active = not self.__active

    def getChanged(self) -> bool:
        return self.changed
    
    def checkChanged(self) -> bool:
        return self.__active == self.changed

    def setChanged(self) -> None:
        self.changed = self.__active

    def draw(self) -> None:
        if not self.__active: return

        self.components = [
            f'FPS: {round(self.client.clock.get_fps())}',
            f'MAP: {self.client.eventHandler.mapHandler.currentMapName}',
            f'[X, Y]: {self.client.eventHandler.currentGrid}'
        ]

        _x: int = 5
        _y: int = 2
        for _item in self.components:
            self.client.screen.blit(self.font.render(_item, False, '#ffffff'), (_x, _y))
            _y += 10