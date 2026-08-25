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
LADYBIRD_BREATHING = Animation(LADYBIRD, 0, 0.2)

PLANKS = pygame.image.load(os.path.join("Graphics", "woodenPlanks.png"))


PLAYER_SHEET = SpriteSheet(pygame.image.load(os.path.join("Graphics", "miner.png")), 8, 5)
PLAYER_BREATHING = Animation(PLAYER_SHEET, 0, 0.1)
PLAYER_WALKING = Animation(PLAYER_SHEET, 1, 0.2)

BACKGROUND_VOLUME = 0
MAIN_VOLUME = 0.1

SOUND_BIP = pygame.mixer.Sound(os.path.join("Audio", "bip.ogg"))
SOUND_BIP.set_volume(MAIN_VOLUME)

SOUND_SMOT = pygame.mixer.Sound(os.path.join("Audio", "smot.ogg"))
SOUND_SMOT.set_volume(MAIN_VOLUME)

SOUND_FOOTSTEP = pygame.mixer.Sound(os.path.join("Audio", "footstep.ogg"))
SOUND_FOOTSTEP.set_volume(MAIN_VOLUME)

SOUND_HIT = pygame.mixer.Sound(os.path.join("Audio", "bleurf.ogg"))
SOUND_HIT.set_volume(MAIN_VOLUME)

SOUND_HIT2 = pygame.mixer.Sound(os.path.join("Audio", "hit.ogg"))
SOUND_HIT2.set_volume(MAIN_VOLUME)

SOUND_HIT3 = pygame.mixer.Sound(os.path.join("Audio", "hit2.ogg"))
SOUND_HIT3.set_volume(MAIN_VOLUME)

SOUND_HIT4 = pygame.mixer.Sound(os.path.join("Audio", "hit3.ogg"))
SOUND_HIT4.set_volume(MAIN_VOLUME)

SOUND_POINT = pygame.mixer.Sound(os.path.join("Audio", "point.ogg"))
SOUND_POINT.set_volume(MAIN_VOLUME)


class Audio():
    def playMusic(self):
        return;
        # pygame.mixer.music.load(os.path.join("Audio", "background2.ogg")) 
        # pygame.mixer.music.set_volume(BACKGROUND_VOLUME)     
        # pygame.mixer.music.play(-1,0.0)  

    def onRockHit(self):
        SOUND_SMOT.play()
    
    def onRockBreak(self):
        SOUND_SMOT.play()

    def onOreHit(self):
        SOUND_SMOT.play()
    
    def onOreBreak(self):
        SOUND_SMOT.play()
        SOUND_POINT.play()
        
    def onSlimeHit(self):
        SOUND_HIT2.play()

    def onSlimeDead(self):
        SOUND_HIT.play()
    
    def onPlayerHit(self):
        SOUND_HIT2.play()

    def onPlayerDead(self):
        SOUND_HIT.play()

    def onBuy(self):
        SOUND_POINT.play()

    def onStep(self):
        SOUND_FOOTSTEP.play()

    def onJump(self):
        SOUND_FOOTSTEP.play()
    
    def onDrop(self):
        SOUND_FOOTSTEP.play()



audio = Audio()

