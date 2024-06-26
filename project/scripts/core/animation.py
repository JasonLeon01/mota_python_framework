import sys
import os
from project.scripts.core.graphics import Graphics

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Animation:
    def __init__(self, frames, voices):
        self.__frames = frames
        self.__voices = voices
        self.x = 0
        self.y = 0
        self.loop = False
        self.__frame_count = 0
        self.__voice_count = 0
        
    def frame(self):
        whole = pygame.Surface((320, 320))
        for pic in self.__frames[self.__frame_count].components:
            cache, x, y, opacity = pic
            rect = cache.get_rect()
            rect.x = x + 160
            rect.y = y + 160
            rect.center = (rect.x, rect.y)
            show = cache.copy()
            show.set_alpha(opacity)
            whole.blit(show, rect)
        return whole
        
    
    def update(self, dst = Graphics.canvas):
        frame_whole = self.frame()
        rect = frame_whole.get_rect()
        rect.x = self.x
        rect.y = self.y
        rect.center = (self.x, self.y)
        dst.blit(self.frame(), rect)
        if self.__frame_count == self.__voices[self.__voice_count][0]:
            pygame.mixer.Sound(self.__voices[self.__voice_count][1]).play()
            self.__voice_count += 1
        self.__frame_count += 1
        if self.__frame_count == len(self.__frames):
            if self.loop:
                self.__frame_count = 0
                self.__voice_count = 0
            else:
                self.dispose()

    def dispose(self):
        Graphics.remove_animation(self)
        print('LOG: Animation disposed successfully.')
