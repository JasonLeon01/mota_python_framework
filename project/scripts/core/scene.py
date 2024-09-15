import logging, os
from project.scripts.core.cache import Cache
from project.scripts.core.config import Config
import project.scripts.core.method as method
from project.scripts.core.sprite import Sprite
from project.scripts.core.surface import FontStyle
from project.scripts.core.surface import Surface
from project.scripts.core.system import System
from project.scripts.core.graphics import Graphics
from project.scripts.core.viewport import ViewportManager

class Scene_Base:
    def __init__(self):
        self.__quitted = False
        
        for _, attr_value in self.__dict__.items():
            if isinstance(attr_value, list):
                for sub in attr_value:
                    if isinstance(sub, Surface):
                        ViewportManager.add_surface(sub)
                    elif isinstance(sub, Sprite):
                        ViewportManager.add_sprite(sub)
            elif isinstance(attr_value, Surface):
                ViewportManager.add_surface(attr_value)
            elif isinstance(attr_value, Sprite):
                ViewportManager.add_sprite(attr_value)
                
    def load_data_from_json(self, file):
        script_name = os.path.basename(file)
        scene_setting_data = method.load_json_file('project\\data\\scene_settings\\' + os.path.splitext(script_name)[0] + '.json')
        setting_str = ''
        for key, value in scene_setting_data.items():
            flag = False
            for key2, value2 in value.items():
                if key2 == 'type':
                    flag = True
                    mdl = value2.split('.')[0]
                    clss = value2.split('.')[1]
                    if f'from project.scripts.core.{mdl} import {clss}' not in setting_str:
                        setting_str += f'from project.scripts.core.{mdl} import {clss}\n'
                    setting_str += f'self.{key}={clss}('
                    if 'para' in value:
                        flag = False
                elif key2 == 'para':
                    for key3, value3 in value2.items():
                        setting_str += f'{key3}={value3},'
                    setting_str = setting_str[:-1]
                    flag = True
                else:
                    setting_str += f'self.{key}.{key2}={value2}\n'
                if flag:
                    setting_str += ')\n'
                    flag = False
        logging.warning('String generated from json will be exec\nexec string:\n %s', setting_str)
        exec(setting_str)

    def update(self):
        Graphics.update()
        
    def quit(self):
        self.__quitted = True
        Graphics.freeze()
        for _, attr_value in self.__dict__.items():
            if isinstance(attr_value, list):
                for sub in attr_value:
                    if isinstance(sub, Surface):
                        ViewportManager.remove_surface(sub)
                    elif isinstance(sub, Sprite):
                        ViewportManager.remove_sprite(sub)
            elif isinstance(attr_value, Surface):
                ViewportManager.remove_surface(attr_value)
                attr_value.dispose()
            elif isinstance(attr_value, Sprite):
                ViewportManager.remove_sprite(attr_value)
    
    def __del__(self):
        if not self.__quitted:
            self.quit()
