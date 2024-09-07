import os
import sys
from project.scripts.core.system import System
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Input:
    """
    输入类。
    该类提供了一系列的方法，用于检查键盘和鼠标的输入。
    
    属性:
        __keys_hash: 按键哈希表。
        __keys_repeat: 按键重复表。
        
    方法:
        press: 检查按键是否按下。
        trigger: 检查按键是否触发。
        repeat: 检查按键是否重复。
        get_mouse_pos: 获取鼠标位置。
        left_click: 检查鼠标左键是否按下。
        right_click: 检查鼠标右键是否按下。
        press_confirm: 检查确认键是否按下。
        press_cancel: 检查取消键是否按下。
        repeat_confirm: 检查确认键是否重复。
        repeat_cancel: 检查取消键是否重复。
        trigger_confirm: 检查确认键是否触发。
        trigger_cancel: 检查取消键是否触发。
        dir4: 检查方向键。
        in_rect: 检查鼠标是否在矩形内。
    """
    
    __keys_hash = {}
    __keys_repeat = {}
    
    @classmethod
    def press(cls, key):
        """
        检查按键是否按下。
        
        参数:
            key: 键值。
        """
        
        keys = pygame.key.get_pressed()
        return keys[key]
    
    @classmethod
    def trigger(cls, key):
        """
        检查按键是否触发。
        该方法只会在按键按下的瞬间返回True，在松开之前不会再次返回True。
        
        参数:
            key: 键值。
        """
        
        if key not in cls.__keys_hash:
            cls.__keys_hash[key] = False
        keys = pygame.key.get_pressed()
        if cls.__keys_hash[key] and keys[key]:
            return False
        if keys[key]:
            cls.__keys_hash[key] = True
            return True
        cls.__keys_hash[key] = False
        return False
    
    @classmethod
    def repeat(cls, key, interval = 8):
        """
        检查按键是否触发。
        该方法会间歇性地返回True。
        
        参数:
            key: 键值。
            interval: 重复间隔。
        """
        
        keys = pygame.key.get_pressed()
        if keys[key]:
            if key not in cls.__keys_repeat:
                cls.__keys_repeat[key] = 0
                return True
            cls.__keys_repeat[key] += 1
        else:
            cls.__keys_repeat.pop(key, None)
            cls.__keys_hash[key] = False
        if key in cls.__keys_repeat and cls.__keys_repeat[key] > interval:
            cls.__keys_repeat[key] = 0
            return True
        return False
    
    @classmethod
    def get_mouse_pos(cls):
        """
        获取鼠标位置。
        该方法会返回一个元组，包含鼠标的x坐标和y坐标，且坐标会根据缩放比例进行转换。
        
        返回:
            鼠标的x坐标和y坐标。
        """
        
        x, y = pygame.mouse.get_pos()
        x /= System.get_scale()
        y /= System.get_scale()
        return x, y
    
    @classmethod
    def left_click(cls, type = 'press', interval = 8):
        """
        检查鼠标左键是否按下。
        
        参数:
            type: 检查类型。可选值有'press'、'trigger'和'repeat'。
            interval: 重复间隔。
            
        返回:
            bool: 是否按下。
        """
        
        return cls.__check_click_type(type, 0, pygame.mouse.get_pressed()[0], interval)
    
    @classmethod
    def right_click(cls, type = 'press', interval = 8):
        """
        检查鼠标右键是否按下。
        
        参数:
            type: 检查类型。可选值有'press'、'trigger'和'repeat'。
            interval: 重复间隔。
        
        返回:
            bool: 是否按下。
        """
        
        return cls.__check_click_type(type, 2, pygame.mouse.get_pressed()[2], interval)
    
    @classmethod
    def press_confirm(cls):
        """
        检查确认键是否按下。
        该方法会检查回车键和空格键。
        
        返回:
            bool: 是否按下。
        """

        return cls.press(pygame.K_RETURN) or cls.press(pygame.K_SPACE)
    
    @classmethod
    def press_cancel(cls):
        """
        检查取消键是否按下。
        该方法会检查ESC键。
        
        返回:
            bool: 是否按下。
        """

        return cls.press(pygame.K_ESCAPE)
    
    @classmethod
    def repeat_confirm(cls):
        """
        检查确认键是否触发。
        该方法会检查回车键和空格键。
        
        返回:
            bool: 是否触发。
        """

        return cls.repeat(pygame.K_RETURN) or cls.repeat(pygame.K_SPACE)
    
    @classmethod
    def repeat_cancel(cls):
        """
        检查取消键是否触发。
        该方法会检查ESC键。
        
        返回:
            bool: 是否触发。
        """

        return cls.repeat(pygame.K_ESCAPE)
    
    @classmethod
    def trigger_confirm(cls):
        """
        检查确认键是否触发。
        该方法会检查回车键和空格键。
        
        返回:
            bool: 是否触发。
        """

        return cls.trigger(pygame.K_RETURN) or cls.trigger(pygame.K_SPACE)
    
    @classmethod
    def trigger_cancel(cls):
        """
        检查取消键是否触发。
        该方法会检查ESC键。
        
        返回:
            bool: 是否触发。
        """

        return cls.trigger(pygame.K_ESCAPE)
    
    @classmethod
    def dir4(cls):
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

        if cls.repeat(pygame.K_DOWN):
            return 1
        elif cls.repeat(pygame.K_LEFT):
            return 2
        elif cls.repeat(pygame.K_RIGHT):
            return 3
        elif cls.repeat(pygame.K_UP):
            return 4
        return 0
    
    @classmethod
    def in_rect(cls, rect):
        """
        检查鼠标是否在矩形内。
        该方法会考虑到缩放比例。
        
        参数:
            rect: 矩形。
        
        返回:
            bool: 是否在矩形内。
        """

        x, y = pygame.mouse.get_pos()
        x /= System.get_scale()
        y /= System.get_scale()
        rect_x, rect_y, rect_width, rect_height = rect
        if x > rect_x and x < rect_x + rect_width and y > rect_y and y < rect_y + rect_height:
            return True
        return False
    
    @classmethod
    def __check_click_type(cls, type, key, pressed, interval):
        """
        检查鼠标点击。
        
        参数:
            type: 检查类型。
            key: 键值。
            pressed: 是否按下。
            interval: 重复间隔。
        """

        if type == 'press':
            return pressed
        elif type == 'trigger':
            if key not in cls.__keys_hash:
                cls.__keys_hash[key] = False
            if cls.__keys_hash[key] and pressed:
                return False
            if pressed:
                cls.__keys_hash[key] = True
                return True
            cls.__keys_hash[key] = False
            return False
        elif type == 'repeat':
            if pressed:
                if key not in cls.__keys_repeat:
                    cls.__keys_repeat[key] = 0
                    return True
                cls.__keys_repeat[key] += 1
            else:
                cls.__keys_repeat.pop(key, None)
                cls.__keys_hash[key] = False
            if key in cls.__keys_repeat and cls.__keys_repeat[key] > interval:
                cls.__keys_repeat[key] = 0
                return True
            return False
        return False
