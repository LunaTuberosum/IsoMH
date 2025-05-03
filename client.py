from engine.settings import *
from engine.eventHandler import EventHandler

class Main():
    def __init__(self) -> None:
        pygame.init()
        
        self._d_font: pygame.Font = pygame.font.SysFont("Arial", 10)
        self._debug: bool = True

        self.screen: pygame.Surface = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display: pygame.Surface = pygame.display.set_mode((display_width, display_height))
        self.clock: pygame.Clock = pygame.time.Clock()

        self.__setUpHandlers()
        
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

            if self._debug: self.screen.blit(self._d_font.render(f'FPS: {round(self.clock.get_fps())}', False, '#ffffff'), (5, 2))
            self.__scaleScreenToDisplay()

            pygame.display.flip()

if __name__ == "__main__":
    Main().main()