
from math import floor

class Animation:
    def __init__(self, spritesheet, rowIndex, speed):
        self.spritesheet = spritesheet
        self.yFrame = rowIndex
        self.frame = 0
        self.speed = speed
        return


    def update(self):
        self.frame += self.speed
        return

    def draw(self, surface, x, y):
        xFrame = floor(self.frame) % self.spritesheet.xFrames
        self.spritesheet.draw(
            surface,
            xFrame,
            self.yFrame,
            x, y
        )
        return

    def reset(self):
        self.frame = 0




