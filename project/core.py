from tkinter import messagebox
from project.scripts.core.config import Config
Config.init(r'project\data\system\config.json')
from project.scripts.core.system import System
System.init('mota.ini')
from project.scripts.core.cache import Cache
Cache.init(r'project\assets', '.png')
from project.scripts.core.graphics import Graphics
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