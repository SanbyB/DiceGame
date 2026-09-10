

class Object:
    def __init__(self, pos = (0, 0)):
        self.x = pos[0]
        self.y = pos[1]
        self.width = 0
        self.height = 0
        self.animation = None
        self.scale = 1.5
        self.angle = 0

        self.collideable = False

    def update(self):
        if self.animation is not None:
            self.animation.update()

    def render(self, screen, camera):
            xPos = self.x - camera.x
            yPos = self.y - camera.y
            
            # Render the entity on the screen
            self.animation.draw(
                surface=screen,
                x=xPos,
                y=yPos,
                rotate=self.angle,
                scale=self.scale
            )

    def checkCollide(self, other, cover=False):
        if not self.collidable or not other.collidable:
            return False
        if cover:
            # print(self.x - self.width/2 > other.x - other.width/2, \
            # self.x + self.width/2 < other.x + other.width/2, \
            # self.y - self.height/2 > other.y - other.height/2, \
            # self.y + self.height/2 < other.y + other.height/2)
            # if other.y < self.y:
            #     return False
            if self.x - self.width/2 < other.x and \
            self.x + self.width/2 > other.x and \
            self.y - self.height/2 < other.y and \
            self.y > other.y:
                return True
        else:
            if self.x - self.width/2 < other.x + other.width/2 and \
            self.x + self.width/2 > other.x - other.width/2 and \
            self.y - self.height/2 < other.y + other.height/2 and \
            self.y + self.height/2 > other.y - other.height/2:
                #print(f"Collision detected between {self.name} and {other.name}")
                return True
        return False