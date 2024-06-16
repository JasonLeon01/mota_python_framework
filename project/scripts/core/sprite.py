import os
import sys

from project.scripts.core.graphics import mota_graphics

project_directory = os.getcwd()
sys.path.append(os.path.join(project_directory, 'custom_lib'))
import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, img = None, graphics = mota_graphics):
        super().__init__()
        mota_graphics.add_sprite(self)
        self.z = 0
        if img:
            self.image = img
            self.rect = self.image.get_rect()
        
    def dispose(self):
        mota_graphics.remove_sprite(self)
    
    def __del__(self):
        self.dispose()
        super().__del__()