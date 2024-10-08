import math, logging
from project.scripts.core.audio import Audio
from project.scripts.core.config import Config
from project.scripts.core.system import System
from project.scripts.core.window import Window
from project.scripts.core.input import Input
import pygame

class ChoiceWindow(Window):
    def __init__(self, size, pos):
        super().__init__(size, pos)
        self.column = 1
        self.cursor_height = 32
        self.index = 0
        self.items = 1
        self.is_active = True

    def rows(self):
        return int(math.ceil(1.0 * self.items / self.column))

    def update_cursor_rect(self):
        row = self.index / self.column
        cursor_width = self.get_size()[0] / self.column - 32
        x = self.index % self.column * (cursor_width + 32)
        y = int(row) * self.cursor_height
        if self.contents:
            y -= self.contents.oy
        self.set_rect(x, y, cursor_width, self.cursor_height)

    def mouse_in_rect(self):
        return Input.in_rect((self.x + 16, self.y + 16, self.get_size()[0] - 32, self.get_size()[1] - 32))
    
    def confirm(self):
        if Input.trigger_confirm():
            return True
        
        if self.mouse_in_rect():
            if Input.left_click('trigger'):
                x, y = Input.get_mouse_pos()
                screen_index = (y - self.y - 16) // self.cursor_height
                now_index = screen_index * self.column + (x - self.x - 16) // (self.get_size()[0] / self.column - 32) + self.column * (self.contents.oy // self.cursor_height)
                logging.info('Caught index on screen is %s, now index is %s', now_index, self.index)
                
                if now_index == self.index:
                    return True
                
                Audio.play_voice(Config.cursor_se)
                self.index = now_index
        return False

    def cancel(self):
        return self.mouse_in_rect() and Input.trigger(pygame.K_ESCAPE) or Input.right_click('repeat')

    def _key_response(self):
        if Input.repeat(pygame.K_UP):
            if (self.column == 1 and Input.trigger(pygame.K_UP)) or self.index >= self.column:
                self.index = (self.index - self.column + self.items) % self.items
                Audio.play_voice(Config.cursor_se)
        if Input.repeat(pygame.K_DOWN):
            if (self.column == 1 and Input.trigger(pygame.K_DOWN)) or self.index < self.items - self.column:
                self.index = (self.index + self.column) % self.items
                Audio.play_voice(Config.cursor_se)
        if Input.repeat(pygame.K_LEFT):
            if self.column > 1 and self.index > 0:
                self.index = (self.index - 1 + self.items) % self.items
                Audio.play_voice(Config.cursor_se)
        if Input.repeat(pygame.K_RIGHT):
            if self.column > 1 and self.index < self.items - 1:
                self.index = (self.index + 1) % self.items
                Audio.play_voice(Config.cursor_se)

    def _mouse_response(self):
        if self.mouse_in_rect() and System.wheel != 0:
            if System.wheel > 0:
                self.index = (self.index - 1 + self.items) % self.items
                Audio.play_voice(Config.cursor_se)
            elif System.wheel < 0:
                self.index = (self.index + 1) % self.items
                Audio.play_voice(Config.cursor_se)
            System.wheel = 0

    def update(self, dst):
        super().update(dst)
        if not self.is_active or self.items == 0 or self.index < 0:
            return
        
        if self.index >= self.items:
            self.index = self.items - 1
        
        self._key_response()
        self._mouse_response()
        
        if self.contents:
            if (self.index // self.column) * self.cursor_height - self.contents.oy + 32 > self.get_size()[1] - 32:
                self.contents.oy = (self.index // self.column) * self.cursor_height - self.get_size()[1] + 64
            if (self.index // self.column) * self.cursor_height - self.contents.oy < 0:
                self.contents.oy = (self.index // self.column) * self.cursor_height
        
        self.update_cursor_rect()
