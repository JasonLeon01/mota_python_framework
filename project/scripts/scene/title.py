import logging
from project.scripts.core.system import System
from project.scripts.core.scene import Scene_Base

class Scene(Scene_Base):
    def __init__(self):
        self.load_data_from_json(__file__)
        super().__init__()
        logging.info('Scene Title launched successfully.')
        
    def update(self):
        super().update()
        if self.window_command.confirm():
            if self.window_command.index == 0:
                pass
            elif self.window_command.index == 1:
                pass
            elif self.window_command.index == 2:
                System.scene = None
