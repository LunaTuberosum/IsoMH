from engine.settings import *

class KeyHandler():
    def __init__(self, client: object) -> None:
        self.client: object = client

    def keydown(self, delta: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            self.client.quit()

    def keyup(self):
        keys = pygame.key.get_just_released()