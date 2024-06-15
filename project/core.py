import time
import configparser
import project.scripts.config
import sys
import os
project_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_directory, 'custom_lib'))

iniconfig = configparser.ConfigParser()
iniconfig.read('mota.ini')
width, height = 640, 480
width = int(width * iniconfig["Mota"].getfloat("resolution", 640))
height = int(height * iniconfig["Mota"].getfloat("resolution", 480))
title = iniconfig["Mota"].get("title", "Mota")

print("Initializing pygame...")
time.sleep(1)