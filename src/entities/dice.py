import random
from entity import Entity
from resources import DiceSprite

class Dice(Entity):
    def __init__(self, sides=6, pos=(0, 0)):
        super().__init__("Dice", pos=pos)
        self.animation = DiceSprite.DICE_IDLE
        self.width = self.animation.spritesheet.imageWidth * self.scale
        self.height = self.animation.spritesheet.imageHeight * self.scale
        self.moveable = True
        self.sides = sides

        self.speedDamp = 0.95
        self.speed = 10

    def roll(self, vel):
        self.x_vel = vel[0]
        self.y_vel = vel[1]
        return random.randint(1, self.sides)

        