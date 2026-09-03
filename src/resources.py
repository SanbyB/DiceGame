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
LADYBIRD_WALKING = Animation(LADYBIRD, 0, 0.1)

PLANKS = pygame.image.load(os.path.join("Graphics", "planks.png"))
PLANKS_SIZE = 75

GROUND = pygame.image.load(os.path.join("Graphics", "groundTile.png"))

class Wizard:
    WIZARD = SpriteSheet(pygame.image.load(os.path.join("Graphics", "wizard.png")), 4, 7)
    WIZARD_FORWARD = Animation(WIZARD, 0, 0)
    WIZARD_RIGHT = Animation(WIZARD, 1, 0)
    WIZARD_LEFT = Animation(WIZARD, 2, 0)
    WIZARD_BACKWARD = Animation(WIZARD, 5, 0)

    WIZARD_FORWARD_IDLE = Animation(WIZARD, 0, 0.1)
    WIZARD_RIGHT_IDLE = Animation(WIZARD, 1, 0.1)
    WIZARD_LEFT_IDLE = Animation(WIZARD, 2, 0.1)

    WIZARD_FORWARD_WALKING = Animation(WIZARD, 3, 0.1)
    WIZARD_RIGHT_WALKING = Animation(WIZARD, 4, 0.1)
    WIZARD_BACKWARD_WALKING = Animation(WIZARD, 5, 0.1)
    WIZARD_LEFT_WALKING = Animation(WIZARD, 6, 0.1)

class Warrior:
    WARRIOR_SCALE = 1
    warrior = pygame.image.load(os.path.join("Graphics", "warrior.png"))
    warrior = pygame.transform.scale(warrior, (warrior.get_width() * WARRIOR_SCALE, warrior.get_height() * WARRIOR_SCALE))
    WARRIOR = SpriteSheet(warrior, 4, 7)
    WARRIOR_FORWARD = Animation(WARRIOR, 0, 0)
    WARRIOR_RIGHT = Animation(WARRIOR, 3, 0)
    WARRIOR_LEFT = Animation(WARRIOR, 5, 0)
    WARRIOR_BACKWARD = Animation(WARRIOR, 2, 0)

    WARRIOR_FORWARD_IDLE = Animation(WARRIOR, 1, 0.1)
    WARRIOR_RIGHT_IDLE = Animation(WARRIOR, 4, 0.1)
    WARRIOR_LEFT_IDLE = Animation(WARRIOR, 6, 0.1)

    WARRIOR_FORWARD_WALKING = Animation(WARRIOR, 0, 0.1)
    WARRIOR_RIGHT_WALKING = Animation(WARRIOR, 3, 0.1)
    WARRIOR_LEFT_WALKING = Animation(WARRIOR, 5, 0.1)
    WARRIOR_BACKWARD_WALKING = Animation(WARRIOR, 2, 0.1)