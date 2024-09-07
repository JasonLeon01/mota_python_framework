import logging
import os
import sys
from project.scripts.core.surface import Surface
from project.scripts.core.graphics import Graphics
from project.scripts.core.cache import Cache
from project.scripts.core.config import Config
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Window(Surface):
    def __init__(self, size, pos = (0, 0)):
        """
        初始化一个窗口对象。
        
        参数:
            size (tuple): 窗口的尺寸。
            pos (tuple): 窗口的位置。
        
        属性:
            asset: 窗口的资源。
            back_opacity: 窗口的背景透明度。
            __size: 窗口的尺寸。
            __window_back: 窗口的背景表面。
            __content_surface: 窗口的内容表面。
            __has_rect: 是否有矩形。
            __rect_rect: 矩形的位置。
            __cached_corner: 缓存的窗口四角资源。
        """

        self.contents = None
        super().__init__(size, pos)
        self.asset = Cache.system(Config.windowskin_file)
        self.back_opacity = Config.window_opacity
        self.__size = size
        self.__window_back = Surface(size)
        self.__content_surface = Surface((size[0] - 32, size[1] - 32))
        self.__content_surface.x = 16
        self.__content_surface.y = 16
        self.__has_rect = False
        self.__rect_rect = (0, 0, 0, 0)
        self.__presave_corner({
            'window': [
                (128, 0, 16, 16),
                (176, 0, 16, 16),
                (128, 48, 16, 16),
                (176, 48, 16, 16)
            ],
            'rect': [
                (128, 64, 4, 4),
                (156, 64, 4, 4),
                (128, 92, 4, 4),
                (156, 92, 4, 4)
            ]
        })
        self.__render_back()
        logging.info('Window initialized successfully.')

    def set_rect(self, x: int, y: int, width: int, height: int):
        """
        设置选择矩形。
        
        参数:
            x (int): 选择矩形的x坐标。
            y (int): 选择矩形的y坐标。
            width (int): 选择矩形的宽度。
            height (int): 选择矩形的高度。
        """

        self.__has_rect = True
        self.__rect_rect = (x, y, width, height)

    def get_size(self):
        """
        获取窗口尺寸。
        
        返回:
            tuple: 窗口尺寸。
        """

        return self.__size
    
    def set_size(self, size):
        """
        设置窗口尺寸。
        
        参数:
            size (tuple): 窗口尺寸。
        """

        if self.__size != size:
            self.__size = size
            self.__window_back = Surface(size)
            self.__render_back()

    def update(self, dst = Graphics.canvas):
        """
        更新窗口对象。
        
        参数:
            dst: 目标画布。默认为Graphics.canvas。
        """

        self.clear()
        self.__window_back.update(self)
        if self.contents:
            self.__content_surface.clear()
            self.contents.update(self.__content_surface)
            if self.__has_rect:
                self.__render_rect(self.__rect_rect, self.__content_surface)
            self.__content_surface.update(self)
        super().update(dst)

    def dispose(self):
        """
        释放窗口对象。
        """

        self._sprite_group.clear()
        self.contents = None
        Graphics.remove_window(self)
        logging.info('Window disposed. %s', type(self).__name__)

    def __presave_corner(self, area_rects):
        """
        预存窗口四角资源。
        
        参数:
            area_rects (dict): 四角资源的位置。
        """

        self.__cached_corner = {}
        for corner_type, corner_area in area_rects.items():
            self.__cached_corner[corner_type] = []
            for i in range(4):
                self.__cached_corner[corner_type].append(pygame.Surface.subsurface(self.asset, corner_area[i]))        

    def __render_corner(self, area_caches, positions, dst):
        """
        绘制窗口四角。
        
        参数:
            area_caches (list): 四角资源。
            positions (list): 四角位置。
            dst: 目标画布。
        """

        for i in range(4):
            dst.blit(area_caches[i], positions[i])

    def __render_edge(self, area_rects, target_scales, positions, dst):
        """
        绘制窗口边缘。
        
        参数:
            area_rects (list): 边缘资源位置。
            target_scales (list): 边缘目标缩放。
            positions (list): 边缘位置。
        """

        for i in range(4):
            dst.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, area_rects[i]), target_scales[i]), positions[i])

    def __render_back(self):
        """
        绘制窗口背景。
        """

        self.__window_back.clear()
        self.__content_surface.clear()
        if self.__content_surface.size != (self.__size[0] - 32, self.__size[1] - 32):
            self.__content_surface = Surface((self.__size[0] - 32, self.__size[1] - 32))
        row_surface = self.__window_back.copy()
        row_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (0, 0, 128, 128)), (self.__size[0] - 2, self.__size[1] - 2)), (1, 1))
        row_surface.set_alpha(self.back_opacity)
        self.__window_back.blit(row_surface, self.__window_back.get_rect())
        self.__render_corner(self.__cached_corner['window'], [(0, 0), (self.__size[0] - 16, 0), (0, self.__size[1] - 16), (self.__size[0] - 16, self.__size[1] - 16)], self.__window_back)
        self.__render_edge([(144, 0, 32, 16), (144, 48, 32, 16), (128, 16, 16, 32), (176, 16, 16, 32)], [(self.size[0] - 32, 16), (self.size[0] - 32, 16), (16, self.size[1] - 32), (16, self.size[1] - 32)], [(16, 0), (16, self.size[1] - 16), (0, 16), (self.size[0] - 16, 16)], self.__window_back)
        
    def __render_rect(self, rect, dst):
        """
        绘制矩形，含选择矩形。
        
        参数:
            rect (tuple): 矩形位置。
            dst: 目标画布。
        """

        x, y, width, height = rect
        draw_surface = pygame.surface.Surface((width, height), pygame.SRCALPHA)
        draw_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (132, 68, 24, 24)), (width - 8, height - 8)), (4, 4))
        self.__render_corner(self.__cached_corner['rect'], [(0, 0), (width - 4, 0), (0, height - 4), (width - 4, height - 4)], draw_surface)
        self.__render_edge([(132, 64, 24, 4), (132, 92, 24, 4), (128, 68, 4, 24), (156, 68, 4, 24)], [(width - 8, 4), (width - 8, 4), (4, height - 8), (4, height - 8)], [(4, 0), (4, height - 4), (0, 4), (width - 4, 4)], draw_surface)
        draw_surface.set_alpha(120 + 5 * abs(27 - Graphics.frame_count() % 54))
        dst.blit(draw_surface, (x, y))
