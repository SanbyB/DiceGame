import sys
import pygame
from pygame.locals import *
from config import *
from camera import Camera
from world import World
from player import Player
from entities.slime import Slime

pygame.init()
pygame.mixer.init() # for sound fxs

RUNNING = True

class Game:
    def __init__(self):
        self.hasStarted = False
        self.hasFinished = False
        self.keysPressed = pygame.key.get_pressed()
        self.mousePos = pygame.mouse.get_pos()
        self.mousePressed = pygame.mouse.get_pressed()
        self.reset()

    def reset(self):
        self.cam = Camera()  
        self.world = World(self.cam)
        self.player = Player()
        self.slime = Slime()
        self.world.entities.append(self.slime)
        self.world.player = self.player
        self.world.camera = self.cam
        self.player.world = self.world

    def update(self):
        self.keysPressed = pygame.key.get_pressed()
        self.mousePos = pygame.mouse.get_pos()
        self.mousePos = (self.mousePos[0] + self.cam.x, self.mousePos[1] + self.cam.y)
        self.mousePressed = pygame.mouse.get_pressed()

        if not self.hasStarted:
            # if keys[pygame.K_RETURN]:
            self.hasStarted = True
            print("Game started!")
            # else:
            #     return
            
        self.player.keysPressed = self.keysPressed
        self.player.mousePos = self.mousePos
        self.player.mousePressed = self.mousePressed
        self.world.update()
        self.cam.move(self.player)
        


    def render(self, DISPLAYSURF):
        # self.player.render(DISPLAYSURF, self.cam)
        self.world.render(DISPLAYSURF)


game = Game()


DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('gameJame')

clock = pygame.time.Clock()

while RUNNING:
    dt = clock.tick(120)
    # Clear the screen
    # pygame.draw.rect(DISPLAYSURF, (0, 0, 0, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    game.update()
    game.render(DISPLAYSURF)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()
