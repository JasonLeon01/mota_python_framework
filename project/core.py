import time
import configparser
import project.scripts.config as config
import sys
import os
project_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_directory, 'custom_lib'))
import pygame

if __name__ == '__main__':
    iniconfig = configparser.ConfigParser()
    iniconfig.read('mota.ini')
    width, height = 640, 480
    width = int(width * iniconfig["Mota"].getfloat("resolution", 640))
    height = int(height * iniconfig["Mota"].getfloat("resolution", 480))
    title = iniconfig["Mota"].get("title", "Mota")

    pygame.init()
    icon = pygame.image.load('icon.ico')
    pygame.display.set_icon(icon)
    canvas = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    time.sleep(1)