import configparser
import logging
import os
import sys
from project.scripts.core.config import Config
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class System:
    """
    系统类。
    该类提供了系统的基本属性和方法。
    
    属性:
        __width: 窗口宽度。
        __height: 窗口高度。
        __scale: 窗口缩放比例。
        canvas: 窗口画布。
        title: 窗口标题。
        font: 窗口字体。
        frame_rate: 窗口帧率。
        running: 窗口运行标志。
        clock: 窗口时钟。
        is_music_on: 音乐开关。
        is_voice_on: 音效开关。
        scene: 场景对象。
        wheel: 鼠标滚轮值。
        variables: 系统变量。
    
    方法:
        init: 初始化系统的基本属性。
        get_size: 获取窗口尺寸。
        get_scale: 获取窗口缩放比例。
        change_scale: 更改窗口缩放比例。
        get_variable: 获取系统变量。
    """
    
    __width = None
    __height = None
    __scale = None
    __width = None
    __height = None
    canvas = None
    title = None
    font = None
    frame_rate = None
    running = None
    clock = None
    is_music_on = None
    is_voice_on = None
    scene = None
    wheel = 0

    variables = {}

    @classmethod
    def init(cls, inifile: str):
        """
        初始化系统的基本属性。
        
        参数:
            inifile (str): INI文件路径。
            
        属性:
            __width: 窗口宽度。
            __height: 窗口高度。
            __scale: 窗口缩放比例。
            canvas: 窗口画布。
            title: 窗口标题。
            font: 窗口字体。
            frame_rate: 窗口帧率。
            running: 窗口运行标志。
            clock: 窗口时钟。
            is_music_on: 音乐开关。
            is_voice_on: 音效开关。
            scene: 场景对象。
            wheel: 鼠标滚轮值。
            variables: 系统变量。
        """
        
        pygame.init()
        iniconfig = configparser.ConfigParser()
        iniconfig.read(inifile)
        cls.__width, cls.__height = 640, 480
        cls.__scale = iniconfig['Mota'].getfloat('Scale')
        cls.__width = int(cls.__width * cls.__scale)
        cls.__height = int(cls.__height * cls.__scale)
        cls.canvas = pygame.display.set_mode((cls.__width, cls.__height), pygame.DOUBLEBUF | pygame.HWSURFACE)
        cls.title = iniconfig['Mota'].get('title', 'Mota')
        pygame.display.set_caption(cls.title)
        icon = pygame.image.load('icon.ico')
        pygame.display.set_icon(icon)
        cls.font = pygame.font.Font((r'project\assets\fonts\{}'.format(Config.font_name)), 22)
        cls.frame_rate = iniconfig['Mota'].getint('FrameRate')
        cls.running = True
        cls.clock = pygame.time.Clock()
        cls.is_music_on = True
        cls.is_voice_on = True
        cls.scene = None
        cls.wheel = 0

        cls.variables = {}
        logging.info('System initialized.')
        
    @classmethod
    def get_size(cls):
        """
        获取窗口尺寸。
        
        返回:
            tuple: 窗口尺寸。
        """

        return cls.__width, cls.__height
    
    @classmethod
    def get_scale(cls):
        """
        获取窗口缩放比例。
        
        返回:
            float: 窗口缩放比例。
        """

        return cls.__scale
    
    @classmethod
    def change_scale(cls, scale: float):
        """
        更改窗口缩放比例。
        
        参数:
            scale (float): 缩放比例。
        """

        cls.__scale = scale
        cls.__width = int(640 * scale)
        cls.__height = int(480 * scale)
        pygame.display.quit()
        cls.canvas = pygame.display.set_mode(cls.get_size())
        logging.info('System scale changed. %s', cls.__scale)

    @classmethod
    def get_variable(cls, name):
        """
        获取系统变量。
        
        参数:
            name (str): 变量名。
        """

        if name in cls.variables:
            return cls.variables[name]
        return 0