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
        self.scale = 1.0
        self.__graphics.add_surface(self)
        
    def update(self):
        draw_surface = pygame.transform.scale(self, (int(self.get_width() * self.scale), int(self.get_height() * self.scale)))
        self.__graphics.canvas.blit(draw_surface, (self.get_rect().x, self.get_rect().y))
        
    def dispose(self):
        self.__graphics.remove_surface(self)
        
    def __del__(self):
        self.dispose()
