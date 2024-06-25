import project.scripts.core.sprite as sprite
import project.scripts.core.surface as surface
import project.scripts.core.window as window
from project.scripts.core.graphics import Graphics

class Scene_Base:
    def __init__(self):
        for attr_name, attr_value in self.__dict__.items():
            if isinstance(attr_value, list):
                for sub in attr_value:
                    if isinstance(sub, window.Window):
                        Graphics.add_window(sub)
                    elif isinstance(sub, surface.Surface):
                        Graphics.add_surface(sub)
                    elif isinstance(sub, sprite.Sprite):
                        Graphics.add_sprite(sub)
            elif isinstance(attr_value, window.Window):
                Graphics.add_window(attr_value)
            elif isinstance(attr_value, surface.Surface):
                Graphics.add_surface(attr_value)
            elif isinstance(attr_value, sprite.Sprite):
                Graphics.add_sprite(attr_value)
                
    def update(self):
        Graphics.update()
        
    def quit(self):
        for attr_name, attr_value in self.__dict__.items():
            if isinstance(attr_value, list):
                for sub in attr_value:
                    if hasattr(sub, 'dispose'):
                        sub.dispose()
            elif hasattr(attr_value, 'dispose'):
                attr_value.dispose()
                