from project.scripts.core.cache import mota_cache

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Animation:
    def __init__(self, frames, voices):
        self.__frames = frames
        self.__voices = voices
        self.x = 0
        self.y = 0
        self.__frame_count = 0
        
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
        
    
    def update(self, dst = sprite.mota_graphics.canvas):
        frame_whole = self.frame()
        rect = frame_whole.get_rect()
        rect.x = self.x
        rect.y = self.y
        rect.center = (self.x, self.y)
        dst.blit(self.frame(), rect)