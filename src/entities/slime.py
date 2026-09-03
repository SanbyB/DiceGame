from entity import Entity
from resources import SlimeSprite


class Slime(Entity):
    def __init__(self, pos=(0, 0)):
        super().__init__("Slime", pos)
        self.width = 40
        self.height = 40
        self.animation = SlimeSprite.SLIME_IDLE