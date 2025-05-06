from engine.settings import *
import math

class TileData():
    def __init__(self, gridCords: list[int], mapImageCords: list[int], image: pygame.Surface, imageID: str) -> None:
        self.gridCords: pygame.Vector2 = pygame.Vector2(gridCords)
        self.mapImageCords: pygame.Vector2 = pygame.Vector2(mapImageCords)

        self.image: pygame.Surface = image
        self.imageID: str = imageID

        self.rect: pygame.Rect = pygame.rect.Rect(int(self.mapImageCords.x - self.mapImageCords.y), int(self.mapImageCords.x + self.mapImageCords.y) // 2, TILE_SIZE, TILE_SIZE // 2)

        ## dubug
        self.font: pygame.Font = pygame.font.SysFont("Arial", 8)

    
    def draw(self, surface: pygame.Surface, x_offset: int, y_offset: int) -> None:
        _blitCords: list[int] = [int(self.mapImageCords.x - self.mapImageCords.y), int(self.mapImageCords.x + self.mapImageCords.y) // 2]

        surface.blit(self.image, _blitCords)
        # surface.blit(self.font.render(f'{self.gridCords.x}, {self.gridCords.y}', False, '#ffffff'), [_blitCords[0] + 8, _blitCords[1]])
        