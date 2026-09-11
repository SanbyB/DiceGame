from entity import Entity
from graphics.resources import WallSprite
import pygame

class Wall(Entity):
    # pos is changed to a tile grid, which is multiplied by the size of the tile
    def __init__(self, world, pos=(0, 0)):
        self.spriteSheet = WallSprite.WALL
        scale = 2
        imgWidth = self.spriteSheet.imageWidth * scale
        imgHeight = self.spriteSheet.imageHeight * scale

        # pos = (pos[0] * imgWidth, pos[1] * imgHeight)

        super().__init__("wall", world, pos)

        # has to be set after the call to super()
        self.width = imgWidth
        self.height = imgHeight
        self.scale = scale



    def render(self, screen, camera):
        xPos = self.x - camera.x
        yPos = self.y - camera.y

        self.spriteSheet.draw(screen, 1, 1, xPos, yPos, scale=self.scale)
                
        