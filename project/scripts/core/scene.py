import logging, os
from project.scripts.core.cache import Cache
from project.scripts.core.config import Config
import project.scripts.core.method as method
from project.scripts.core.sprite import Sprite
from project.scripts.core.surface import Surface
from project.scripts.core.system import System
from project.scripts.core.window import Window
from project.scripts.core.graphics import Graphics

class Scene_Base:
    """
    场景基类。
    该类提供了场景对象的基本属性和方法。
    
    属性:
        __quitted: 退出标志。
        
    方法:
        load_data_from_json: 从JSON文件中加载数据。
        update: 更新方法。
        quit: 退出方法。
    """
    
    def __init__(self):
        """
        初始化场景对象。

        根据场景对象的属性，将窗口、表面和精灵添加到Graphics模块中。
        
        属性:
            __quitted: 退出标志。
        """
        
        # 退出标志
        self.__quitted = False
        
        # 添加窗口、表面和精灵
        for _, attr_value in self.__dict__.items():
            if isinstance(attr_value, list):
                for sub in attr_value:
                    if isinstance(sub, Window):
                        Graphics.add_window(sub)
                    elif isinstance(sub, Surface):
                        Graphics.add_surface(sub)
                    elif isinstance(sub, Sprite):
                        Graphics.add_sprite(sub)
            elif isinstance(attr_value, Window):
                Graphics.add_window(attr_value)
            elif isinstance(attr_value, Surface):
                Graphics.add_surface(attr_value)
            elif isinstance(attr_value, Sprite):
                Graphics.add_sprite(attr_value)
                
    def load_data_from_json(self, file: str):
        """
        从JSON文件中加载数据，解析成为对应Python代码。
        
        参数:
            file: JSON文件路径。
        """
        
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
        """
        基类的更新仅仅是更新Graphics模块。
        """

        Graphics.update()
        
    def quit(self):
        """
        退出场景。
        此时将冻结Graphics模块，并释放所有资源。
        """

        self.__quitted = True
        Graphics.freeze()
        for attr_name, attr_value in self.__dict__.items():
            if isinstance(attr_value, list):
                for sub in attr_value:
                    if hasattr(sub, 'dispose'):
                        sub.dispose()
            elif hasattr(attr_value, 'dispose'):
                attr_value.dispose()
    
    def __del__(self):
        """
        析构函数。
        用以防范场景对象未被正确释放的情况。
        """

        if not self.__quitted:
            self.quit()
                