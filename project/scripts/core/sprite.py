import os
import sys

from project.scripts.core.graphics import mota_graphics

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, frames = None):
        super().__init__()
        self.x = 0
        self.y = 0
        self.z = 0
        self.opacity = 255
        self.scale = 1.0
        self.move = False
        self.interval = 30
        self.__frame_count = 0
        if frames:
            if isinstance(frames, list):
                self.__frames = frames
            else:
                self.__frames = [frames]
        
    def set_frames(self, frames):
        if isinstance(frames, list):
            self.__frames = frames
        else:
            self.__frames = [frames]
    
    def update(self, dst = mota_graphics.canvas):
        self.opacity = max(0, min(255, self.opacity))
        now_index = int(self.__frame_count / self.interval)
        self.image = pygame.transform.scale(self.__frames[now_index], (int(self.__frames[now_index].get_width() * self.scale), int(self.__frames[now_index].get_height() * self.scale)))
        rect = self.image.get_rect()
        rect.x = self.x
        rect.y = self.y
        rect.center = (self.x, self.y)
        show = self.image.copy()
        show.set_alpha(self.opacity)
        dst.blit(show, rect)
        if self.move:
            self.__frame_count = (self.__frame_count + 1) % (len(self.__frames) * self.interval)
        
    def dispose(self, group = mota_graphics):
        group.remove_sprite(self)
    
