from engine.settings import *
from engine.eventHandler import EventHandler
from debug import Debug

class Main():
    def __init__(self) -> None:
        pygame.init()
        pygame.key.set_repeat(200, 200)
        
        self.screen: pygame.Surface = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display: pygame.Surface = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Client')
        self.clock: pygame.Clock = pygame.time.Clock()

        self.__setUpHandlers()
        self.debug: Debug = Debug(self)
        
    def __setUpHandlers(self) -> None:
        self.eventHandler: EventHandler = EventHandler(self)

    def __scaleScreenToDisplay(self) -> None:
        temp: pygame.Surface = pygame.transform.scale(self.screen, self.display.size)

        self.display.blit(temp)

    def quit(self) -> None:
        pygame.quit()
        sys.exit(-1)

    def main(self) -> None:

        while True:
            self.screen.fill("#000000")

            delta: float = self.clock.tick(30) / 1000

            self.eventHandler.checkEvent(delta)

            self.debug.draw()

            self.__scaleScreenToDisplay()

            pygame.display.flip()

if __name__ == "__main__":
    Main().main()