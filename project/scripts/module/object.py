from project.scripts.core.graphics import Graphics
from project.scripts.core.sprite import Sprite
from project.scripts.core.system import System

class Object(Sprite):
    def __init__(self, frames = None):
        super().__init__(frames)
        self.id = 0
        self.name = ''
        self.map_x = 0
        self.map_y = 0
        self.interval = 30
        self.condition = ['', 0]
        self.move = False
        self.exist = True
        self.todo = {}
    
    def update(self, dst):
        self.x = self.map_x * 32
        self.y = self.map_y * 32
        if not self.exist or System.get_variables(self.condition[0]) < self.condition[1]:
            self.is_visible = False
        else:
            self.is_visible = True
        super().update(dst)

    def dispose(self):
        self._frames = None
        self.image = None