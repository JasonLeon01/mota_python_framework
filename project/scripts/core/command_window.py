from project.scripts.core.choice_window import ChoiceWindow
from project.scripts.core.surface import Surface
from project.scripts.core.system import System

class CommandWindow(ChoiceWindow):
    def __init__(self, width, commands, pos=(0, 0), viewport = None):
        self.__commands = commands
        height = 32 * (len(self.__commands) + 1)
        super().__init__((width, height), pos, viewport)
        self.items = len(self.__commands)
        self.contents = Surface((width - 32, height - 32))
        self.refresh()

    def refresh(self):
        self.contents.clear()
        for i, command in enumerate(self.__commands):
            self.contents.draw_text(0, 32 * i, self.get_size()[0] - 32, 32, command, 1)
