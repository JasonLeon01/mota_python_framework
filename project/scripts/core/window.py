import os
import sys

import project.scripts.core.surface as surface

from project.scripts.core.graphics import mota_graphics
from project.scripts.core.cache import mota_cache
from project.scripts.core.config import mota_config

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Window(surface.Surface):
    def __init__(self, size, asset = mota_cache.system(mota_config.windowskin_file)):
        super().__init__(size)
        self.contents = None
        self.asset = asset
        print('LOG: Window initialized successfully.')

    def __draw_back(self):
        self.clear()
        self.blit(pygame.transform.scale(pygame.Surface.subsurface(self.asset, (0, 0, 128, 128)), (self.size[0], self.size[1])))

    def update(self, dst = mota_graphics.canvas):
        self.__draw_back()
        if self.contents:
            self.contents.update(self)
        super().update(dst)
