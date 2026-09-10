import random
import sys
import pygame
from pygame.locals import *
from config import *
from graphics.camera import Camera
from world import World
from player import Player
from entities.slime import Slime
from entities.spider import Spider
from entities.wall import Wall
from objects.foliage import Bush, Rock, SpruceTree, Tree, Flowers
import time

  

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
        self.world.camera = self.cam

        self.player = Player(self.world)

        self.world.addPlayer(self.player)

        self.world.addEntity(Slime(self.world, pos=(1000, 0)))
        self.world.addEntity(Spider(self.world, pos=(-100, 0)))

        self.world.addEntity(Wall(self.world, pos=(-1,-3)))
        self.world.addEntity(Wall(self.world, pos=(-1,-2)))


        self.world.addObject(Bush(pos=(200, 200)))
        self.world.addObject(Tree(pos=(100, 300)))
        self.world.addObject(SpruceTree(pos=(0, 0)))
        self.world.addSTObject(Rock(pos=(100, 100)))
        
        self.world.addObject(Flowers(pos=(300, 200), speed = random.uniform(0.005, 0.05)))
        self.world.addObject(Flowers(pos=(-60, 20), speed = random.uniform(0.005, 0.05)))
        self.world.addObject(Flowers(pos=(30, -80), speed = random.uniform(0.005, 0.05)))


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
    # startTime = time.time() # Record when the loop was started    
    dt = clock.tick(60)
    # Clear the screen
    # pygame.draw.rect(DISPLAYSURF, (0, 0, 0, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    game.update()
    game.render(DISPLAYSURF)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Calculate how long did it take the loop to run.
    # HowLong = time.time() - startTime
    # print(HowLong)

    
    pygame.display.update()
