
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
        self.x_acc = 0
        self.y_acc = 0

        self.speed = 2
        self.sprintSpeed = 1
        self.sprintResetTime = 0

        self.direction = Direction.FORWARD

        self.width = 40
        self.height = 64
        
        self.animation = None

        self.hp = 1


    def update(self):
        self.move()
        self.animation.update()

    def move(self):
        self.speedLimit()
        self.integrate(0)
        self.dampSpeed()
        self.sprintCooldown()        

    def speedLimit(self):
        if self.x_vel ** 2 + self.y_vel ** 2 > self.speed ** 2:
            theta = np.arctan2(np.abs(self.y_vel), np.abs(self.x_vel))
            self.x_vel = np.sign(self.x_vel) * self.speed * np.cos(theta)
            self.y_vel = np.sign(self.y_vel) * self.speed * np.sin(theta)

    def integrate(self, dt):
        self.x_vel += self.x_acc
        self.y_vel += self.y_acc

        self.x += self.x_vel * self.sprintSpeed
        self.y += self.y_vel * self.sprintSpeed

    def dampSpeed(self, amount = 0.7):
        if self.x_acc == 0 and self.y_acc == 0:
            self.x_vel = self.x_vel * amount
            self.y_vel = self.y_vel * amount

        if self.x_vel < 0.01 and self.x_vel > -0.01:
            self.x_vel = 0

        if self.y_vel < 0.01 and self.y_vel > -0.01:
            self.y_vel = 0

    def sprint(self, amount):
        self.sprintSpeed = amount
        self.sprintResetTime = 10 # make configurable later

    def sprintCooldown(self):
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

    def render(self, screen, camera):
        xPos = self.x - camera.x
        yPos = self.y - camera.y
        
        # Render the entity on the screen
        self.animation.draw(
            surface=screen,
            x=xPos,
            y=yPos,
            rotate=0,
            scale=1.5
        )

        