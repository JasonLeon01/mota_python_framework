from project.scripts.core.cache import mota_cache
from project.scripts.core.config import mota_config
import project.scripts.core.sprite as sprite
import project.scripts.core.surface as surface

import project.scripts.core.scene as scene_base

class Scene(scene_base.Scene_Base):
    def __init__(self):
        self.title_surface = surface.Surface((640, 480))
        title_sprite = sprite.Sprite(mota_cache.system(mota_config.title_file))
        title_sprite.x = 320
        title_sprite.y = 240
        self.title_surface.add_sprite(title_sprite)
        sstar_sprite = sprite.Sprite(mota_cache.system(['star-1', 'star-2', 'star-3', 'star-2', 'star-1']))
        sstar_sprite.x = 160
        sstar_sprite.y = 128
        sstar_sprite.move = True
        sstar_sprite.interval = 5
        self.title_surface.add_sprite(sstar_sprite)
        self.title_surface.x = 320
        self.title_surface.y = 240
        self.title_surface_2 = surface.Surface((320, 240))
        ssstar_sprite = sprite.Sprite(mota_cache.system(['star-1', 'star-2', 'star-3', 'star-2', 'star-1']))
        ssstar_sprite.x = 160
        ssstar_sprite.y = 120
        ssstar_sprite.move = True
        ssstar_sprite.interval = 10
        self.title_surface_2.add_sprite(ssstar_sprite)
        self.title_surface_2.x = 320
        self.title_surface_2.y = 240
        self.star_sprite = sprite.Sprite(mota_cache.system(['star-1', 'star-2', 'star-3', 'star-2', 'star-1']))
        self.star_sprite.x = 320
        self.star_sprite.y = 32
        self.star_sprite.move = True
        self.star_sprite.interval = 15
        self.__change = False
        super().__init__()
        
    def update(self):
        if self.title_surface.opacity == 255 and not self.__change:
            self.__change = True
        elif self.title_surface.opacity == 190 and self.__change:
            self.__change = False
        if self.__change:
            self.title_surface.opacity -= 1
        else:
            self.title_surface.opacity += 1
        self.star_sprite.angle += 1
        super().update()
