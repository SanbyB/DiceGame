import pygame
import numpy as np
from entity import *
from resources import LADYBIRD_WALKING

WALK_ACCN = 0.5

class Player(Entity):
    def __init__(self):
        super().__init__("Player")
        self.width = 40
        self.height = 64
        self.keysPressed = []
        self.animation = LADYBIRD_WALKING
        self.sprintTimer = 0
        self.spaceUp = True

    def update(self):
        super().update()
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

        if self.keysPressed[pygame.K_SPACE] and self.sprintTimer == 0 and self.spaceUp:
            self.sprintTimer = 10
            self.sprint = 10
            self.spaceUp = False
            
        if self.sprintTimer == 0:
            pass            
        elif self.sprintTimer > 0:
            self.sprintTimer -= 0.1
        elif self.sprintTimer < 0:
            self.sprintTimer = 0

        if not self.keysPressed[pygame.K_SPACE]:
            self.spaceUp = True

        
        super().move()


    def render(self, screen, camera):
        # Render the player on the screen
        self.animation.draw(
            surface=screen,
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
            direction=self.direction
        )