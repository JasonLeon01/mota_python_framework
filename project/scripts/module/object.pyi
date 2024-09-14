from project.scripts.core.sprite import Sprite

class Object:
    def __init__(self, sprite: Sprite, pos: tuple[int, int], interval: int, is_animating: bool) -> None:
        self.id: int
        self.name: str
        self.sprite: Sprite
        self.x: int
        self.y: int
        self.interval: int
        self.is_visible: bool
        self.is_animating: bool
        self.frame_index: int
        self.condition: list
        self.todo: list
        self.__screen_x: int
        self.__screen_y: int
        self.__is_moving: bool
    
    def update(self) -> None:
        pass

    def onFunction(self):
        pass
