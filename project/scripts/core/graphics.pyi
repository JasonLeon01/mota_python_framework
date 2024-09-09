from project.scripts.core.sprite import Sprite
from project.scripts.core.surface import Surface
from project.scripts.core.window import Window
from project.scripts.core.animation import Animation
import pygame

class Graphics:
    """
    图形系统类。
    方法:
    
        init(): 初始化图形系统。
        add_window(window): 添加一个窗口。
        remove_window(window): 移除一个窗口。
        add_sprite(sprite): 添加一个精灵。
        remove_sprite(sprite): 移除一个精灵。
        add_surface(surface): 添加一个画布。
        remove_surface(surface): 移除一个画布。
        add_animation(animation): 添加一个动画。
        remove_animation(animation): 移除一个动画。
        frame_count: 获取帧计数。
        update: 更新图形系统。
        debug_info(draw_surface): 输出调试信息。
        freeze: 冻结画面。
        transition(time): 过渡效果。
    """
    
    __sprite_group: list[Sprite]
    """精灵组"""
    
    __surface_group: list[Surface]
    """画布组"""
    
    __window_group: list[Window]
    """窗口组"""
    
    __animation_group: list[Animation]
    """动画组"""
    
    __frame_count: int
    """帧计数"""
    
    __freeze_Image: pygame.Surface
    """冻结图像"""
    
    __last_frame_time: int
    """上一帧时间"""
    
    __total_time: int
    """总时间"""

    @classmethod
    def init(cls) -> None:
        """
        初始化图形系统。
        """
        pass
    
    @classmethod
    def add_window(cls, window: Window) -> None:
        """
        添加一个窗口。
        
        参数:
            window: 要添加的窗口。
        """
        pass

    @classmethod
    def remove_window(cls, window: Window) -> None:
        """
        移除一个窗口。
        
        参数:
            window: 要移除的窗口。
        """
        pass

    @classmethod
    def add_sprite(cls, sprite: Sprite) -> None:
        """
        添加一个精灵。
        
        参数:
            sprite: 要添加的精灵。
        """
        pass
        
    @classmethod
    def remove_sprite(cls, sprite: Sprite) -> None:
        """
        移除一个精灵。
        
        参数:
            sprite: 要移除的精灵。
        """
        pass
    
    @classmethod
    def add_surface(cls, surface: Surface) -> None:
        """
        添加一个画布。
        
        参数:
            surface: 要添加的画布。
        """
        pass
    
    @classmethod
    def remove_surface(cls, surface: Surface) -> None:
        """
        移除一个画布。
        
        参数:
            surface: 要移除的画布。
        """
        pass

    @classmethod
    def add_animation(cls, animation: Animation) -> None:
        """
        添加一个动画。
        
        参数:
            animation: 要添加的动画。
        """
        pass

    @classmethod
    def remove_animation(cls, animation: Animation) -> None:
        """
        移除一个动画。
        
        参数:
            animation: 要移除的动画。
        """
        pass

    @classmethod
    def frame_count(cls) -> int:
        """
        获取帧计数。
        
        返回:
            int: 帧计数。
        """
        pass
        
    @classmethod
    def update(cls) -> None:
        """
        更新图形系统。
        """
        pass

    @classmethod
    def debug_info(cls, draw_surface: pygame.Surface) -> None:
        """
        输出调试信息。
        """
        pass

    @classmethod
    def freeze(cls) -> None:
        """
        冻结画面。
        """
        pass

    @classmethod
    def transition(cls, time: int = 20) -> None:
        """
        过渡效果。
        """
        pass