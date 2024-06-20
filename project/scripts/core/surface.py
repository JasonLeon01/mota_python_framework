import os
import sys

from project.scripts.core.graphics import mota_graphics
from project.scripts.core.system import mota_system

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
        print('LOG: Surface initialized.')
        
    def add_sprite(self, sprite):
        self.__sprite_group.append(sprite)
        print('LOG: Sprite added into surface.', self)
        
    def remove_sprite(self, sprite):
        self.__sprite_group.remove(sprite)
        print('LOG: Sprite removed from surface.', self)

    def draw_text(self, x, y, width, height, text, pos = 0, colour = (255, 255, 255), font = mota_system.font):
        size = font.size(text)
        dx, dy = 0, 0
        if size[0] < width:
            if (pos == 1):
                dx = (width - size[0]) / 2
            if (pos == 2):
                dx = width - size[0]
        if size[1] < height:
            dy = (height - size[1]) / 2
        text_surface = font.render(text, True, colour)
        self.blit(text_surface, (x + dx, y + dy), (0, 0, min(size[0], width), min(size[1], height)))


    def clear(self):
        self.fill((0, 0, 0, 0))
        print('LOG: Surface cleared.', self)
        
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
        print('LOG: Surface disposed.', self)
    