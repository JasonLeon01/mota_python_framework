from project.scripts.core.system import mota_system
from project.scripts.core.cache import mota_cache
from project.scripts.core.config import mota_config
import project.scripts.core.sprite as sprite

import project.scripts.core.scene as scene_base
import time

class Scene(scene_base.Scene_Base):
    def __init__(self):
        self.title_sprite = sprite.Sprite(mota_cache.system(mota_config.title_file))
        self.title_sprite.x = 320
        self.title_sprite.y = 240
        
    def update(self):
        super().update()
