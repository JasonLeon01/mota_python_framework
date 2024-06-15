import time
import configparser
import project.scripts.config as config
import project.scripts.cache as cache
import sys
import os
project_directory = os.getcwd()
sys.path.append(os.path.join(project_directory, 'custom_lib'))
import pygame

motaConfig = config.Config()
motaCache = cache.Cache(r'project\assets', '.png')

if __name__ == '__main__':
    iniconfig = configparser.ConfigParser()
    iniconfig.read('mota.ini')
    width, height = 640, 480
    width = int(width * iniconfig['Mota'].getfloat('resolution', 640))
    height = int(height * iniconfig['Mota'].getfloat('resolution', 480))
    title = iniconfig["Mota"].get('title', 'Mota')

    pygame.init()
    icon = pygame.image.load('icon.ico')
    pygame.display.set_icon(icon)
    canvas = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    
    print(motaCache.cache)
    time.sleep(1)