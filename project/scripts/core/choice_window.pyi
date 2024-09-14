from project.scripts.core.window import Window

class ChoiceWindow(Window):
    """
    表示一个选择窗口。
    """

    def __init__(self, size: tuple[int, int], pos: tuple[int, int]) -> None:
        """
        初始化一个 ChoiceWindow 对象。

        参数:
        
            size (tuple[int, int]): ChoiceWindow 的大小。
            pos (tuple[int, int]): ChoiceWindow 的位置。
        """

        self.column: int
        """列数"""
        self.cursor_height: int
        """光标高度"""
        self.index: int
        """当前选项的索引"""
        self.items: int
        """选项总数"""
        self.is_active: bool
        """窗口是否处于激活状态"""
        pass

    def rows(self) -> int:
        """
        返回 ChoiceWindow 的行数。

        返回:

            int: ChoiceWindow 的行数。
        """
        pass

    def update_cursor_rect(self) -> None:
        """更新光标的矩形。"""
        pass

    def mouse_in_rect(self) -> bool:
        """
        判断鼠标是否在 ChoiceWindow 的矩形内。

        返回:

            bool: 如果鼠标在矩形内，则返回 True，否则返回 False。
        """
        pass

    def confirm(self) -> bool:
        """
        判定是否确认，含有鼠标点击和键盘触发两种情况。

        返回:

            bool: 如果确认，则返回 True，否则返回 False。
        """
        pass

    def cancel(self) -> bool:
        """
        判定是否取消，含有鼠标点击和键盘触发两种情况。

        返回:

            bool: 如果取消，则返回 True，否则返回 False。
        """
        pass

    def _key_response(self) -> None:
        """处理键盘输入，包括上下左右键，用于选择。"""
        pass

    def _mouse_response(self) -> None:
        """处理鼠标输入，包括鼠标滚轮，用于选择。"""
        pass

    def update(self) -> None:
        """
        更新 ChoiceWindow 对象。

        参数:

            dst (pygame.Surface): 目标画布。
        """
        pass
