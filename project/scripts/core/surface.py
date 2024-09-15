import logging, enum, copy
from project.scripts.core.system import System
import pygame

class FontStyle(enum.Enum):
    NORMAL, SHADOW, STROKE = range(3)

class Surface(pygame.Surface):

    def __init__(self, size, pos = (0, 0)):
        super().__init__(size, pygame.SRCALPHA)
        self.x, self.y = pos
        self.ox = 0
        self.oy = 0
        self.z = 0
        self._size = size
        self.angle = 0
        self.opacity = 255
        self.scale = 1.0
        self.font_style = FontStyle.NORMAL
        self.is_visible = True
        self.is_centre = False
        self._sprite_group = []
        self._surface_group = []
        logging.info('Surface initialized')
        
    def get_size(self):
        return self._size
        
    def add_sprite(self, sprite):
        self._sprite_group.append(sprite)
        logging.info('Sprite added into surface. %s', sprite)
        
    def remove_sprite(self, sprite):
        self._sprite_group.remove(sprite)
        logging.info('Sprite removed from surface. %s', sprite)

    def clear_sprite(self):
        self._sprite_group.clear()
        logging.info('Sprite cleared from surface. %s', self)

    def add_surface(self, surface):
        self._surface_group.append(surface)
        logging.info('Surface added into surface. %s', surface)
    
    def remove_surface(self, surface):
        self._surface_group.remove(surface)
        logging.info('Surface removed from surface. %s', surface)

    def clear_surface(self):
        self._surface_group.clear()
        logging.info('Surface cleared from surface. %s', self)

    def draw_text(self, x, y, width, height, text, pos=0, colour=(255, 255, 255, 255), font_size = -1):
        logging.info('text %s', text)
        from project.scripts.core.system import System
        if font_size == -1:
            font_size = System.default_font_size
        size = System.fonts[font_size].size(text)
        dx, dy = 0, 0
        if size[0] < width:
            if (pos == 1):
                dx = (width - size[0]) / 2
            if (pos == 2):
                dx = width - size[0]
        if size[1] < height:
            dy = (height - size[1]) / 2

        if self.font_style != FontStyle.NORMAL:
            effect_text_surface = System.fonts[font_size].render(text, True, (0, 0, 0))
            if self.font_style == FontStyle.SHADOW:
                self.blit(effect_text_surface, (x + dx + 1, y + dy + 1), (0, 0, width, height))
            if self.font_style == FontStyle.STROKE:
                self.blit(effect_text_surface, (x + dx + 1, y + dy + 1), (0, 0, width, height))
                self.blit(effect_text_surface, (x + dx - 1, y + dy + 1), (0, 0, width, height))
                self.blit(effect_text_surface, (x + dx + 1, y + dy - 1), (0, 0, width, height))
                self.blit(effect_text_surface, (x + dx - 1, y + dy - 1), (0, 0, width, height))
                
        text_surface = System.fonts[font_size].render(text, True, colour)
        self.blit(text_surface, (x + dx, y + dy), (0, 0, width, height))
        
        logging.info('Text drawn. %s', text)

    def clear(self, need_log=False):
        self.fill((0, 0, 0, 0))
        if need_log:
            logging.info('Surface cleared. %s', self)
        
    def update(self, dst):
        if not self.is_visible:
            return
        
        self.angle = self.angle % 360
        
        total_count = len(self._surface_group) + len(self._sprite_group)
        raw_surface = self.copy()
        count, z = 0, 0
        while count < total_count:
            for sprite in self._sprite_group:
                if sprite.z == z:
                    sprite.update(raw_surface)
                    count += 1
            for surface in self._surface_group:
                if surface.z == z:
                    surface.update(raw_surface)
                    count += 1
            z += 1
        if self.scale != 1.0 or self.angle != 0:
            draw_surface = pygame.transform.rotozoom(raw_surface, self.angle, self.scale)
        else:
            draw_surface = raw_surface
        
        draw_surface.set_alpha(self.opacity)
        
        rect = draw_surface.get_rect()
        rect.x = self.x - self.ox
        rect.y = self.y - self.oy
        if self.is_centre:
            rect.center = (self.x, self.y)
        dst.blit(draw_surface, (rect.x, rect.y))
            
    def get_color(self, clr):
        color_map = {
            "white": (255, 255, 255, 255),
            "gray": (175, 175, 175, 255),
            "dkgray": (192, 192, 192, 255),
            "black": (0, 0, 0, 255),
            "red": (255, 50, 50, 255),
            "yellow": (255, 255, 128, 255),
            "orange": (255, 185, 25, 255),
            "brown": (200, 150, 75, 255),
            "blue": (128, 255, 255, 255),
            "dkblue": (128, 185, 255, 255),
            "green": (128, 255, 128, 255),
            "pink": (255, 128, 255, 255)
        }
        return color_map.get(clr, (255, 255, 255, 255))
    
    def dispose(self):
        self.clear_sprite()
        self.clear_surface()
        logging.info('Surface deleted. %s', self)
