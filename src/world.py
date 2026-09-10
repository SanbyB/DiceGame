import pygame
from graphics.camera import Camera
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from graphics.resources import GROUND
from entities.dice import Dice

class World:
    def __init__(self, camera: Camera):
        self.camera = camera
        
        self.background_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create a surface for the background

        self.dice = []
        self.entities = []
        self.player = None
        self.objects = []  # List to hold all objects in the world
        self.seeThroughObjects = []


    def update(self):
        self.player.colliding = False  # Reset the colliding state of each player at the start of each update
        # Handle collisions
        objects = self.entities + self.dice
        for entity in objects:
            # player collides with everything but dice
            if entity.collidable and not isinstance(entity, Dice):
                if self.player.checkCollide(entity):
                    self.player.resolveCollision(entity)
                    # self.camera.shake(0.2)
                    self.player.colliding = True
                    # print(f"Collision detected between Player and {entity.name}")
            
            # all other collisions not player
            if entity.collidable and entity.moveable and (entity.x_vel != 0 or entity.y_vel != 0):
                for other_entity in objects:
                    if other_entity != entity and other_entity.collidable:
                        if entity.checkCollide(other_entity):
                            entity.resolveCollision(other_entity)

        objects.append(self.player)
        for obj in self.seeThroughObjects:
            obj.animation = obj.state["default"]
            for object in objects:
                if obj.checkCollide(object, cover=True):
                    obj.animation = obj.state["seeThrough"]

        # update everything
        for object in self.objects:
            object.update()

    def render(self, surface):
        # Render the background first
        self.backgroundRender()
        surface.blit(self.background_surface, (0, 0))  # Blit the background surface onto the main surface

        ## TODO if there is an object behind another the front object alpha should be reduced to make it look like the player is behind the object
        self.objects.sort(key=lambda obj: obj.y + obj.height/2)  # Sort objects by their y-coordinate for proper rendering order
        # Render all objects in the world
        for object in self.objects:
            object.render(surface, self.camera)


    def backgroundRender(self):
        # Render the background here
        for x in range(-5, 5):
            for y in range(-5, 5):
                scaledImage = pygame.transform.scale(GROUND, (64, 64))

                self.background_surface.blit(scaledImage, (x * 64 - self.camera.x, y * 64 - self.camera.y))

    def addEntity(self, entity):
        self.entities.append(entity)
        self.objects.append(entity)

    def removeEntity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)
        if entity in self.objects:
            self.objects.remove(entity)

    def addObject(self, obj):
        self.objects.append(obj)

    def removeObject(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)

    def addDice(self, dice):
        dice.player = self.player
        self.dice.append(dice)
        self.objects.append(dice)

    def removeDice(self, dice):
        if dice in self.dice:
            self.dice.remove(dice)
        if dice in self.objects:
            self.objects.remove(dice)

    def addSTObject(self, obj):
            self.seeThroughObjects.append(obj)
            self.objects.append(obj)
    
    def removeSTObject(self, obj):
        if obj in self.seeThroughObjects:
            self.seeThroughObjects.remove(obj)
        if obj in self.objects:
            self.objects.remove(obj)

    def addPlayer(self, player):
        self.player = player
        self.objects.append(player)