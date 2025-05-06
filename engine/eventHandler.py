from engine.settings import *
from engine.keyHandler import KeyHandler
from engine.mapHandler import MapHandler

class EventHandler():
    def __init__(self, client) -> None:
        self.client: object = client
        
        self.keyHandler: KeyHandler = KeyHandler(client)
        self.mapHandler: MapHandler = MapHandler(client)

        self.drag: bool = False
        self.offset: pygame.Rect = pygame.Rect(0, 0, 0, 0)

        self.currentGrid: list[int] = [-1, -1]

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

        _mousePos = pygame.mouse.get_pos()
        _mouseScale = [display_width / SCREEN_WIDTH, display_height / SCREEN_HEIGHT]
        _mousePos = [_mousePos[0] / _mouseScale[0], _mousePos[1] / _mouseScale[1]]

        pygame.draw.rect(self.client.screen, '#ff00ff', pygame.Rect(_mousePos[0], _mousePos[1], 10, 10))

        for _tile in self.mapHandler.currentMap.tiles:
            if _tile.rect.collidepoint(_mousePos):
               self.currentGrid = _tile.gridCords

