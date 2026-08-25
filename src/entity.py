
import numpy as np


class Direction:
    N = 0
    NE = 1
    E = 2
    SE = 3
    S = 4
    SW = 5
    W = 6
    NW = 7

class Entity:
    def __init__(self, name: str, pos=(0, 0)):
        self.name = name
        self.x = pos[0]
        self.y = pos[1]
        self.x_vel = 0
        self.y_vel = 0
        self.width = 40
        self.height = 64
        self.direction = Direction.E
        self.stepFreq = 0
        self.speed = 1.2
        self.sprint = 1
        self.animation = None

    def update(self):
        self.move()
        self.animation.update()

    def move(self):
        if self.x_vel ** 2 + self.y_vel ** 2 > self.speed ** 2:
            theta = np.arctan2(np.abs(self.y_vel), np.abs(self.x_vel))
            self.x_vel = np.sign(self.x_vel) * self.speed * np.cos(theta)
            self.y_vel = np.sign(self.y_vel) * self.speed * np.sin(theta)
        
        self.x += self.x_vel * self.sprint
        self.y += self.y_vel * self.sprint

        self.x_vel = self.x_vel * 0.8
        self.y_vel = self.y_vel * 0.8

        if self.sprint == 1:
            pass
        elif self.sprint > 1:
            self.sprint = self.sprint * 0.9
        else:
            self.sprint = 1

        