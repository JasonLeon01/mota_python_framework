from project.scripts.core.sprite import Sprite

class Object:
    def __init__(self, sprite: Sprite, pos: tuple[int, int], interval: int, is_animating: bool) -> None:
        self.id: int
        """事件的ID，作为唯一的标识符"""
        self.name: str
        """事件名称"""
        self.sprite: Sprite
        """事件所有的精灵"""
        self.x: int
        """事件的地图x坐标"""
        self.y: int
        """事件的地图y坐标"""
        self.condition: list
        """事件的出现触发条件，第一个为变量，第二个为数值，当且仅当为数字型时是>=，其余则为=="""
        self.todo: list
        """事件的需要执行的序列，在触碰事件之后，将会添加到角色的todo list中"""
    
    def update(self, dst) -> None:
        pass

    def onFunction(self):
        pass
