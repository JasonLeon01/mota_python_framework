import os
import sys

from project.scripts.core.graphics import Graphics
from project.scripts.core.system import System

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Surface(pygame.Surface):
    def __init__(self, size):
        super().__init__(size, pygame.SRCALPHA)
        self.x = 0
        self.y = 0
        self.ox = 0
        self.oy = 0
        self.z = 0
        self.size = size
        self.angle = 0
        self.opacity = 255
        self.scale = 1.0
        self.visible = True
        self.centre = False
        self._sprite_group = []
        print('LOG: Surface initialized.')
        
    def add_sprite(self, sprite):
        self._sprite_group.append(sprite)
        print('LOG: Sprite added into surface.', self, sprite)
        
    def remove_sprite(self, sprite):
        self._sprite_group.remove(sprite)
        print('LOG: Sprite removed from surface.', self, sprite)

    def draw_text(self, x, y, width, height, text, pos = 0, colour = (255, 255, 255, 255), font = System.font):
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
        
    def update(self, dst = Graphics.canvas):
        if not self.visible:
            return
        self.angle = self.angle % 360
        row_surface = self.copy()
        for sprite in self._sprite_group:
            sprite.update(row_surface)
        draw_surface = pygame.transform.rotozoom(row_surface, self.angle, self.scale)
        draw_surface.set_alpha(self.opacity)
        rect = draw_surface.get_rect()
        rect.x = self.x - self.ox
        rect.y = self.y - self.oy
        if self.centre:
            rect.center = (self.x, self.y)
        dst.blit(draw_surface, (rect.x, rect.y))
        
    def dispose(self):
        self._sprite_group.clear()
        Graphics.remove_surface(self)
        print('LOG: Surface disposed.', self)
    
    def get_color(self, clr):
        color_map = {
            "white": (255, 255, 255, 255),
            "gray": (175, 175, 175, 255),
            "dkgray": (192, 192, 192, 255),
            "black": (0, 0, 0, 255),
            "red": (255, 50, 50, 255),
            "yellow": (255, 255, 128, 255),
            "orange": (255, 185, 25, 255),
            "brown": (200, 150, 75, 255),
            "blue": (128, 255, 255, 255),
            "dkblue": (128, 185, 255, 255),
            "green": (128, 255, 128, 255),
            "pink": (255, 128, 255, 255)
        }
        return color_map.get(clr, (255, 255, 255, 255))