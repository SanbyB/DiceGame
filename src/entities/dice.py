from entity import Entity
from resources import DiceSprite

class Dice(Entity):
    def __init__(self, pos=(0, 0)):
        super().__init__("Dice", pos=pos)
        self.animation = DiceSprite.DICE_IDLE