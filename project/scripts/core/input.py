import os
import sys
from project.scripts.core.system import System
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Input:
    __keys_hash = {}
    __keys_repeat = {}
    @classmethod
    def press(cls, key):
        keys = pygame.key.get_pressed()
        return keys[key]
    
    @classmethod
    def trigger(cls, key):
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
        x, y = pygame.mouse.get_pos()
        x /= System.get_scale()
        y /= System.get_scale()
        return x, y
    
    @classmethod
    def left_click(cls, type = 'press', interval = 8):
        return cls.__check_click_type(type, 0, pygame.mouse.get_pressed()[0], interval)
    
    @classmethod
    def right_click(cls, type = 'press', interval = 8):
        return cls.__check_click_type(type, 2, pygame.mouse.get_pressed()[2], interval)
    
    @classmethod
    def press_confirm(cls):
        return cls.press(pygame.K_RETURN) or cls.press(pygame.K_SPACE)
    
    @classmethod
    def press_cancel(cls):
        return cls.press(pygame.K_ESCAPE)
    
    @classmethod
    def repeat_confirm(cls):
        return cls.repeat(pygame.K_RETURN) or cls.repeat(pygame.K_SPACE)
    
    @classmethod
    def repeat_cancel(cls):
        return cls.repeat(pygame.K_ESCAPE)
    
    @classmethod
    def trigger_confirm(cls):
        return cls.trigger(pygame.K_RETURN) or cls.trigger(pygame.K_SPACE)
    
    @classmethod
    def trigger_cancel(cls):
        return cls.trigger(pygame.K_ESCAPE)
    
    @classmethod
    def dir4(cls):
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
        x, y = pygame.mouse.get_pos()
        x /= System.get_scale()
        y /= System.get_scale()
        rect_x, rect_y, rect_width, rect_height = rect
        if x > rect_x and x < rect_x + rect_width and y > rect_y and y < rect_y + rect_height:
            return True
        return False
    
    @classmethod
    def __check_click_type(cls, type, key, pressed, interval):
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
