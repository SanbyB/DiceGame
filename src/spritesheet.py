
import pygame
from math import floor

class SpriteSheet:
    def __init__(self, image, xFrames, yFrames):
        self.image = image
        self.xFrames = xFrames
        self.yFrames = yFrames
        self.imageWidth = self.image.get_width() / self.xFrames
        self.imageHeight = self.image.get_height() / self.yFrames

    def draw(self, surface, xFrame, yFrame, x, y):
        rotatedImage = pygame.transform.rotate(self.image, 0)
        surface.blit(rotatedImage, (x, y), (xFrame * self.imageWidth, yFrame * self.imageHeight, self.imageWidth, self.imageHeight))

