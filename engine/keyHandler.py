from engine.settings import *

class KeyHandler():
    def __init__(self, client: object) -> None:
        self.client: object = client

    def keydown(self, delta: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            self.client.quit()

        ## DEBUG HANDLER
        if keys[pygame.K_F1]:
            if self.client.debug.checkChanged():
                self.client.debug.toggleActive()

    def keyup(self):
        keys = pygame.key.get_just_released()

        ## DEBUG HANDLER
        if keys[pygame.K_F1]:
            self.client.debug.setChanged()
