from maps.tilemap import TileMap
import pygame
import math
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from maps.tilemap import TILE_MAP_WIDTH, TILE_SIZE
# from entities.entity import Entity

class World:
    def __init__(self, camera):
        self.player = None
        self.camera = camera
        self.tileMap = TileMap(self)



    def render(self, surface, camera):   
        
        pygame.draw.rect(surface, (0, 0, 0), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        
        camX = camera.x
        camRight = camera.x + SCREEN_WIDTH
        if camX < 0:
            camX = 0
        if camRight > TILE_MAP_WIDTH * TILE_SIZE:
            camRight = TILE_MAP_WIDTH * TILE_SIZE

        camY = camera.y
        camDown = camera.y + SCREEN_HEIGHT
        if camY < 0:
            camY = 0
        #TODO change to tile map height
        if camDown > TILE_MAP_WIDTH * TILE_SIZE:
            camDown = TILE_MAP_WIDTH * TILE_SIZE

        pygame.draw.rect(surface, (28, 22, 27), (camX - camera.x, camY - camera.y, camRight - camX, camDown - camY))

        leftOfScreen = self.player.x - SCREEN_WIDTH/2
        roundedLOS = 100 * int(math.ceil(leftOfScreen/100))

        topOfScreen = self.player.y - SCREEN_HEIGHT/2
        roundedTOS = 100 * int(math.ceil(topOfScreen/100))

        for i in range(int(math.ceil(SCREEN_WIDTH/100))):
            pygame.draw.rect(surface, (255, 255, 255), (roundedLOS + 100 * i - camera.x, 0, 1, SCREEN_HEIGHT))
        for i in range(int(math.ceil(SCREEN_HEIGHT/100))):
            pygame.draw.rect(surface, (255, 255, 255), (0, roundedTOS + 100 * i - camera.y, SCREEN_WIDTH, 1))

        self.tileMap.render(surface, camera)
        self.player.render(surface, camera)
            





