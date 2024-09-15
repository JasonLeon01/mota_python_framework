import configparser, logging
from project.scripts.core.config import Config
import pygame

class System:
    __width = 640
    __height = 480
    __scale = 1.0
    canvas = None
    title = ""
    font = None
    frame_rate = 30
    default_font_size = 22
    running = False
    clock = None
    is_music_on = True
    is_voice_on = True
    scene = None
    wheel = 0
    default_viewport = None

    @classmethod
    def init(cls, inifile):
        pygame.init()
        iniconfig = configparser.ConfigParser()
        iniconfig.read(inifile)
        cls.default_viewport = pygame.Surface((cls.__width, cls.__height))
        cls.__scale = iniconfig['Mota'].getfloat('Scale')
        cls.canvas = pygame.display.set_mode((cls.__width * cls.__scale, cls.__height * cls.__scale), pygame.DOUBLEBUF | pygame.HWSURFACE)
        cls.title = iniconfig['Mota'].get('title', 'Mota')
        pygame.display.set_caption(cls.title)
        icon = pygame.image.load('icon.ico')
        pygame.display.set_icon(icon)
        cls.fonts = {}
        for i in range(12, 49):
            cls.fonts[i] = pygame.font.Font((r'project\assets\fonts\{}'.format(Config.font_name)), i)
        cls.frame_rate = iniconfig['Mota'].getint('FrameRate')
        cls.default_font_size = iniconfig['Mota'].getint('FontSize')
        cls.running = True
        cls.clock = pygame.time.Clock()
        cls.is_music_on = True
        cls.is_voice_on = True
        cls.scene = None
        cls.wheel = 0
        logging.info('System initialized.')
        
    @classmethod
    def get_size(cls):
        return cls.__width, cls.__height
    
    @classmethod
    def get_scale(cls):
        return cls.__scale
    
    @classmethod
    def change_scale(cls, scale):
        cls.__scale = scale
        cls.__width = int(640 * scale)
        cls.__height = int(480 * scale)
        pygame.display.quit()
        cls.canvas = pygame.display.set_mode(cls.get_size())
        logging.info('System scale changed. %s', cls.__scale)

    @classmethod
    def get_variable(cls, name):
        if name in cls.variables:
            return cls.variables[name]
        return 0