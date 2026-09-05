import pygame
from camera import Camera
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from resources import GROUND, TREE

class World:
    def __init__(self, camera: Camera):
        self.camera = camera
        self.entities = []
        self.player = None
        self.background_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create a surface for the background

    def update(self):
        self.player.colliding = False  # Reset the colliding state of the player at the start of each update
        # Update all entities in the world
        for entity in self.entities:
            if entity.hp <= 0:
                self.entities.remove(entity)

            if entity.collidable:
                if self.player.checkCollide(entity):
                    self.player.x_vel -= 0.1
                    self.player.resolveCollision(entity)
                    # self.camera.shake(0.2)
                    self.player.colliding = True
                    # print(f"Collision detected between Player and {entity.name}")

            if entity.collidable and entity.moveable:# and (entity.x_vel != 0 or entity.y_vel != 0):
                for other_entity in self.entities:
                    if other_entity != entity and other_entity.collidable:
                        if entity.checkCollide(other_entity):
                            entity.resolveCollision(other_entity)

            entity.update()

        if self.player: 
            self.player.update()

    def render(self, surface):
        # Render the background first
        self.backgroundRender()
        surface.blit(self.background_surface, (0, 0))  # Blit the background surface onto the main surface

        # Render all entities in the world
        for entity in self.entities:
            entity.render(surface, self.camera)

        self.player.render(surface, self.camera)

    def backgroundRender(self):
        # Render the background here
        for x in range(-5, 5):
            for y in range(-5, 5):
                scaledImage = pygame.transform.scale(GROUND, (64, 64))

                self.background_surface.blit(scaledImage, (x * 64 - self.camera.x, y * 64 - self.camera.y))

    def addEntity(self, entity):
        self.entities.append(entity)