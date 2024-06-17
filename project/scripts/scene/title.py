from project.scripts.core.system import mota_system
from project.scripts.core.cache import mota_cache
from project.scripts.core.config import mota_config
from project.scripts.core.graphics import mota_graphics
import project.scripts.core.sprite as sprite

import project.scripts.core.scene as scene_base
import time

class Scene(scene_base.Scene_Base):
    def __init__(self):
        self.title_sprite = sprite.Sprite(mota_cache.system(mota_config.title_file))
        self.title_sprite.x = 320
        self.title_sprite.y = 240
        self.star_sprite = sprite.Sprite(mota_cache.system(['star-1', 'star-2', 'star-3', 'star-2', 'star-1']))
        self.star_sprite.x = 320
        self.star_sprite.y = 32
        self.star_sprite.move = True
        self.star_sprite.interval = 15
        self.__change = False
        super().__init__()
        
    def update(self):
        if self.title_sprite.opacity == 255 and not self.__change:
            self.__change = True
        elif self.title_sprite.opacity == 128 and self.__change:
            self.__change = False
        if self.__change:
            self.title_sprite.opacity -= 1
        else:
            self.title_sprite.opacity += 1
        super().update()
