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

    def __draw_back(self):
        self.fill((0, 0, 0, 0))
        self.__content_surface.fill((0, 0, 0, 0))
        if self.__content_surface.size != (self.size[0] - 32, self.size[1] - 32):
            self.__content_surface = Surface((self.size[0] - 32, self.size[1] - 32))
        row_surface = self.copy()
        row_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (0, 0, 128, 128)), (self.size[0] - 2, self.size[1] - 2)), (1, 1))
        row_surface.set_alpha(self.back_opacity)
        row_surface.blit(pygame.Surface.subsurface(self.asset, (128, 0, 16, 16)), (0, 0))
        row_surface.blit(pygame.Surface.subsurface(self.asset, (176, 0, 16, 16)), (self.size[0] - 16, 0))
        row_surface.blit(pygame.Surface.subsurface(self.asset, (128, 48, 16, 16)), (0, self.size[1] - 16))
        row_surface.blit(pygame.Surface.subsurface(self.asset, (176, 48, 16, 16)), (self.size[0] - 16, self.size[1] - 16))
        row_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (144, 0, 32, 16)), (self.size[0] - 32, 16)), (16, 0))
        row_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (144, 48, 32, 16)), (self.size[0] - 32, 16)), (16, self.size[1] - 16))
        row_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (128, 16, 16, 32)), (16, self.size[1] - 32)), (0, 16))
        row_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (176, 16, 16, 32)), (16, self.size[1] - 32)), (self.size[0] - 16, 16))
        self.blit(row_surface, self.get_rect())

    def set_rect(self, x, y, width, height):
        self.__has_rect = True
        self.__rect_rect = (x, y, width, height)
        
    def __render_rect(self, rect, dst):
        x, y, width, height = rect
        draw_surface = pygame.surface.Surface((width, height), pygame.SRCALPHA)
        draw_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (132, 68, 24, 24)), (width - 8, height - 8)), (4, 4))
        draw_surface.blit(pygame.Surface.subsurface(self.asset, (128, 64, 4, 4)), (0, 0))
        draw_surface.blit(pygame.Surface.subsurface(self.asset, (156, 64, 4, 4)), (0 + width - 4, 0))
        draw_surface.blit(pygame.Surface.subsurface(self.asset, (128, 92, 4, 4)), (0, height - 4))
        draw_surface.blit(pygame.Surface.subsurface(self.asset, (156, 92, 4, 4)), (0 + width - 4, height - 4))
        draw_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (132, 64, 24, 4)), (width - 8, 4)), (4, 0))
        draw_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (132, 92, 24, 4)), (width - 8, 4)), (4, height - 4))
        draw_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (128, 68, 4, 24)), (4, height - 8)), (0, 4))
        draw_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (156, 68, 4, 24)), (4, height - 8)), (width - 4, 4))
        draw_surface.set_alpha(120 + 5 * abs(27 - Graphics.frame_count() % 54))
        dst.blit(draw_surface, (x, y))

    def update(self):
        self.__draw_back()
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
