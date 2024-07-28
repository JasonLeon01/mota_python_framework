import os
import sys
from project.scripts.core.surface import Surface
from project.scripts.core.graphics import Graphics
from project.scripts.core.cache import Cache
from project.scripts.core.config import Config
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Window(Surface):
    def __init__(self, size):
        super().__init__(size)
        self.contents = None
        self.asset = Cache.system(Config.windowskin_file)
        self.back_opacity = Config.window_opacity
        self.__content_surface = Surface((self.size[0] - 32, self.size[1] - 32))
        self.__content_surface.x = 16
        self.__content_surface.y = 16
        self.__has_rect = False
        self.__rect_rect = (0, 0, 0, 0)
        print('LOG: Window initialized successfully.')

    def __render_corner(self, area_rects, positions, dst):
        for i in range(4):
            dst.blit(pygame.Surface.subsurface(self.asset, area_rects[i]), positions[i])

    def __render_edge(self, area_rects, target_scales, positions, dst):
        for i in range(4):
            dst.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, area_rects[i]), target_scales[i]), positions[i])

    def __render_back(self):
        self.fill((0, 0, 0, 0))
        self.__content_surface.fill((0, 0, 0, 0))
        if self.__content_surface.size != (self.size[0] - 32, self.size[1] - 32):
            self.__content_surface = Surface((self.size[0] - 32, self.size[1] - 32))
        row_surface = self.copy()
        row_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (0, 0, 128, 128)), (self.size[0] - 2, self.size[1] - 2)), (1, 1))
        row_surface.set_alpha(self.back_opacity)
        self.blit(row_surface, self.get_rect())
        self.__render_corner([(128, 0, 16, 16), (176, 0, 16, 16), (128, 48, 16, 16), (176, 48, 16, 16)], [(0, 0), (self.size[0] - 16, 0), (0, self.size[1] - 16), (self.size[0] - 16, self.size[1] - 16)], self)
        self.__render_edge([(144, 0, 32, 16), (144, 48, 32, 16), (128, 16, 16, 32), (176, 16, 16, 32)], [(self.size[0] - 32, 16), (self.size[0] - 32, 16), (16, self.size[1] - 32), (16, self.size[1] - 32)], [(16, 0), (16, self.size[1] - 16), (0, 16), (self.size[0] - 16, 16)], self)

    def set_rect(self, x: int, y: int, width: int, height: int):
        self.__has_rect = True
        self.__rect_rect = (x, y, width, height)
        
    def __render_rect(self, rect, dst):
        x, y, width, height = rect
        draw_surface = pygame.surface.Surface((width, height), pygame.SRCALPHA)
        draw_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (132, 68, 24, 24)), (width - 8, height - 8)), (4, 4))
        self.__render_corner([(128, 64, 4, 4), (156, 64, 4, 4), (128, 92, 4, 4), (156, 92, 4, 4)], [(0, 0), (width - 4, 0), (0, height - 4), (width - 4, height - 4)], draw_surface)
        self.__render_edge([(132, 64, 24, 4), (132, 92, 24, 4), (128, 68, 4, 24), (156, 68, 4, 24)], [(width - 8, 4), (width - 8, 4), (4, height - 8), (4, height - 8)], [(4, 0), (4, height - 4), (0, 4), (width - 4, 4)], draw_surface)
        draw_surface.set_alpha(120 + 5 * abs(27 - Graphics.frame_count() % 54))
        dst.blit(draw_surface, (x, y))

    def update(self):
        self.__render_back()
        if self.contents:
            self.contents.update(self.__content_surface)
            if self.__has_rect:
                self.__render_rect(self.__rect_rect, self.__content_surface)
            self.__content_surface.update(self)
        super().update()

    def dispose(self):
        self._sprite_group.clear()
        self.contents = None
        Graphics.remove_window(self)
        print('LOG: Window disposed.', self)
