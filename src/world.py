import pygame
from camera import Camera
# from resources import PLANKS, PLANKS_SIZE
from resources import GROUND

class World:
    def __init__(self, camera: Camera):
        self.camera = camera
        self.entities = []
        self.player = None
        self.background_surface = pygame.Surface((800, 600))  # Create a surface for the background

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

