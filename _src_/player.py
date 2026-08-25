import pygame
import numpy as np
from resources import PLAYER_BREATHING, PLAYER_WALKING, audio
from resources import LADYBIRD_WALKING, LADYBIRD_BREATHING
from physics import Physics
from maps.tilemap import TILE_MAP_WIDTH, TILE_SIZE
from config import SCREEN_WIDTH, SCREEN_HEIGHT
# from equipment import Equipment

WALK_ACCN = 1.5
WALK_SPEED = 5
JUMP_POWER = 12

class Player(Physics):
    def __init__(self, world):
        super().__init__(
            (TILE_MAP_WIDTH / 2) * TILE_SIZE,
            (TILE_MAP_WIDTH / 2) * TILE_SIZE,
            40,
            64
        )
        # self.onPlayerDead = onPlayerDead
        self.invtry = []
        self.world = world
        self.isFlipped = False
        self.hitCount = 0
        # self.equipment = Equipment(world, self)
        self.stepFreq = 0


    def update(self):
        super().update()
        self.move()
        # self.equipment.update()
        LADYBIRD_WALKING.update()
        LADYBIRD_BREATHING.update()



    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x_vel -= WALK_ACCN

        if keys[pygame.K_d]:
            self.x_vel += WALK_ACCN

        if keys[pygame.K_w]:
            self.y_vel -= WALK_ACCN

        if keys[pygame.K_s]:
            self.y_vel += WALK_ACCN

        if self.x_vel ** 2 + self.y_vel ** 2 > WALK_SPEED ** 2:
            theta = np.arctan2(np.abs(self.y_vel), np.abs(self.x_vel))
            self.x_vel = np.sign(self.x_vel) * WALK_SPEED * np.cos(theta)
            self.y_vel = np.sign(self.y_vel) * WALK_SPEED * np.sin(theta)

        self.x_vel = self.x_vel * 0.8
        self.y_vel = self.y_vel * 0.8


    def playMove(self):
        if self.stepFreq == 0:
            audio.onStep()
            self.stepFreq = 20
        else:
            self.stepFreq -= 1



    def render(self, screen, camera):
        imageInflate = 12
        xPos = self.x - camera.x - imageInflate
        yPos = self.y - camera.y

        isWalking = abs(self.x_vel) + abs(self.y_vel) > 0.05

        if self.x_vel < 0:
            self.isFlipped = True

        if self.x_vel > 0:
            self.isFlipped = False

        width = self.width + imageInflate * 2

        if self.hitCount > 0:
            self.hitCount -= 1
        elif isWalking:
            self.playMove()
            LADYBIRD_WALKING.draw(screen, xPos, yPos, width, self.height, self.isFlipped)
        else: 
            LADYBIRD_BREATHING.draw(screen, xPos, yPos, width, self.height, self.isFlipped)










