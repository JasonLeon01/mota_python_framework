import configparser
import os
import sys

from project.scripts.core.config import Config
Config.init(r'project\data\system\config.json')

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class System:
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
    bgm_on = None
    se_on = None
    scene = None
    wheel = 0

    @classmethod
    def init(cls, inifile):
        pygame.init()
        iniconfig = configparser.ConfigParser()
        iniconfig.read(inifile)
        cls.__width, cls.__height = 640, 480
        cls.__scale = iniconfig['Mota'].getfloat('Scale')
        cls.__width = int(cls.__width * cls.__scale)
        cls.__height = int(cls.__height * cls.__scale)
        cls.canvas = pygame.display.set_mode((cls.__width, cls.__height))
        cls.title = iniconfig['Mota'].get('title', 'Mota')
        pygame.display.set_caption(cls.title)
        icon = pygame.image.load('icon.ico')
        pygame.display.set_icon(icon)
        cls.font = pygame.font.Font((r'project\assets\fonts\{}'.format(Config.font_name)), 22)
        cls.frame_rate = iniconfig['Mota'].getint('FrameRate')
        cls.running = True
        cls.clock = pygame.time.Clock()
        cls.bgm_on = True
        cls.se_on = True
        cls.scene = None
        cls.wheel = 0
        print('LOG: System initialized.')
        
    @classmethod
    def get_size(cls):
        return cls.__width, cls.__height
    
    @classmethod
    def change_scale(cls, scale):
        cls.__scale = scale
        cls.__width = int(640 * scale)
        cls.__height = int(480 * scale)
        pygame.display.quit()
        cls.canvas = pygame.display.set_mode(cls.get_size())
        print('LOG: System scale changed.')
