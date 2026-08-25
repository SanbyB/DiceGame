from camera import Camera


class World:
    def __init__(self, camera: Camera):
        self.camera = camera
        self.entities = []
        self.player = None