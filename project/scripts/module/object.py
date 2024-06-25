import project.scripts.core.sprite

class Object(project.scripts.core.sprite.Sprite):
    def __init__(self, frames = None):
        super().__init__(frames)
        self.id = 0
        self.name = ''
        self.x = 0
        self.y = 0
        self.z = 0
        self.scale = 1.0
        self.opacity = 255
        self.condition = [0, 0, 0]
        self.move = False
        self.todo = {}
    
    def dispose(self):
        self.__graphics.remove_surface(self)
        super().dispose()
    
    def __del__(self):
        self.dispose()