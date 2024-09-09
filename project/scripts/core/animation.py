from project.scripts.core.system import System
from project.scripts.core.audio import Audio
import pygame

class Animation:
    def __init__(self, frames, voices, viewport = None):
        self.__frames = frames
        self.__voices = voices
        self.x = 0
        self.y = 0
        self.loop = False
        if viewport is None:
            viewport = System.default_viewport
        self.viewport = viewport
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

    def update(self):
        frame_whole = self.frame()
        rect = frame_whole.get_rect()
        rect.x = self.x
        rect.y = self.y
        rect.center = (self.x, self.y)
        self.viewport.blit(self.frame(), rect)
        
        if self.__frame_count == self.__voices[self.__voice_count][0]:
            Audio.play_voice(self.__voices[self.__voice_count][1])
            self.__voice_count += 1
        
        self.__frame_count += 1
        
    def has_reach_end(self):
        return self.__frame_count == len(self.__frames)

    def reset(self):
        self.__frame_count = 0
        self.__voice_count = 0
