from engine.settings import *

class TileData():
    def __init__(self, gridCords: list[int], mapImageCords: list[int], image: pygame.Surface, imageID: str, tileInfo: dict[str, str]) -> None:
        self.gridCords: pygame.Vector2 = pygame.Vector2(gridCords)
        self.mapImageCords: pygame.Vector2 = pygame.Vector2(mapImageCords)

        self.image: pygame.Surface = image
        self.imageID: str = imageID

        self.tileInfo: dict[str, str] = tileInfo

        if int(self.tileInfo['Elv']) >= 1:
            self.gridCords.x += 1
            self.gridCords.y += 1

        self.rect: pygame.Rect = pygame.rect.Rect(
            int(self.mapImageCords.x - self.mapImageCords.y) + int(self.tileInfo['XOff']), 
            (int(self.mapImageCords.x + self.mapImageCords.y) // 2) + int(self.tileInfo['YOff']), 
            TILE_SIZE - int(self.tileInfo['WOff']), 
            (TILE_SIZE // 2) - int(self.tileInfo['HOff'])
        )

    def draw(self, surface: pygame.Surface) -> None:
        _blitCords: list[int] = [int(self.mapImageCords.x - self.mapImageCords.y), int(self.mapImageCords.x + self.mapImageCords.y) // 2]

        surface.blit(self.image, _blitCords)
        