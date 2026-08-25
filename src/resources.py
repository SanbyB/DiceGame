import os.path
import pygame
from spritesheet import SpriteSheet
from animation import Animation

pygame.init()

FONT = 0
FONT = pygame.font.Font(os.path.join("Graphics", "ARCADECLASSIC.TTF"), 72)
SMALLER_FONT = pygame.font.Font(os.path.join("Graphics", "ARCADECLASSIC.TTF"), 36)
EVEN_SMALLER_FONT = pygame.font.Font(os.path.join("Graphics", "ARCADECLASSIC.TTF"), 28)

LADYBIRD = SpriteSheet(pygame.image.load(os.path.join("Graphics", "ladyBird.png")), 4, 1)
LADYBIRD_WALKING = Animation(LADYBIRD, 0, 0.2)

PLANKS = pygame.image.load(os.path.join("Graphics", "woodenPlanks.png"))