import pygame
from project.scripts.core.surface import Surface

class Window(Surface):
    """
    窗口类。
    
    该类继承自Surface类，用于在画布上绘制窗口。

    方法:

        set_rect(x, y, width, height): 设置选择矩形。
        update(): 更新窗口对象。
        __presave_corner(area_rects): 预存窗口四角资源。
        __render_corner(area_caches, positions, dst): 绘制窗口四角。
        __render_edge(area_rects, target_scales, positions, dst): 绘制窗口边缘。
        __render_back(): 绘制窗口背景。
        __render_rect(rect, dst): 绘制矩形，含选择矩形。
    """

    def __init__(self, size: tuple[int, int], pos: tuple[int, int] = (0, 0), viewport: pygame.Surface = None) -> None:
        """
        初始化一个窗口对象。
        
        参数:

            size: 窗口的尺寸。
            pos: 窗口的位置。
            viewport: 绘制所在的视口，默认为System.default_viewport。
        """

        self.contents: Surface
        """窗口的内容表面"""
        
        self.asset: pygame.Surface
        """窗口的资源"""
        
        self.back_opacity: int
        """窗口的背景透明度"""
        
        self.__window_back: Surface
        """窗口的背景表面"""
        
        self.__content_surface: Surface
        """窗口的内容表面"""
        
        self.__has_rect: bool
        """是否有矩形"""
        
        self.__rect_rect: tuple[int, int, int, int]
        """矩形的位置"""
        
        self.__cached_corner: dict[str, list[pygame.Surface]]
        """缓存的窗口四角资源"""
        
        self.__render_count: int
        """用以计时的计数器，设计选择矩形绘制"""

        pass

    def set_rect(self, x: int, y: int, width: int, height: int) -> None:
        """
        设置选择矩形。
        
        参数:

            x: 选择矩形的x坐标。
            y: 选择矩形的y坐标。
            width: 选择矩形的宽度。
            height: 选择矩形的高度。
        """
        pass
    
    def update(self) -> None:
        """更新窗口对象。"""
        pass

    def __presave_corner(self, area_rects: dict[str, list[tuple[int, int, int, int]]]) -> None:
        """
        预存窗口四角资源。
        
        参数:

            area_rects: 四角资源的位置。
        """
        pass

    def __render_corner(self, area_caches: list[pygame.Surface], positions: list[tuple[int, int]], dst: pygame.Surface) -> None:
        """
        绘制窗口四角。
        
        参数:

            area_caches: 四角资源。
            positions: 四角位置。
            dst: 目标画布。
        """
        pass

    def __render_edge(self, area_rects: list[tuple[int, int, int, int]], target_scales: list[tuple[int, int]], positions: list[tuple[int, int]], dst: pygame.Surface) -> None:
        """
        绘制窗口边缘。
        
        参数:

            area_rects: 边缘资源位置。
            target_scales: 边缘目标缩放。
            positions: 边缘位置。
            dst: 目标画布。
        """
        pass

    def __render_back(self) -> None:
        """绘制窗口背景。"""
        pass
        
    def __render_rect(self, rect: tuple[int, int, int, int], dst: pygame.Surface) -> None:
        """
        绘制矩形，含选择矩形。
        
        参数:

            rect: 矩形位置。
            dst: 目标画布。
        """
        pass