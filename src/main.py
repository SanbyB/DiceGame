import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

RUNNING = True
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
class Game:
    def __init__(self):
        self.hasStarted = False
        self.hasFinished = False
        self.reset()

    def reset(self):
        # self.cam = Camera()  
        # self.world = World(self.cam)
        # self.player = Player(self.world)
        # self.world.player = self.player
        pass

    def update(self):

        keys = pygame.key.get_pressed()
        if not self.hasStarted:
            if keys[pygame.K_RETURN]:
                self.hasStarted = True
            else:
                return
            
        # self.player.update()
        # self.cam.move(game.player)
        


    def render(self, DISPLAYSURF):
        # self.world.render(DISPLAYSURF, game.cam)
        pass


game = Game()


DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('gameJame')

clock = pygame.time.Clock()

while RUNNING:
    dt = clock.tick(60)
    # Clear the screen
    pygame.draw.rect(DISPLAYSURF, (0, 0, 0, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    # game.update()
    # game.render(DISPLAYSURF)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()
