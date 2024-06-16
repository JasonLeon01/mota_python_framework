import time
import sys
import os

from project.scripts.core.system import mota_system
from project.scripts.core.cache import mota_cache
from project.scripts.core.config import mota_config
from project.scripts.core.graphics import mota_graphics

if __name__ == '__main__':
    while mota_system.running:
        mota_graphics.update()
