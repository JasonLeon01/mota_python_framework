import os
import sys
import math

from project.scripts.core.audio import Audio
from project.scripts.core.config import Config
from project.scripts.core.system import System
import project.scripts.core.window as window
from project.scripts.core.input import Input

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class ChoiceWindow(window.Window):
    def __init__(self, size):
        super().__init__(size)
        self.colomn = 1
        self.cursor_height = 32
        self.index = 0
        self.items = 1
        self.active = True
    
    def rows(self):
        return int(math.ceil(1.0 * self.items / self.colomn))

    def render_rect(self, x, y, width, height):
        pass

    def update_cursor_rect(self):
        row = self.index / self.colomn
        cursor_width = self.size[0] / self.colomn - 32
        x = self.index % self.colomn * (cursor_width + 32)
        y = int(row) * self.cursor_height
        if self.contents:
            y -= self.oy
        self.render_rect(x, y, cursor_width, self.cursor_height)

    def mouse_in_rect(self):
        x, y = pygame.mouse.get_pos()
        if x > self.x and x < self.x + self.size[0] and y > self.y and y < self.y + self.size[1]:
            return True
        return False
    
    def confirm(self):
        return self.mouse_in_rect() and Input.trigger(pygame.K_RETURN)
    
    def cancel(self):
        return self.mouse_in_rect() and Input.trigger(pygame.K_ESCAPE)

    def update(self):
        super().update()
        if not self.active or self.items == 0 or self.index < 0:
            return
        if self.index >= self.items:
            self.index = self.items - 1
        if Input.repeat(pygame.K_UP):
            if (self.colomn == 1 and Input.trigger(pygame.K_UP)) or self.index >= self.colomn:
                self.index = (self.index - self.colomn + self.items) % self.items
                Audio.play_voice(Config.cursor_se)
        if Input.repeat(pygame.K_DOWN):
            if (self.colomn == 1 and Input.trigger(pygame.K_DOWN)) or self.index < self.items - self.colomn:
                self.index = (self.index + self.colomn) % self.items
                Audio.play_voice(Config.cursor_se)
        if Input.repeat(pygame.K_LEFT) or (self.mouse_in_rect() and System.wheel > 0):
            if self.colomn > 1 and self.index > 0:
                self.index -= 1
        if Input.repeat(pygame.K_RIGHT) or (self.mouse_in_rect() and System.wheel < 0):
            if self.colomn > 1 and self.index < self.items - 1:
                self.index += 1
        if self.contents:
            if (self.index / self.colomn) * 32 - self.contents.oy + 32 > self.size[1] - 32:
                self.contents.oy = (self.index / self.colomn) * 32 - self.size[1] + 64
            if (self.index / self.colomn) * 32 - self.contents.oy < 0:
                self.contents.oy = (self.index / self.colomn) * 32
        self.update_cursor_rect()
