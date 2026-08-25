import pygame
from pygame import Rect
from resources import audio, PLANKS
import random
from math import ceil, floor
from particle import Particle


class Tile:
    def __init__(self, world, type, tileX, tileY, doesCollide):
        self.world = world
        self.type = type
        self.doesCollide = doesCollide
        self.tileX = tileX
        self.tileY = tileY
        return

    def render(self, surface, x, y, size, tiles):
        return


class Air(Tile):
    def __init__(self, world, tileX, tileY):
        super().__init__(world, "Air", tileX, tileY, False)

    def render(self, surface, x, y, size, tiles):
        return
        
        
class Floor(Tile):
    def __init__(self, world, tileX, tileY):
        super().__init__(world, "Floor", tileX, tileY, False)

    def render(self, surface, x, y, size):
        super().render(surface, x, y, size, None)
        scaledImage = pygame.transform.scale(PLANKS, (size, size)) 
        surface.blit(scaledImage, (x, y))
        return
