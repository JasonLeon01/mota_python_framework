import os
import sys
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