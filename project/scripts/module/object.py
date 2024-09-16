class Object:
    def __init__(self, sprite = None, pos = (0, 0), interval = 30, is_animating = False):
        self.id = 0
        self.name = ''
        self.sprite = sprite
        self.x, self.y = pos
        self.sprite.x = self.x * 32
        self.sprite.y = self.y * 32
        self.sprite.interval = interval
        self.sprite.is_animating = is_animating
        self.condition = []
        self.todo = []
        
        self.__is_moving = False
    
    def update(self, dst):
        if not self.sprite.is_visible:
            return
        
        self.sprite.update(dst)
        
        if self.sprite.x != self.x * 32 or self.sprite.y != self.y * 32:
            self.__is_moving = True
        else:
            self.__is_moving = False
            
        if self.sprite.x < self.x * 32:
            self.sprite.x += 4
        elif self.sprite.x > self.x * 32:
            self.sprite.x -= 4
        if self.sprite.y < self.y * 32:
            self.sprite.y += 4
        elif self.sprite.y > self.y * 32:
            self.sprite.y -= 4
            
        if not self.__is_moving:
            self.onFunction()

    def onFunction(self):
        pass
