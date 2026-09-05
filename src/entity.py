
import numpy as np

WALK_ACCN = 0.5
COLLIDE_ACCN = 2 * WALK_ACCN

class Direction:
    FORWARD = 0
    BACKWARD = 1
    LEFT = 2
    RIGHT = 3

class Entity:
    def __init__(self, name: str, pos=(0, 0)):
        self.name = name

        self.x = pos[0]
        self.y = pos[1]
        self.x_vel = 0
        self.y_vel = 0
        self.x_acc = 0
        self.y_acc = 0

        self.speed = 2
        self.speedDamp = 0.7
        self.sprintSpeed = 1
        self.sprintResetTime = 0

        self.direction = Direction.FORWARD

        self.width = 0
        self.height = 0
        self.animation = None
        self.scale = 1.5

        self.hp = 1
        
        # vars determine if an entity needs to be checked for collisions
        # if an entity is not moveable then it doesn't need to check collisions
        # if an entity is moveable then it needs to check collisions only when it's moving
        self.moveable = False # if an entity will never move or not
        self.collidable = True # if an entity can collide with other entities or not


    def update(self):
        self.move()
        self.animation.update()


    def move(self):
        self.speedLimit()
        self.integrate(0)
        self.dampSpeed()
        self.sprintCooldown()        

    def speedLimit(self):
        if self.x_vel ** 2 + self.y_vel ** 2 > self.speed ** 2:
            theta = np.arctan2(np.abs(self.y_vel), np.abs(self.x_vel))
            self.x_vel = np.sign(self.x_vel) * self.speed * np.cos(theta)
            self.y_vel = np.sign(self.y_vel) * self.speed * np.sin(theta)

    def integrate(self, dt):
        self.x_vel += self.x_acc
        self.y_vel += self.y_acc

        self.x += self.x_vel * self.sprintSpeed
        self.y += self.y_vel * self.sprintSpeed

    def dampSpeed(self):
        if self.x_acc == 0 and self.y_acc == 0:
            self.x_vel = self.x_vel * self.speedDamp
            self.y_vel = self.y_vel * self.speedDamp

        if self.x_vel < 0.01 and self.x_vel > -0.01:
            self.x_vel = 0

        if self.y_vel < 0.01 and self.y_vel > -0.01:
            self.y_vel = 0

        self.x_acc = 0
        self.y_acc = 0

    def sprint(self, amount):
        self.sprintSpeed = amount
        self.sprintResetTime = 10 # make configurable later

    def sprintCooldown(self):
        if self.sprintSpeed == 1:
            pass
        elif self.sprintSpeed > 1:
            self.sprintSpeed = self.sprintSpeed * 0.9
        else:
            self.sprintSpeed = 1

        if self.sprintResetTime == 0:
            pass            
        elif self.sprintResetTime > 0:
            self.sprintResetTime -= 0.1
        elif self.sprintResetTime < 0:
            self.sprintResetTime = 0

    def render(self, screen, camera):
        xPos = self.x - camera.x
        yPos = self.y - camera.y
        
        # Render the entity on the screen
        self.animation.draw(
            surface=screen,
            x=xPos,
            y=yPos,
            rotate=0,
            scale=self.scale
        )

    def checkCollide(self, other):
        if not self.collidable or not other.collidable:
            return False
        if self.x - self.width/2 < other.x + other.width/2 and \
           self.x + self.width/2 > other.x - other.width/2 and \
           self.y - self.height/2 < other.y + other.height/2 and \
           self.y + self.height/2 > other.y - other.height/2:
            #print(f"Collision detected between {self.name} and {other.name}")
            return True
        else:
            return False

    def resolveCollision(self, other): # TODO change the amount of movement in the direction that is not being collided with
        if self.x < other.x:
            self.x_acc = -COLLIDE_ACCN
            if other.moveable:
                other.x_acc = COLLIDE_ACCN
        elif self.x > other.x:
            self.x_acc = COLLIDE_ACCN
            if other.moveable:
                other.x_acc = -COLLIDE_ACCN
        if self.y < other.y:
            self.y_acc = -COLLIDE_ACCN
            if other.moveable:
                other.y_acc = COLLIDE_ACCN
        elif self.y > other.y:
            self.y_acc = COLLIDE_ACCN
            if other.moveable:
                other.y_acc = -COLLIDE_ACCN