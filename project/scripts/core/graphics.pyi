from project.scripts.core.sprite import Sprite
from project.scripts.core.surface import Surface
from project.scripts.core.window import Window
from project.scripts.core.animation import Animation
import pygame

class Graphics:
    """
    图形系统类。
    """
    
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