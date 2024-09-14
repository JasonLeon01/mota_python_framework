from project.scripts.core.sprite import Sprite

class Object:
    def __init__(self, sprite = None, pos = (0, 0), interval = 30, is_animating = False):
        self.id = 0
        self.name = ''
        self.sprite = sprite
        self.x, self.y = pos
        self.interval = interval
        self.is_visible = True
        self.is_animating = is_animating
        self.frame_index = self.sprite.frame_index
        self.condition = []
        self.todo = []
        
        self.__screen_x = self.x * 32
        self.__screen_y = self.y * 32
        self.__is_moving = False
    
    def update(self):
        if not self.is_visible:
            return
        
        self.frame_index = self.sprite.frame_index
        self.sprite.is_animating = self.is_animating
        self.sprite.update()
        
        if self.__screen_x != self.x * 32 or self.__screen_y != self.y * 32:
            self.__is_moving = True
        else:
            self.__is_moving = False
            
        if self.__screen_x < self.x * 32:
            self.__screen_x += 4
        elif self.__screen_x > self.x * 32:
            self.__screen_x -= 4
        if self.__screen_y < self.y * 32:
            self.__screen_y += 4
        elif self.__screen_y > self.y * 32:
            self.__screen_y -= 4
            
        if not self.__is_moving:
            self.onFunction()

    def onFunction(self):
        pass
