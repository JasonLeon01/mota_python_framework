import logging
from project.scripts.core.surface import Surface
from project.scripts.core.surface import FontStyle
from project.scripts.core.system import System

class Text(Surface):
    def __init__(self, content, size, pos, font_size, font_style = FontStyle.NORMAL, colour=(255, 255, 255, 255)):
        super().__init__(size, pos)
        self.font.size = font_size
        self.font_style = font_style
        self.__content = content
        self.__colour = colour
        self.refresh()
        logging.info('Text settled.')

    def refresh(self):
        self.clear()
        self.draw_text(0, 0, self._size[0], self._size[1], self.__content, 1, self.__colour)
        logging.info('Text refreshed.')
        
    def get_content(self):
        return self.__content

    def set_content(self, new_content):
        if new_content != self.__content:
            self.__content = new_content
            self.refresh()
            logging.info('New text settled.')

    def get_colour(self):
        return self.__colour
    
    def set_colour(self, new_colour):
        self.__colour = new_colour
        self.refresh()
        logging.info('New colour settled.')
        
    def set_font_style(self, new_font_style):
        self.font_style = new_font_style
        self.refresh()
        logging.info('New font style settled.')
    