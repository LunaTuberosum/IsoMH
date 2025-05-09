from engine.settings import *

class KeyHandler():
    def __init__(self, client: object) -> None:
        from client import Main
        self.client: Main = client

    def keydown(self, delta: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            self.client.quit()

        ## DEBUG HANDLER
        if keys[pygame.K_F1]:
            if self.client.debug.checkChanged():
                self.client.debug.toggleActive()
                self.client.debug.setChanged()

        if self.client.debug.getActive() and keys[pygame.K_F2]:
            if self.client.debug.checkChanged():
                self.client.debug.toggleSectionActive('Tile')
                self.client.debug.setChanged()

        if self.client.debug.getActive() and keys[pygame.K_RIGHT]:
            if self.client.debug.checkChanged():
                self.client.debug.tileSelector = f'{int(self.client.debug.tileSelector) + 1}'
                self.client.debug.setChanged()

        if self.client.debug.getActive() and keys[pygame.K_LEFT]:
            if self.client.debug.checkChanged():
                self.client.debug.tileSelector = f'{int(self.client.debug.tileSelector) - 1}'
                self.client.debug.setChanged()

    def keyup(self):
        keys = pygame.key.get_just_released()

        ## DEBUG HANDLER
        if keys[pygame.K_F1]:
            self.client.debug.resetChanged()

        if self.client.debug.getActive() and keys[pygame.K_F2]:
            self.client.debug.resetChanged()

        if self.client.debug.getActive() and keys[pygame.K_RIGHT]:
            self.client.debug.resetChanged()

        if self.client.debug.getActive() and keys[pygame.K_LEFT]:
            self.client.debug.resetChanged()
