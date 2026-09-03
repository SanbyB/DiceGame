
import numpy as np


class Direction:
    FORWARD = 0
    BACKWARD = 1
    LEFT = 2
    RIGHT = 3

class Entity:
    def __init__(self, name: str, pos=(0, 0)):
        self.name = name
        self.x = pos[0]
        self.y = pos[1]
        self.x_vel = 0
        self.y_vel = 0
        self.width = 40
        self.height = 64
        self.direction = Direction.FORWARD
        self.stepFreq = 0
        self.speed = 3
        self.sprintSpeed = 1
        self.sprintResetTime = 0
        self.animation = None

    def update(self):
        self.move()
        self.animation.update()

    def move(self):
        if self.x_vel ** 2 + self.y_vel ** 2 > self.speed ** 2:
            theta = np.arctan2(np.abs(self.y_vel), np.abs(self.x_vel))
            self.x_vel = np.sign(self.x_vel) * self.speed * np.cos(theta)
            self.y_vel = np.sign(self.y_vel) * self.speed * np.sin(theta)
        
        self.x += self.x_vel * self.sprintSpeed
        self.y += self.y_vel * self.sprintSpeed

        self.x_vel = self.x_vel * 0.7
        self.y_vel = self.y_vel * 0.7

        if self.x_vel < 0.01 and self.x_vel > -0.01:
            self.x_vel = 0

        if self.y_vel < 0.01 and self.y_vel > -0.01:
            self.y_vel = 0

        if self.sprintSpeed == 1:
            pass
        elif self.sprintSpeed > 1:
            self.sprintSpeed = self.sprintSpeed * 0.9
        else:
            self.sprintSpeed = 1

        if self.sprintResetTime == 0:
            pass            
        elif self.sprintResetTime > 0:
            self.sprintResetTime -= 0.1
        elif self.sprintResetTime < 0:
            self.sprintResetTime = 0

    def sprint(self, amount):
        self.sprintSpeed = amount
        self.sprintResetTime = 10

        