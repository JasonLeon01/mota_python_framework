import pygame
from project.scripts.core.sprite import Sprite

class Surface(pygame.Surface):
    """
    画布类。

    该类继承自pygame.Surface，提供了一系列的方法，用于绘制图像。
        
    方法:

        add_sprite(sprite): 添加精灵到画布中。
        remove_sprite(sprite): 从画布中移除精灵。
        clear_sprite(): 清除画布中的精灵。
        draw_text(x, y, width, height, text, pos, colour): 在画布上绘制文本。
        clear(need_log): 清除画布。
        update(): 更新画布。
        get_color(clr): 获取颜色。
    """
    
    def __init__(self, size: tuple[int, int], pos: tuple[int, int] = (0, 0), viewport: pygame.Surface = System.default_viewport) -> None:
        """
        初始化一个画布对象。

        参数:

            size: 画布的尺寸。
            pos: 画布的位置。默认为(0, 0)。
            viewport: 绘制所在的视口，默认为System.default_viewport。
        """

        self.x: int
        """画布的x坐标"""
        
        self.y: int
        """画布的y坐标"""
        
        self.ox: int
        """画布的原点x坐标"""
        
        self.oy: int
        """画布的原点y坐标"""
        
        self.z: int
        """画布的z坐标"""
        
        self.size: tuple[int, int]
        """画布的尺寸"""
        
        self.angle: int
        """画布的旋转角度"""
        
        self.opacity: int
        """画布的透明度"""
        
        self.scale: float
        """画布的缩放比例"""
        
        self.is_visible: bool
        """画布的可见性"""
        
        self.is_centre: bool
        """画布的中心标志"""
        
        self._sprite_group: list[Sprite]
        """画布的精灵组"""
        
        pass
        
    def get_size(self) -> tuple[int, int]:
        """
        获取画布尺寸。
        
        返回:

            tuple: 画布尺寸。
        """
        pass
        
    def add_sprite(self, sprite: Sprite) -> None:
        """
        添加精灵到画布中。
        
        参数:

            sprite: 精灵对象。
        """
        pass
        
    def remove_sprite(self, sprite: Sprite) -> None:
        """
        从画布中移除精灵。
        
        参数:

            sprite: 精灵对象。
        """
        pass

    def clear_sprite(self) -> None:
        """清除画布中的精灵。"""
        pass

    def draw_text(self, x: int, y: int, width: int, height: int, text: str, pos: int = 0, colour: tuple[int, int, int, int] = (255, 255, 255, 255)) -> None:
        """
        在画布上绘制单行的文本。
        
        参数:

            x: 绘制的x坐标。
            y: 绘制的y坐标。
            width: 绘制的宽度。
            height: 绘制的高度。
            text: 绘制的文本。
            pos: 绘制的位置。0为左对齐，1为居中，2为右对齐。默认为0。
            colour: 绘制的颜色。默认为白色。
        """
        pass

    def clear(self, need_log: bool = False) -> None:
        """
        清除画布。
        
        参数:

            need_log: 是否需要记录日志。默认为False。
        """
        pass
        
    def update(self) -> None:
        """更新画布。"""
        pass
            
    def get_color(self, clr: str) -> tuple[int, int, int, int]:
        """
        获取颜色。
        
        参数:

            clr: 颜色名称。
        """
        pass