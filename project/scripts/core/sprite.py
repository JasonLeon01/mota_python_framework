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
        self.interval = 30
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
        now_index = int(self.__frame_count / self.interval)
        self.image = pygame.transform.scale(self.__frames[now_index], (int(self.__frames[now_index].get_width() * self.scale), int(self.__frames[now_index].get_height() * self.scale)))
        rect = self.image.get_rect()
        rect.x = self.x
        rect.y = self.y
        rect.center = (self.x, self.y)
        self.__graphics.canvas.blit(self.image, rect)
        self.__frame_count = (self.__frame_count + 1) % (len(self.__frames) * self.interval)
        
    def dispose(self):
        self.__graphics.remove_sprite(self)
    
    def __del__(self):
        self.dispose()
