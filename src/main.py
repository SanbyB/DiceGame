import sys
import pygame
from pygame.locals import *
from camera import Camera
from world import World
from player import Player

pygame.init()
pygame.mixer.init()

RUNNING = True
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600


class Game:
    def __init__(self):
        self.hasStarted = False
        self.hasFinished = False
        self.keysPressed = pygame.key.get_pressed()
        self.reset()

    def reset(self):
        self.cam = Camera()  
        self.world = World(self.cam)
        self.player = Player()
        self.world.player = self.player
        pass

    def update(self):
        keys = pygame.key.get_pressed()
        if not self.hasStarted:
            if keys[pygame.K_RETURN]:
                self.hasStarted = True
                print("Game started!")
            else:
                return
            
        self.player.keysPressed = keys
        self.player.update()
        # self.cam.move(game.player)
        


    def render(self, DISPLAYSURF):
        self.player.render(DISPLAYSURF, self.cam)
        # self.world.render(DISPLAYSURF, game.cam)


game = Game()


DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('gameJame')

clock = pygame.time.Clock()

while RUNNING:
    dt = clock.tick(120)
    # Clear the screen
    pygame.draw.rect(DISPLAYSURF, (0, 0, 0, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    game.update()
    game.render(DISPLAYSURF)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()
