from tkinter import messagebox
from project.scripts.core.config import Config
from project.scripts.core.system import System
from project.scripts.core.cache import Cache
from project.scripts.core.graphics import Graphics

Config.init(r'project\data\system\config.json')
System.init('mota.ini')
Cache.init(r'project\assets', '.png')
Graphics.init()

import project.scripts.scene.title as title

if __name__ == '__main__':
    print('LOG: Game launched successfully.')
    System.scene = title.Scene()
    while System.running and System.scene != None:
        System.scene.update()
    System.scene = None
    Graphics.transition()
    print('LOG: Game exited successfully.')
