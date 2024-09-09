from typing import List, Union
import pygame

class Sprite(pygame.sprite.Sprite):
    """
    精灵类。

    该类继承自pygame.sprite.Sprite，用于在屏幕上绘制和更新精灵对象。
            
    方法:

        __init__(frames, pos, viewport): 初始化精灵对象。
        __process_frames(frames): 处理帧数据。
        set_frames(frames): 设置精灵的帧数据。
        update(): 更新精灵的状态和图像。
    """
    

    def __init__(self, frames: Union[List[pygame.Surface], pygame.Surface] = None, pos: tuple[int, int] = (0, 0), viewport: pygame.Surface = System.default_viewport) -> None:
        """
        初始化精灵对象。
        
        参数:

            frames: 精灵的帧数据，可以是一个Surface对象或Surface对象的列表。
            pos: 精灵的初始位置，默认为(0, 0)。
            viewport: 精灵的视口，默认为System.default_viewport。
        """

        self.x: int
        """精灵的 x 坐标"""
        
        self.y: int
        """精灵的 y 坐标"""
        
        self.z: int
        """精灵的 z 坐标"""
        
        self.angle: int
        """精灵的旋转角度"""
        
        self.opacity: int
        """精灵的透明度"""
        
        self.scale: float
        """精灵的缩放比例"""
        
        self.is_visible: bool
        """精灵是否可见"""
        
        self.is_animating: bool
        """精灵是否正在动画"""
        
        self.is_centre: bool
        """精灵是否以中心点为基准"""
        
        self.frame_index: int
        """当前帧的索引"""
        
        self.interval: int
        """帧动画的间隔"""
        
        self.viewport: pygame.Surface
        """精灵的视口"""
        
        self._frames: list[pygame.Surface]
        """精灵的帧列表"""
        
        self._frame_count: int
        """当前帧计数"""

        pass
        
    def __process_frames(self, frames: Union[List[pygame.Surface], pygame.Surface]) -> list[pygame.Surface]:
        """
        处理帧数据。
        
        参数:

            frames: 精灵的帧数据，可以是一个Surface对象或Surface对象的列表。
        
        返回:

            list[pygame.Surface]: 处理后的帧列表。
        """
        pass
        
    def set_frames(self, frames: Union[List[pygame.Surface], pygame.Surface]) -> None:
        """
        设置精灵的帧数据。
        
        参数:

            frames: 精灵的帧数据，可以是一个Surface对象或Surface对象的列表。
        """
        pass
    
    def update(self) -> None:
        """更新精灵的状态和图像。"""
        pass