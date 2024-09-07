import logging
import project.scripts.core.choice_window as choice_window
import project.scripts.core.surface as surface

class CommandWindow(choice_window.ChoiceWindow):
    """
    表示一个命令窗口。
    
    方法:
        __init__(width, commands): 初始化一个 CommandWindow 对象。
        refresh(): 刷新命令窗口。
    """
    
    def __init__(self, width, commands):
        """
        初始化一个 CommandWindow 对象。

        参数:
            width (int): 命令窗口的宽度。
            commands (list): 命令列表。
        """

        # 根据命令列表的长度计算窗口的高度
        self.__commands = commands
        height = 32 * (len(self.__commands) + 1)
        super().__init__((width, height))
        self.items = len(self.__commands)
        self.contents = surface.Surface((width - 32, height - 32))
        self.refresh()

    def refresh(self):
        """
        刷新命令窗口。
        
        属性:
            contents (Surface): 命令窗口的内容。
        """

        self.contents.clear()
        for i, command in enumerate(self.__commands):
            self.contents.draw_text(0, 32 * i, self.get_size()[0] - 32, 32, command, 1)
