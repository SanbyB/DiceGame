import random
from entity import Entity
from resources import DiceSprite

class Dice(Entity):
    def __init__(self, world, sides=6, pos=(0, 0)):
        super().__init__("Dice", world, pos=pos)
        self.animation = DiceSprite.DICE_1
        self.key = {1: DiceSprite.DICE_1, 2: DiceSprite.DICE_2, 3: DiceSprite.DICE_3, 4: DiceSprite.DICE_4, 5: DiceSprite.DICE_5, 6: DiceSprite.DICE_6,\
                    7: DiceSprite.DICE_1_IN_RANGE, 8: DiceSprite.DICE_2_IN_RANGE, 9: DiceSprite.DICE_3_IN_RANGE, 10: DiceSprite.DICE_4_IN_RANGE, 11: DiceSprite.DICE_5_IN_RANGE, 12: DiceSprite.DICE_6_IN_RANGE}
        self.scale = 1
        self.spinTime = 0
        
        self.width = self.animation.spritesheet.imageWidth * self.scale
        self.height = self.animation.spritesheet.imageHeight * self.scale
        self.moveable = True
        self.sides = sides

        self.speedDamp = 0.95
        self.speed = 10

        self.inrange = False
        self.player = None

        self.currentRoll = 1  # Store the current roll value

    def roll(self, vel):
        self.spinTime = 20
        self.x_vel = vel[0]
        self.y_vel = vel[1]
        result = random.randint(1, self.sides)
        # self.animation = self.key[result]
        # print(f"Dice rolled: {result}")
        self.currentRoll = result  # Update the current roll value

    def update(self):
        super().update()
        self.inRange()
        if self.spinTime > 0:
            self.spinTime -= 1
            self.angle += self.spinTime  # Rotate the dice while spinning

    def inRange(self):
        if (self.x - self.player.x) ** 2 + (self.y - self.player.y) ** 2 < 15000 and not self.inrange: # if the dice is within range of the player
            self.animation = self.key[self.currentRoll + 6]
            self.inrange = True
        elif (self.x - self.player.x) ** 2 + (self.y - self.player.y) ** 2 >= 15000 and self.inrange:
            self.animation = self.key[self.currentRoll]
            self.inrange = False
        

        