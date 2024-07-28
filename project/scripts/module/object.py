from project.scripts.core.sprite import Sprite

class Object:
    def __init__(self, sprite: Sprite = None, pos = (0, 0), interval = 30, is_animating = False):
        self.id = 0
        self.sprite = sprite
        self.x, self.y = pos
        self.interval = interval
        self.is_animating = is_animating
        
        self.__screen_x = self.x * 32
        self.__screen_y = self.y * 32
        self.__is_moving = False
    
    def update(self, dst):
        if not self.is_visible:
            return
        
        self.sprite.is_animating = self.is_animating
        self.sprite.update(dst)
        
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

    def dispose(self):
        self._frames = None
        self.image = None