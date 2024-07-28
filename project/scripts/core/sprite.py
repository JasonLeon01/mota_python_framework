import os
import sys
from typing import List, Union
from project.scripts.core.graphics import Graphics
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, frames: Union[List[pygame.Surface], pygame.Surface] = None, pos = (0, 0)):
        super().__init__()
        self.x, self.y = pos
        self.z = 0
        self.angle = 0
        self.opacity = 255
        self.scale = 1.0
        self.is_visible = True
        self.is_animating = False
        self.is_centre = False
        self.frame_index = 0
        self.interval = 30
        self._frames = self.__process_frames(frames)
        self._frame_count = 0
        print('LOG: Sprite created successfully.', self._frames)
        
    def __process_frames(self, frames):
        if frames is None:
            return []
        if isinstance(frames, list):
            return frames
        else:
            return [frames]
        
    def set_frames(self, frames):
        self._frames = self.__process_frames(frames)
        print('LOG: Sprite frames updated successfully.', self._frames)
    
    def update(self, dst = Graphics.canvas):
        if not self.is_visible:
            return
        self.angle = self.angle % 360
        self.opacity = max(0, min(255, self.opacity))
        if self.scale != 1.0 or self.angle != 0:
            self.image = pygame.transform.rotozoom(self._frames[self.frame_index], self.angle, self.scale)
        else:
            self.image = self._frames[self.frame_index]
        self.image.set_alpha(self.opacity)
        rect = self.image.get_rect()
        rect.x = self.x
        rect.y = self.y
        if self.is_centre:
            rect.center = (self.x, self.y)
        dst.blit(self.image, rect)
        if self.is_animating:
            self._frame_count = self._frame_count + 1
            if self._frame_count >= self.interval:
                self._frame_count = 0
                self.frame_index = (self.frame_index + 1) % len(self._frames)
        
    def dispose(self):
        self.image = None
        Graphics.remove_sprite(self)
        print('LOG: Sprite disposed successfully.')
    
