import project.scripts.module.object

class Map:
    def __init__(self, width, height):
        self.name = ''
        self.width = width
        self.height = height
        self.tileset = None
        self.bgm = None
        self.tile = []
        self.objects = []
        
    def get_size(self):
        return self.width, self.height