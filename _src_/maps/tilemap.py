

from maps.tile import Air, Floor
from math import ceil, floor
from config import SCREEN_WIDTH, SCREEN_HEIGHT
# from entities.entity import Entity
import random
import pygame

TILE_MAP_WIDTH = 20
TILE_SIZE = 80

class TileMap:
    def __init__(self, world):
        self.world = world
        self.tiles = []
        for i in range(TILE_MAP_WIDTH):
            tileRow = []
            for j in range(TILE_MAP_WIDTH):
                tileRow.append(Floor(self.world, i, j))
                if j == TILE_MAP_WIDTH - 1:
                    self.tiles.append(tileRow)
        # self.generateChunk()
        return

    def render(self, surface, camera):        
        xPos = camera.x
        yPos = camera.y
        xWidth = SCREEN_WIDTH
        yHeight = SCREEN_HEIGHT

        # When camera is lower than what we've generated, generate more tiles
        # targetTileHeight = ceil((yPos + yHeight) / TILE_SIZE)
        # if (targetTileHeight > len(self.tiles)):
        #     for x in range(targetTileHeight - len(self.tiles)):
        #         self.generateChunk()

        xTilePos = floor(xPos / TILE_SIZE)
        yTilePos = floor(yPos / TILE_SIZE)
        xTileWidth = ceil((xPos + xWidth) / TILE_SIZE)
        yTileHeight = ceil((yPos + yHeight) / TILE_SIZE)

        xTilePos = min(max(xTilePos, 0), TILE_MAP_WIDTH)
        yTilePos = min(max(yTilePos, 0), len(self.tiles))
        xTileWidth = min(max(xTileWidth, 0), TILE_MAP_WIDTH)
        yTileHeight = min(max(yTileHeight, 0), len(self.tiles))

        # Draw the tiles
        for tileY in range(yTilePos, yTileHeight):
            for tileX in range(xTilePos, xTileWidth):
                xRender = (tileX * TILE_SIZE) - xPos
                yRender = (tileY * TILE_SIZE) - yPos
                tile = self.tiles[tileY][tileX]
                tile.render(surface, xRender, yRender, TILE_SIZE)

        
        return

    def doesCollide(self, x, y):
        xTilePos = floor(x / TILE_SIZE)
        yTilePos = floor(y / TILE_SIZE)
        if (xTilePos < 0 or xTilePos >= TILE_MAP_WIDTH):
            return True
        #TODO   
        if (yTilePos < 0 or yTilePos >= TILE_MAP_WIDTH):
            return True
        return False
        return self.tiles[yTilePos][xTilePos].doesCollide

        









