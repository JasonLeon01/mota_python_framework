import os
import sys

from project.scripts.core.graphics import mota_graphics

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Surface(pygame.Surface):
    def __init__(self, rect):
        super().__init__((rect.width, rect.height))
        self.__rect = rect
        self.z = 0
        self.opacity = 255
        self.scale = 1.0
        self.__sprite_group = []
        
    def add_sprite(self, sprite):
        self.__sprite_group.append(sprite)
        
    def remove_sprite(self, sprite):
        self.__sprite_group.remove(sprite)
        
    def update(self, dst = mota_graphics.canvas):
        row_surface = self.copy()
        for sprite in self.__sprite_group:
            sprite.update(row_surface)
        draw_surface = pygame.transform.scale(row_surface, (int(row_surface.get_width() * self.scale), int(row_surface.get_height() * self.scale)))
        rect = draw_surface.get_rect()
        rect.x = self.__rect.x
        rect.y = self.__rect.y
        show = draw_surface.copy()
        show.set_alpha(self.opacity)
        dst.blit(show, rect)
        
    def dispose(self, group = mota_graphics):
        self.__sprite_group.clear()
        group.remove_surface(self)
    