from entity import Entity
from resources import SlimeSprite


class Slime(Entity):
    def __init__(self, pos=(0, 0)):
        super().__init__("Slime", pos)
        self.animation = SlimeSprite.SLIME_IDLE
        self.width = self.animation.spritesheet.imageWidth * self.scale
        self.height = self.animation.spritesheet.imageHeight * self.scale
        self.moveable = True