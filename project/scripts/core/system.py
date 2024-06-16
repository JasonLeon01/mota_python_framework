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
        self.resolution = iniconfig['Mota'].getfloat('resolution')
        self.__width = int(self.__width * self.resolution)
        self.__height = int(self.__height * self.resolution)
        self.canvas = pygame.display.set_mode((self.__width, self.__height))
        self.title = iniconfig['Mota'].get('title', 'Mota')
        pygame.display.set_caption(self.title)
        icon = pygame.image.load('icon.ico')
        pygame.display.set_icon(icon)
        self.bgm_on = True
        self.se_on = True
        self.scene = None
        
    def get_size(self):
        return self.__width, self.__height
    
    def change_resolution(self, resolution):
        self.resolution = resolution
        self.__width = int(640 * resolution)
        self.__height = int(480 * resolution)
        
mota_system = System('mota.ini')