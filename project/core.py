import logging
from project.scripts.core.config import Config
from project.scripts.core.system import System
from project.scripts.core.cache import Cache
from project.scripts.core.graphics import Graphics


import project.scripts.scene.title as title

logging.info('Game launched successfully.')
System.scene = title.Scene()
while System.running and System.scene != None:
    System.scene.update()
System.scene = None
Graphics.transition()
logging.info('Game exited successfully.')
