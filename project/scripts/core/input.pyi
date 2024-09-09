class Input:
    """
    输入类。

    该类提供了一系列的方法，用于检查键盘和鼠标的输入。
        
    方法:

        press(key): 检查按键是否按下。
        trigger(key): 检查按键是否触发。
        repeat(key, interval): 检查按键是否重复。
        get_mouse_pos(): 获取鼠标位置。
        left_click(type, interval): 检查鼠标左键是否按下。
        right_click(type, interval): 检查鼠标右键是否按下。
        press_confirm(): 检查确认键是否按下。
        press_cancel(): 检查取消键是否按下。
        repeat_confirm(): 检查确认键是否重复。
        repeat_cancel(): 检查取消键是否重复。
        trigger_confirm(): 检查确认键是否触发。
        trigger_cancel(): 检查取消键是否触发。
        dir4(): 检查方向键。
        in_rect(rect): 检查鼠标是否在矩形内。
    """
    
    __keys_hash: dict[any, bool]
    """按键哈希表"""
    __keys_repeat: dict[any, int]
    """按键重复表"""
    
    @classmethod
    def press(cls, key: int) -> bool:
        """
        检查按键是否按下。
        
        参数:

            key: 键值。
        """
        pass

    @classmethod
    def trigger(cls, key: int) -> bool:
        """
        检查按键是否触发。

        该方法只会在按键按下的瞬间返回True，在松开之前不会再次返回True。
        
        参数:

            key: 键值。
        """
        pass

    @classmethod
    def repeat(cls, key: int, interval: int = 8) -> bool:
        """
        检查按键是否触发。

        该方法会间歇性地返回True。
        
        参数:

            key: 键值。
            interval: 重复间隔。
        """
        pass

    @classmethod
    def get_mouse_pos(cls) -> tuple[float, float]:
        """
        获取鼠标位置。

        该方法会返回一个元组，包含鼠标的x坐标和y坐标，且坐标会根据缩放比例进行转换。
        
        返回:

            鼠标的x坐标和y坐标。
        """
        pass

    @classmethod
    def left_click(cls, type: str = 'press', interval: int = 8) -> bool:
        """
        检查鼠标左键是否按下。
        
        参数:

            type: 检查类型。可选值有'press'、'trigger'和'repeat'。
            interval: 重复间隔。
            
        返回:

            bool: 是否按下。
        """
        pass

    @classmethod
    def right_click(cls, type: str = 'press', interval: int = 8) -> bool:
        """
        检查鼠标右键是否按下。
        
        参数:

            type: 检查类型。可选值有'press'、'trigger'和'repeat'。
            interval: 重复间隔。
        
        返回:

            bool: 是否按下。
        """
        pass

    @classmethod
    def press_confirm(cls) -> bool:
        """
        检查确认键是否按下。

        该方法会检查回车键和空格键。
        
        返回:

            bool: 是否按下。
        """
        pass

    @classmethod
    def press_cancel(cls) -> bool:
        """
        检查取消键是否按下。

        该方法会检查ESC键。
        
        返回:

            bool: 是否按下。
        """
        pass

    @classmethod
    def repeat_confirm(cls) -> bool:
        """
        检查确认键是否触发。

        该方法会检查回车键和空格键。
        
        返回:

            bool: 是否触发。
        """
        pass

    @classmethod
    def repeat_cancel(cls) -> bool:
        """
        检查取消键是否触发。

        该方法会检查ESC键。
        
        返回:

            bool: 是否触发。
        """
        pass

    @classmethod
    def trigger_confirm(cls) -> bool:
        """
        检查确认键是否触发。

        该方法会检查回车键和空格键。
        
        返回:

            bool: 是否触发。
        """
        pass

    @classmethod
    def trigger_cancel(cls) -> bool:
        """
        检查取消键是否触发。

        该方法会检查ESC键。
        
        返回:

            bool: 是否触发。
        """
        pass

    @classmethod
    def dir4(cls) -> int:
        """
        检查方向键。
        该方法会返回一个整数，代表方向。

        1: 下

        2: 左

        3: 右

        4: 上
        
        返回:

            int: 方向。
        """
        pass

    @classmethod
    def in_rect(cls, rect: tuple[int, int, int, int]) -> bool:
        """
        检查鼠标是否在矩形内。

        该方法会考虑到缩放比例。
        
        参数:

            rect: 矩形。
        
        返回:

            bool: 是否在矩形内。
        """
        pass

    @classmethod
    def __check_click_type(cls, type: str, key: int, pressed: bool, interval: int) -> bool:
        """
        检查鼠标点击。
        
        参数:

            type: 检查类型。
            key: 键值。
            pressed: 是否按下。
            interval: 重复间隔。
        """
        pass