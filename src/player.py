import pygame
import numpy as np
from entity import *
from entities.dice import Dice
from resources import Warrior

WALK_ACCN = 0.5

class Player(Entity):
    def __init__(self):
        super().__init__("Player")

        self.keysPressed = []
        self.mousePressed = []
        self.mousePos = (0, 0)

        self.animation = Warrior.WARRIOR_FORWARD_IDLE
        self.width = self.animation.spritesheet.imageWidth * self.scale # best to move this to a function in entity.py that sets the width and height based on the animation, so that it can be called whenever the animation changes
        self.height = self.animation.spritesheet.imageHeight * self.scale
        self.stateSwitchTime = 0

        self.spaceUp = True
        self.keyUp = {"space": True, "leftClick": True, "rightClick": True}
        
        self.world = None
        self.moveable = True
        self.colliding = False
        # self.collidable = False

    def update(self):
        if self.stateSwitchTime == 0:
            pass
        elif self.stateSwitchTime > 0:
            self.stateSwitchTime -= 1
        elif self.stateSwitchTime < 0:
            self.stateSwitchTime = 0
        super().update()
        self.updateState()
        self.keyCheck()
        return
        
    def move(self):
        if self.colliding:
            super().move()
            return # don't move if colliding, will be handled by collision resolution

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
        if self.colliding:# or self.stateSwitchTime > 0:
            return
        if self.x_vel < -0.01:
            if self.direction != Direction.LEFT:
                self.stateSwitchTime = 5

            self.direction = Direction.LEFT
            self.animation = Warrior.WARRIOR_LEFT_WALKING

        if self.x_vel > 0.01:
            if self.direction != Direction.RIGHT:
                self.stateSwitchTime = 5

            self.direction = Direction.RIGHT
            self.animation = Warrior.WARRIOR_RIGHT_WALKING

        if abs(self.x_vel) < 0.01:
            if self.direction == Direction.LEFT:
                self.stateSwitchTime = 5

                self.animation = Warrior.WARRIOR_LEFT_IDLE
            elif self.direction == Direction.RIGHT:
                self.stateSwitchTime = 5

                self.animation = Warrior.WARRIOR_RIGHT_IDLE

        if abs(self.y_vel) < 0.01:
            if self.direction == Direction.FORWARD:
                self.stateSwitchTime = 5

                self.animation = Warrior.WARRIOR_FORWARD_IDLE
            elif self.direction == Direction.BACKWARD:
                self.stateSwitchTime = 5

                self.animation = Warrior.WARRIOR_BACKWARD

        elif self.y_vel > 0.01:
            if self.direction != Direction.FORWARD:
                self.stateSwitchTime = 5

            self.direction = Direction.FORWARD
            self.animation = Warrior.WARRIOR_FORWARD_WALKING
        
        elif self.y_vel < -0.01:
            if self.direction != Direction.BACKWARD:
                self.stateSwitchTime = 5

            self.direction = Direction.BACKWARD
            self.animation = Warrior.WARRIOR_BACKWARD_WALKING
    
    def keyCheck(self):
        if self.mousePressed[2] and self.keyUp["rightClick"]:
            self.keyUp["rightClick"] = False
            self.spawnDice()
        
        elif not self.mousePressed[2]:
            self.keyUp["rightClick"] = True

        if self.mousePressed[0] and self.keyUp["leftClick"]:
            self.keyUp["leftClick"] = False
            self.hitDice()
        
        elif not self.mousePressed[0]:
            self.keyUp["leftClick"] = True

    def spawnDice(self):
        dice = Dice(pos=(self.x, self.y))
        if self.world is not None:
            self.world.addEntity(dice)
        else:
            print("World is not set for player, cannot spawn dice.")
        
    def hitDice(self):
        for entity in self.world.entities:
            if isinstance(entity, Dice):
                if self.mousePos[0] >= entity.x - entity.width/2 and self.mousePos[0] <= entity.x + entity.width/2\
                   and self.mousePos[1] >= entity.y - entity.height/2 and self.mousePos[1] <= entity.y + entity.height/2:
                    entity.roll(((self.mousePos[0] - self.x)*10, (self.mousePos[1] - self.y)*10))
                    return True
        return False
        
        


    