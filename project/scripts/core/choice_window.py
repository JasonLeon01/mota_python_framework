import math

import project.scripts.core.window as window

class ChoiceWindow(window.Window):
    def __init__(self, size):
        super().__init__(size)
        self.colomn = 1
        self.cursor_height = 32
        self.index = 0
        self.choices = []
        self.__oy = 0
    
    def rows(self):
        return int(math.ceil(1.0 * len(self.choices) / self.colomn))

    def render_rect(self, x, y, width, height):
        pass
    def update_cursor_rect(self):
        if self.index < 0:
            return
        if self.index >= len(self.choices):
            self.index = len(self.choices) - 1
        row = self.index / self.colomn
        cursor_width = self.size[0] / self.colomn - 32
        x = self.index % self.colomn * (cursor_width + 32)
        y = int(row) * self.cursor_height
        self.cursor_rect = (x, y, cursor_width, cursor_height)