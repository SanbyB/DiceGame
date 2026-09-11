from graphics.resources import MAP
from config import TILE_SIZE
from entities.slime import Slime
from entities.wall import Wall
from player import Player
from objects.foliage import *

class MapLoader():
    def __init__(self, world):

        self.map = MAP
        self.world = world
        self.width, self.height = MAP.size

    def loadMap(self):
        for x in range(self.width):
            for y in range(self.height):
                r,g,b,a = self.map.getpixel((x,y))
                pos = (x * TILE_SIZE, y * TILE_SIZE)
                if r == 255 and g == 0 and b == 0:
                    self.world.addEntity(Slime(self.world, pos))
                if r == 0 and g == 255 and b == 0:
                    self.world.addPlayer(Player(self.world, pos))
                if r == 0 and g == 0 and b == 0:
                    self.world.addEntity(Wall(self.world, pos))
                if r == 75 and g == 105 and b == 47:
                    self.world.addSTObject(SpruceTree(pos))
                    
        return self.world