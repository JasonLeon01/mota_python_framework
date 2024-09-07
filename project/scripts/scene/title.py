"""
此脚本为标题场景脚本，用于处理标题场景的逻辑。
标题场景的内容会在读取title.json后自动处理，若在VS Code等IDE中看到红波浪线提示为正常现象。
其中，title.json为静态场景制作器自动生成，但是逻辑需要在update处自行设置。
"""

import logging
from project.scripts.core.system import System
from project.scripts.core.scene import Scene_Base
from project.scripts.core.audio import Audio
from project.scripts.core.config import Config

class Scene(Scene_Base):
    def __init__(self):
        self.load_data_from_json(__file__)
        super().__init__()
        Audio.play_music(Config.title_bgm)
        logging.info('Scene Title launched successfully.')
        
    def update(self):
        super().update()
        if self.window_command.confirm():
            if self.window_command.index == 0:
                Audio.play_voice(Config.decision_se)
            elif self.window_command.index == 1:
                Audio.play_voice(Config.decision_se)
            elif self.window_command.index == 2:
                Audio.play_voice(Config.decision_se)
                System.scene = None
            elif self.window_command.index == 3:
                Audio.play_voice(Config.decision_se)
