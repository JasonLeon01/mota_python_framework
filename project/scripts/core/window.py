import os
import sys

import project.scripts.core.surface as surface

from project.scripts.core.graphics import Graphics
from project.scripts.core.cache import Cache
from project.scripts.core.config import Config

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Window(surface.Surface):
    def __init__(self, size):
        super().__init__(size)
        self.contents = None
        self.asset = Cache.system(Config.windowskin_file)
        self.back_opacity = Config.window_opacity
        print('LOG: Window initialized successfully.')

    def __draw_back(self):
        self.fill((0, 0, 0, 0))
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

    def update(self):
        self.__draw_back()
        if self.contents:
            self.contents.x = self.size[0] / 2
            self.contents.y = self.size[1] / 2
            self.contents.update(self)
        super().update()

    def dispose(self):
        self._sprite_group.clear()
        self.contents = None
        Graphics.remove_window(self)
        print('LOG: Window disposed.', self)
