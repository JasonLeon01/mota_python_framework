import os
import sys

import project.scripts.core.surface as surface

from project.scripts.core.cache import Cache
from project.scripts.core.config import Config

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Window(surface.Surface):
    def __init__(self, size):
        super().__init__(size)
        self.contents = None
        self.asset = Cache.system(Config.windowskin_file)
        self.opacity = Config.window_opacity
        print('LOG: Window initialized successfully.')
        self.__draw_back()

    def __draw_back(self):
        self.clear()
        rect = self.get_rect()
        rect.x = 0
        rect.y = 0
        row_surface = self.copy()
        row_surface.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (0, 0, 128, 128)), (self.size[0], self.size[1])), rect)
        row_surface.set_alpha(self.opacity)
        self.blit(row_surface, rect)

    def update(self):
        if self.contents:
            self.contents.update(self)
        super().update()
