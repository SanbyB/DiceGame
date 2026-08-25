import pygame

class Physics:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.x_vel = 0
        self.y_vel = 0

    def update(self):
        self.resolveCollisions()
        self.applyVelocity()


    def resolveCollisions(self):
        
        # Does right side collide
        if self.x_vel > 0 and self.world.tileMap.doesCollide(self.x + self.x_vel + self.width, self.y):
            self.x_vel = 0
        if self.x_vel > 0 and self.world.tileMap.doesCollide(self.x + self.x_vel + self.width, self.y + self.height):
            self.x_vel = 0

        # Does left side collide
        if self.x_vel < 0 and self.world.tileMap.doesCollide(self.x + self.x_vel, self.y):
            self.x_vel = 0
        if self.x_vel < 0 and self.world.tileMap.doesCollide(self.x + self.x_vel, self.y + self.height):
            self.x_vel = 0
        
        
        BOTTOM_FRIC = 0.2
        # Does bottom collide
        if self.y_vel > 0 and self.world.tileMap.doesCollide(self.x, self.y + self.height + self.y_vel):
            # if self.y_vel < 2.5:
            self.y_vel = 0
            # self.y_vel = -self.y_vel * BOTTOM_FRIC
        if self.y_vel > 0 and self.world.tileMap.doesCollide(self.x + self.width, self.y + self.height + self.y_vel):
            # if self.y_vel < 2.5:
            self.y_vel = 0
            # self.y_vel = -self.y_vel * BOTTOM_FRIC

        # Does top collide
        if self.y_vel < 0 and self.world.tileMap.doesCollide(self.x, self.y + self.y_vel):
            self.y_vel = 0 #-self.y_vel * 0.08
        if self.y_vel < 0 and self.world.tileMap.doesCollide(self.x + self.width, self.y + self.y_vel):
            self.y_vel = 0 #-self.y_vel * 0.08

        return

    def applyVelocity(self):
        self.x += self.x_vel
        self.y += self.y_vel
        # The x_vel friction is different for the player and entity, as the entity doesn't move enough to have as much friction
        # self.y_vel = self.y_vel * 0.97


        

