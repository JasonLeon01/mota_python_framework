import project.scripts.core.choice_window as choice_window
import project.scripts.core.surface as surface

class CommandWindow(choice_window.ChoiceWindow):
    def __init__(self, width, commands):
        self.__commands = commands
        height = 32 * (len(self.__commands) + 1)
        super().__init__((width, height))
        self.items = len(self.__commands)
        self.contents = surface.Surface((width - 32, height - 32))
        self.refresh()

    def refresh(self):
        self.contents.clear()
        for i, command in enumerate(self.__commands):
            self.contents.draw_text(0, 32 * i, self.size[0] - 32, 32, command, 1)
