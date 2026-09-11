import random

from graphics.animation import Animation
from object import Object
from graphics.resources import Foliage


class Bush(Object):
    def __init__(self, pos=(0, 0)):
        super().__init__(pos)
        self.animation = Foliage.BUSH
        self.width = self.animation.spritesheet.imageWidth * self.scale
        self.height = self.animation.spritesheet.imageHeight * self.scale
        # self.collidable = False  # Bushes are not collidable, so the player can walk through them

class Tree(Object):
    def __init__(self, pos=(0, 0)):
        super().__init__(pos)
        self.animation = Foliage.TREE
        self.scale = 4
        self.width = self.animation.spritesheet.imageWidth * self.scale
        self.height = self.animation.spritesheet.imageHeight * self.scale
        # self.collidable = False  # Trees are not collidable, so the player can walk through them

class Flowers(Object):
    def __init__(self, pos=(0, 0), speed=0.05):
        super().__init__(pos)
        self.animation = Animation(Foliage.FLOWERS, 0, speed)  # Random speed for each flower instance
        self.width = self.animation.spritesheet.imageWidth * self.scale
        self.height = self.animation.spritesheet.imageHeight * self.scale
        # self.animation.setFrame(random.randint(0, self.animation.spritesheet.xFrames - 1))  # Set the initial frame to a random frame of the animation

class SpruceTree(Object):
    def __init__(self, pos=(0, 0)):
        super().__init__(pos)
        self.state = {"default": Foliage.SPRUCE_TREE, "seeThrough": Foliage.SPRUCE_TREE_ST}
        self.animation = Foliage.SPRUCE_TREE
        self.scale = 4
        self.width = self.animation.spritesheet.imageWidth * self.scale
        self.height = self.animation.spritesheet.imageHeight * self.scale
        self.collidable = True

class Rock(Object):
    def __init__(self, pos=(0, 0)):
        super().__init__(pos)
        self.state = {"default": Foliage.ROCK, "seeThrough": Foliage.ROCK_ST}
        self.animation = Foliage.ROCK
        self.scale = 3
        self.width = self.animation.spritesheet.imageWidth * self.scale
        self.height = self.animation.spritesheet.imageHeight * self.scale
        self.collidable = True
