
import pygame
from math import floor

class SpriteSheet:
    def __init__(self, image, xFrames, yFrames):
        self.image = image
        self.xFrames = xFrames
        self.yFrames = yFrames
        self.imageWidth = self.image.get_width() / self.xFrames
        self.imageHeight = self.image.get_height() / self.yFrames

    def draw(self, surface, xFrame, yFrame, x, y, rotate=0, scale=1):
        frame = pygame.Surface((self.imageWidth, self.imageHeight), pygame.SRCALPHA)
        frame.blit(self.image, (0, 0), (xFrame * self.imageWidth, yFrame * self.imageHeight, self.imageWidth, self.imageHeight))
        scaledImage = pygame.transform.scale(frame, (int(self.imageWidth) * scale, int(self.imageHeight) * scale))
        rotatedImage = pygame.transform.rotate(scaledImage, rotate)
        surface.blit(rotatedImage, (x - scale * self.imageWidth/2, y - scale * self.imageHeight/2))