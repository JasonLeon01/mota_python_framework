import os
import sys

from project.scripts.core.graphics import mota_graphics

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Surface(pygame.Surface):
    def __init__(self, size):
        super().__init__(size, pygame.SRCALPHA)
        self.x = 0
        self.y = 0
        self.z = 0
        self.size = size
        self.angle = 0
        self.opacity = 255
        self.scale = 1.0
        self.__sprite_group = []
        
    def add_sprite(self, sprite):
        self.__sprite_group.append(sprite)
        
    def remove_sprite(self, sprite):
        self.__sprite_group.remove(sprite)

    def clear(self):
        self = self.fill((0, 0, 0, 0))
        
    def update(self, dst = mota_graphics.canvas):
        self.angle = self.angle % 360
        row_surface = self.copy()
        for sprite in self.__sprite_group:
            sprite.update(row_surface)
        draw_surface = pygame.transform.scale(row_surface, (int(row_surface.get_width() * self.scale), int(row_surface.get_height() * self.scale)))
        show = pygame.transform.rotate(draw_surface, self.angle)
        show.set_alpha(self.opacity)
        rect = show.get_rect()
        rect.x = self.x
        rect.y = self.y
        rect.center = (self.x, self.y)
        dst.blit(show, rect)
        
    def dispose(self, group = mota_graphics):
        self.__sprite_group.clear()
        group.remove_surface(self)
    