import pygame

class Animation:
    """
    表示一个动画对象。

    方法:
    
        __init__(frames, voices): 初始化一个 Animation 对象。
        frame(): 生成一个动画帧。
        update(): 通过将当前帧绘制到目标画布来更新动画。
        dispose(): 释放动画资源。
    """

    def __init__(self, frames, voices: str, viewport: pygame.Surface):
        """初始化一个 Animation 对象。"""

        self.x: int
        """动画的 x 坐标"""
        self.y: int
        """动画的 y 坐标"""
        self.loop: bool
        """指示动画是否应循环"""
        self.viewport: pygame.Surface
        """显示在的视口"""
        self.__frame_count: int
        """当前帧计数"""
        self.__voice_count: int
        """当前声音计数"""

        pass

    def frame(self) -> pygame.Surface:
        """
        生成一个动画帧。

        返回:

            pygame.Surface: 生成的动画帧。
        """
        pass

    def update(self):
        """
        通过将当前帧绘制到目标画布来更新动画。

        参数:

            dst (pygame.Surface): 将帧绘制到的目标画布。默认是 System.default_viewport。
        """
        pass

    def has_reach_end(self) -> bool:
        """
        判断当前动画是否播放到结尾。

        返回:
        
            bool: 判断结果。
        """
        pass

    def reset(self):
        """重置当前动画，用于循环动画"""
        pass
