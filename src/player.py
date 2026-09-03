import pygame
import numpy as np
from entity import *
from entities.dice import Dice
from resources import Warrior

WALK_ACCN = 0.5
PLAYER_SIZE = 80

class Player(Entity):
    def __init__(self):
        super().__init__("Player")
        self.width = PLAYER_SIZE
        self.height = PLAYER_SIZE

        self.keysPressed = []
        self.mousePressed = []
        self.mousePos = (0, 0)

        self.animation = Warrior.WARRIOR_FORWARD_IDLE
        
        self.spaceUp = True
        self.keyUp = {"space": True, "leftClick": True}
        
        self.world = None

    def update(self):
        super().update()
        self.updateState()
        self.keyCheck()
        return
        
    def move(self):
        self.x_acc = 0
        self.y_acc = 0

        if self.keysPressed[pygame.K_a]:
            self.x_acc = -WALK_ACCN

        if self.keysPressed[pygame.K_d]:
            self.x_acc = WALK_ACCN

        if self.keysPressed[pygame.K_w]:
            self.y_acc = -WALK_ACCN

        if self.keysPressed[pygame.K_s]:
            self.y_acc = WALK_ACCN

        if self.keysPressed[pygame.K_SPACE] and self.sprintResetTime == 0 and self.keyUp["space"]:
            self.sprint(10) # make configurable later
            self.keyUp["space"] = False
            
        if not self.keysPressed[pygame.K_SPACE]:
            self.keyUp["space"] = True

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
        if abs(self.y_vel) < 0.01:
            if self.direction == Direction.FORWARD:
                self.animation = Warrior.WARRIOR_FORWARD_IDLE
            elif self.direction == Direction.BACKWARD:
                self.animation = Warrior.WARRIOR_BACKWARD
        elif self.y_vel > 0.01:
            self.direction = Direction.FORWARD
            self.animation = Warrior.WARRIOR_FORWARD_WALKING
        elif self.y_vel < -0.01:
            self.direction = Direction.BACKWARD
            self.animation = Warrior.WARRIOR_BACKWARD_WALKING
    
    def keyCheck(self):
        if self.mousePressed[0] and self.keyUp["leftClick"]:
            self.keyUp["leftClick"] = False
            self.spawnDice()
        
        elif not self.mousePressed[0]:
            self.keyUp["leftClick"] = True

    def spawnDice(self):
        dice = Dice((self.x, self.y))
        if self.world is not None:
            self.world.addEntity(dice)
        else:
            print("World is not set for player, cannot spawn dice.")
        
        


    