import logging
import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, frames = None, pos = (0, 0)):
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
        logging.info('Sprite created successfully. %s', self._frames)
        
    def __process_frames(self, frames):
        if frames is None:
            return []
        if isinstance(frames, list):
            return frames
        else:
            return [frames]
        
    def set_frames(self, frames):
        self._frames = self.__process_frames(frames)
        logging.info('Sprite frames updated successfully. %s', self._frames)
    
    def update(self, dst):
        if not self.is_visible:
            return
        self.angle = self.angle % 360
        self.opacity = max(0, min(255, self.opacity))
        if self.scale != 1.0 or self.angle != 0:
            image = pygame.transform.rotozoom(self._frames[self.frame_index], self.angle, self.scale)
        else:
            image = self._frames[self.frame_index]
        image.set_alpha(self.opacity)
        rect = image.get_rect()
        rect.x = self.x
        rect.y = self.y
        if self.is_centre:
            rect.center = (self.x, self.y)
        dst.blit(image, (rect.x, rect.y))
        if self.is_animating:
            self._frame_count = self._frame_count + 1
            if self._frame_count >= self.interval:
                self._frame_count = 0
                self.frame_index = (self.frame_index + 1) % len(self._frames)
