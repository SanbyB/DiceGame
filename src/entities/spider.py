from entity import Entity
from resources import SpiderSprite

class Spider(Entity):
    def __init__(self, world, pos=(0, 0)):
        super().__init__("Spider", world, pos)
        self.animation = SpiderSprite.SPIDER_IDLE
        self.width = self.animation.spritesheet.imageWidth * self.scale
        self.height = self.animation.spritesheet.imageHeight * self.scale
        self.moveable = True

        self.hp = 15