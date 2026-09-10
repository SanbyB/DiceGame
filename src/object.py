

class Object:
    def __init__(self, pos = (0, 0)):
        self.x = pos[0]
        self.y = pos[1]
        self.width = 0
        self.height = 0
        self.animation = None
        self.scale = 1.5
        self.angle = 0

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