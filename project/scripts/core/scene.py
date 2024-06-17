import project.scripts.core.sprite as sprite
import project.scripts.core.surface as surface
from project.scripts.core.graphics import mota_graphics

class Scene_Base:
    def __init__(self):
        for attr_name, attr_value in self.__dict__.items():
            if isinstance(attr_value, surface.Surface):
                mota_graphics.add_surface(attr_value)
            elif isinstance(attr_value, sprite.Sprite):
                mota_graphics.add_sprite(attr_value)
                
    def update(self):
        mota_graphics.update()
        
    def quit(self):
        for attr_name, attr_value in self.__dict__.items():
            if hasattr(attr_value, 'dispose'):
                attr_value.dispose()
                