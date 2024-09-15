import pygame
from project.scripts.core.surface import Surface
from project.scripts.core.sprite import Sprite

class ViewportManager:
    """
    视口管理类。
    
    该类提供了一系列的方法，用于管理视口和其包含的精灵和画布。
    
    属性:
    
        _viewport_dictionary: 存储视口的字典。
    """
    
    _viewport_dictionary: dict[int, Surface]
    """存储视口的字典"""

    @classmethod
    def init(cls) -> None:
        """
        初始化视口管理器。
        """
        pass

    @classmethod
    def add_viewport(cls, viewport: Surface) -> None:
        """
        添加视口。
        
        参数:
        
            viewport: 要添加的视口。
        """
        pass
    
    @classmethod
    def remove_viewport(cls, viewport: Surface) -> None:
        """
        移除视口。
        
        参数:
        
            viewport: 要移除的视口。
        """
        pass

    @classmethod
    def add_sprite(cls, sprite: Sprite, viewport: Surface = None) -> None:
        """
        添加精灵到指定视口。
        
        参数:
        
            sprite: 要添加的精灵。
            viewport: 要添加到的视口。默认为None。
        """
        pass
    
    @classmethod
    def remove_sprite(cls, sprite: Sprite, viewport: Surface = None) -> None:
        """
        从指定视口移除精灵。
        
        参数:
        
            sprite: 要移除的精灵。
            viewport: 要从中移除的视口。默认为None。
        """
        pass

    @classmethod
    def add_surface(cls, surface: Surface, viewport: Surface = None) -> None:
        """
        添加画布到指定视口。
        
        参数:
        
            surface: 要添加的画布。
            viewport: 要添加到的视口。默认为None。
        """
        pass

    @classmethod
    def remove_surface(cls, surface: Surface, viewport: Surface = None) -> None:
        """
        从指定视口移除画布。
        
        参数:
        
            surface: 要移除的画布。
            viewport: 要从中移除的视口。默认为None。
        """
        pass

    @classmethod
    def update(cls) -> None:
        """更新所有视口。"""
        pass