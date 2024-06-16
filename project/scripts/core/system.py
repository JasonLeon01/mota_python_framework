import configparser
import os
import sys

project_directory = os.getcwd()
sys.path.append(os.path.join(project_directory, 'custom_lib'))
import pygame

class System:
    def __init__(self, inifile):
        pygame.init()
        iniconfig = configparser.ConfigParser()
        iniconfig.read(inifile)
        self.__width, self.__height = 640, 480
        self.scale = iniconfig['Mota'].getfloat('Scale')
        self.__width = int(self.__width * self.scale)
        self.__height = int(self.__height * self.scale)
        self.canvas = pygame.display.set_mode((self.__width, self.__height))
        self.title = iniconfig['Mota'].get('title', 'Mota')
        pygame.display.set_caption(self.title)
        icon = pygame.image.load('icon.ico')
        pygame.display.set_icon(icon)
        self.running = True
        self.frame_rate = iniconfig['Mota'].getint('FrameRate')
        self.clock = pygame.time.Clock()
        self.bgm_on = True
        self.se_on = True
        self.scene = None
        
    def get_size(self):
        return self.__width, self.__height
    
    def change_scale(self, scale):
        self.scale = scale
        self.__width = int(640 * scale)
        self.__height = int(480 * scale)
        pygame.display.quit()
        self.canvas = pygame.display.set_mode(self.get_size())
        
mota_system = System('mota.ini')