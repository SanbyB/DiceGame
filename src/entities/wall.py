from entity import Entity
from resources import WALL
import pygame

class Wall(Entity):
    def __init__(self, world, pos=(0, 0)):
        super().__init__("wall", world, pos)
        self.image = WALL
        self.scale = 2
        self.width = self.image.get_width() * self.scale
        self.height = self.image.get_height() * self.scale

        self.scaledImage = pygame.transform.scale(self.image, (int(self.width), int(self.height)))


    def render(self, screen, camera):
        xPos = self.x - camera.x
        yPos = self.y - camera.y

        screen.blit(self.scaledImage, (xPos - self.width/2, yPos - self.height/2))

                
        