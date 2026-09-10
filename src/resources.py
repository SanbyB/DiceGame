import os.path
import pygame
from spritesheet import SpriteSheet
from animation import Animation

pygame.init()

FONT = 0
FONT = pygame.font.Font(os.path.join("Graphics", "ARCADECLASSIC.TTF"), 72)
SMALLER_FONT = pygame.font.Font(os.path.join("Graphics", "ARCADECLASSIC.TTF"), 36)
EVEN_SMALLER_FONT = pygame.font.Font(os.path.join("Graphics", "ARCADECLASSIC.TTF"), 28)

GROUND = pygame.image.load(os.path.join("Graphics", "groundTile.png"))

WALL = pygame.image.load(os.path.join("Graphics", "wallTile.png"))

class Foliage:
    TREE = SpriteSheet(pygame.image.load(os.path.join("Graphics", "tree.png")), 4, 1)
    TREE = Animation(TREE, 0, 0.02)

    SPRUCE_TREE = SpriteSheet(pygame.image.load(os.path.join("Graphics", "spruceTree.png")), 1, 1)
    SPRUCE_TREE = Animation(SPRUCE_TREE, 0, 0)

    ROCK = SpriteSheet(pygame.image.load(os.path.join("Graphics", "rock.png")), 1, 1)
    ROCK = Animation(ROCK, 0, 0)

    BUSH = SpriteSheet(pygame.image.load(os.path.join("Graphics", "bush.png")), 4, 1)
    BUSH = Animation(BUSH, 0, 0.05)

    FLOWERS = SpriteSheet(pygame.image.load(os.path.join("Graphics", "flowers.png")), 8, 1)

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
    warrior = pygame.image.load(os.path.join("Graphics", "warriorDebug.png"))
    WARRIOR = SpriteSheet(warrior, 4, 7)
    WARRIOR_FORWARD = Animation(WARRIOR, 0, 0)
    WARRIOR_RIGHT = Animation(WARRIOR, 3, 0)
    WARRIOR_LEFT = Animation(WARRIOR, 5, 0)
    WARRIOR_BACKWARD = Animation(WARRIOR, 2, 0)

    WARRIOR_FORWARD_IDLE = Animation(WARRIOR, 1, 0.05)
    WARRIOR_RIGHT_IDLE = Animation(WARRIOR, 4, 0.05)
    WARRIOR_LEFT_IDLE = Animation(WARRIOR, 6, 0.05)

    WARRIOR_FORWARD_WALKING = Animation(WARRIOR, 0, 0.1)
    WARRIOR_RIGHT_WALKING = Animation(WARRIOR, 3, 0.1)
    WARRIOR_LEFT_WALKING = Animation(WARRIOR, 5, 0.1)
    WARRIOR_BACKWARD_WALKING = Animation(WARRIOR, 2, 0.1)

class SlimeSprite:
    SLIME = pygame.image.load(os.path.join("Graphics", "slime.png"))
    SLIME_SPRITESHEET = SpriteSheet(SLIME, 6, 1)
    SLIME_IDLE = Animation(SLIME_SPRITESHEET, 0, 0.1)

class SpiderSprite:
    SPIDER = pygame.image.load(os.path.join("Graphics", "spider.png"))
    SPIDER_SPRITESHEET = SpriteSheet(SPIDER, 4, 2)
    SPIDER_IDLE = Animation(SPIDER_SPRITESHEET, 1, 0.1)
    SPIDER_WALKING = Animation(SPIDER_SPRITESHEET, 0, 0.1)

class DiceSprite:
    DICE = pygame.image.load(os.path.join("Graphics", "dice.png"))
    DICE_SPRITESHEET = SpriteSheet(DICE, 4, 6)
    DICE_1 = Animation(DICE_SPRITESHEET, 0, 0)
    DICE_2 = Animation(DICE_SPRITESHEET, 1, 0)
    DICE_3 = Animation(DICE_SPRITESHEET, 2, 0)
    DICE_4 = Animation(DICE_SPRITESHEET, 3, 0)
    DICE_5 = Animation(DICE_SPRITESHEET, 4, 0)
    DICE_6 = Animation(DICE_SPRITESHEET, 5, 0)

    DICE_1_IN_RANGE = Animation(DICE_SPRITESHEET, 0, 0.07)
    DICE_2_IN_RANGE = Animation(DICE_SPRITESHEET, 1, 0.07)
    DICE_3_IN_RANGE = Animation(DICE_SPRITESHEET, 2, 0.07)
    DICE_4_IN_RANGE = Animation(DICE_SPRITESHEET, 3, 0.07)
    DICE_5_IN_RANGE = Animation(DICE_SPRITESHEET, 4, 0.07)
    DICE_6_IN_RANGE = Animation(DICE_SPRITESHEET, 5, 0.07)