import time
import sys
import os

from project.scripts.core.system import mota_system

import project.scripts.core.scene as scene_base
import project.scripts.scene.title as title


if __name__ == '__main__':
    print('LOG: Game launched successfully.')
    mota_system.scene = title.Scene()
    while mota_system.running and mota_system.scene != None:
        mota_system.scene.update()
    mota_system.scene = None