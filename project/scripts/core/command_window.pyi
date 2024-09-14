from typing import List, Tuple
import project.scripts.core.choice_window as choice_window
import pygame

class CommandWindow(choice_window.ChoiceWindow):
    """
    表示一个命令窗口。
    """

    def __init__(self, width: int, commands: List[str], pos: Tuple[int, int]) -> None:
        """
        初始化一个 CommandWindow 对象。

        参数:
          width (int): 命令窗口的宽度。
          commands (List[str]): 命令列表。
          pos (Tuple[int, int]): 命令窗口的位置。
        """
        pass

    def refresh(self) -> None:
        """
        刷新命令窗口。

        属性:
          contents (surface.Surface): 命令窗口的内容。
        """
        pass