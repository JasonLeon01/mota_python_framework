import os
import sys

from project.scripts.core.graphics import mota_graphics

project_directory = os.getcwd()
sys.path.append(os.path.join(project_directory, 'custom_lib'))
import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, frames = None, graphics = mota_graphics):
        super().__init__()
        self.__graphics = graphics
        self.x = 0
        self.y = 0
        self.z = 0
        self.scale = 1.0
        self.move = False
        self.__frame_count = 0
        if frames:
            if isinstance(frames, list):
                self.__frames = frames
            else:
                self.__frames = [frames]
        self.__graphics.add_sprite(self)
        
    def set_frames(self, frames):
        if isinstance(frames, list):
            self.__frames = frames
        else:
            self.__frames = [frames]
    
    def update(self):
        if not self.move:
            self.__frame_count = 0
        self.image = pygame.transform.scale(self.__frames[self.__frame_count], (int(self.__frames[self.__frame_count].get_width() * self.scale), int(self.__frames[self.__frame_count].get_height() * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.center = (self.x, self.y)
        self.__graphics.canvas.blit(self.image, self.rect)
        self.__frame_count = (self.__frame_count + 1) % len(self.__frames)
        
    def dispose(self):
        self.__graphics.remove_sprite(self)
    
    def __del__(self):
        self.dispose()
