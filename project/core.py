import sys, os, logging
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
from project.scripts.core.config import Config
from project.scripts.core.system import System
from project.scripts.core.viewport import ViewportManager
from project.scripts.core.cache import Cache
from project.scripts.core.graphics import Graphics

Config.init(r'project\data\config.json')
System.init('mota.ini')
ViewportManager.init()
Cache.init(r'project\assets', '.png')
Graphics.init()

logging.info('Game launched successfully. %s', System.title)
import project.scripts.scene.title as title
System.scene = title.Scene()
while System.running and System.scene is not None:
    System.scene.update()
System.scene = None
Graphics.transition()
logging.info('Game exited successfully. %s', System.title)
