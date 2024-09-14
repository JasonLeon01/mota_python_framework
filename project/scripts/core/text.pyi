from project.scripts.core.surface import Surface

class Text(Surface):
    """
    文本类。

    该类继承自Surface类，用于在画布上绘制文本。
    """

    def __init__(self, content: str, pos: tuple[int, int] = (0, 0), colour: tuple[int, int, int, int] = (255, 255, 255, 255)) -> None:
        """
        初始化一个文本对象。

        参数:

            content: 文本内容。
            pos: 文本的位置。默认为(0, 0)。
            colour: 文本的颜色。默认为白色。
        """

        self.__content: str
        """文本的内容"""
        
        self.__colour: tuple[int, int, int, int]
        """文本的颜色"""

        pass

    def refresh(self) -> None:
        """刷新文本内容。"""
        pass
        
    def get_content(self) -> str:
        """
        获取文本内容。

        返回:

            str: 文本内容。
        """
        pass

    def set_content(self, new_content: str) -> None:
        """
        设置新的文本内容。

        参数:

            new_content: 新的文本内容。
        """
        pass

    def get_colour(self) -> tuple[int, int, int, int]:
        """
        获取文本颜色。

        返回:

            tuple: 文本颜色。
        """
        pass
    
    def set_colour(self, new_colour: tuple[int, int, int, int]) -> None:
        """
        设置新的文本颜色。

        参数:

            new_colour: 新的文本颜色。
        """
        pass
        
    def set_font_style(self, new_font_style: Surface.FontStyle) -> None:
        """
        设置新的字体样式。

        参数:

            new_font_style: 新的字体样式。
        """
        pass
