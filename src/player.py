import pygame
import numpy as np
from entity import *
# from resources import LADYBIRD_WALKING
from resources import Warrior

WALK_ACCN = 0.5

class Player(Entity):
    def __init__(self):
        super().__init__("Player")
        self.keysPressed = []
        self.animation = Warrior.WARRIOR_FORWARD_IDLE
        self.spaceUp = True

    def update(self):
        super().update()
        self.updateState()
        return
        
    def move(self):
        if self.keysPressed[pygame.K_a]:
            self.x_vel -= WALK_ACCN

        if self.keysPressed[pygame.K_d]:
            self.x_vel += WALK_ACCN

        if self.keysPressed[pygame.K_w]:
            self.y_vel -= WALK_ACCN

        if self.keysPressed[pygame.K_s]:
            self.y_vel += WALK_ACCN

        if self.keysPressed[pygame.K_SPACE] and self.sprintResetTime == 0 and self.spaceUp:
            self.sprint(10)
            self.spaceUp = False
            
        if not self.keysPressed[pygame.K_SPACE]:
            self.spaceUp = True

        
        super().move()

    def updateState(self):
        if self.x_vel < -0.01:
            self.direction = Direction.LEFT
            self.animation = Warrior.WARRIOR_LEFT_WALKING
        if self.x_vel > 0.01:
            self.direction = Direction.RIGHT
            self.animation = Warrior.WARRIOR_RIGHT_WALKING
        if abs(self.x_vel) < 0.01:
            if self.direction == Direction.LEFT:
                self.animation = Warrior.WARRIOR_LEFT_IDLE
            elif self.direction == Direction.RIGHT:
                self.animation = Warrior.WARRIOR_RIGHT_IDLE
        if self.y_vel > 0.01:
            self.direction = Direction.FORWARD
            self.animation = Warrior.WARRIOR_FORWARD_WALKING
        if self.y_vel < -0.01:
            self.direction = Direction.BACKWARD
            self.animation = Warrior.WARRIOR_BACKWARD_WALKING
        if abs(self.y_vel) < 0.01:
            if self.direction == Direction.FORWARD:
                self.animation = Warrior.WARRIOR_FORWARD_IDLE
            elif self.direction == Direction.BACKWARD:
                self.animation = Warrior.WARRIOR_BACKWARD
        


    def render(self, screen, camera):
        xPos = self.x - camera.x
        yPos = self.y - camera.y
        
        # Render the player on the screen
        self.animation.draw(
            surface=screen,
            x=xPos,
            y=yPos
        )