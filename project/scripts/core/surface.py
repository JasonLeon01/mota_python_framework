import os
import sys

from project.scripts.core.graphics import mota_graphics

project_directory = os.getcwd()
sys.path.append(os.path.join(project_directory, 'custom_lib'))
import pygame

class Surface(pygame.Surface):
    def __init__(self, size, graphics = mota_graphics):
        super().__init__(size)
        self.__graphics = graphics
        self.z = 0
        self.__graphics.add_surface(self)
        
    def dispose(self):
        self.__graphics.remove_surface(self)
        
    def __del__(self):
        self.dispose()
        super().__del__()