import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Input:
    keys_hash = {}
    @classmethod
    def press(cls, key):
        keys = pygame.key.get_pressed()
        return keys[key]
    
    @classmethod
    def trigger(cls, key):
        keys = pygame.key.get_pressed()
        if key not in cls.keys_hash:
            cls.keys_hash[key] = 0
        if keys[key]:
            cls.keys_hash[key] += 1
        else:
            cls.keys_hash[key] = 0
        if cls.keys_hash[key] == 1:
            return True
        return False
    
    @classmethod
    def repeat(cls, key, interval = 4):
        keys = pygame.key.get_pressed()
        if key not in cls.keys_hash:
            cls.keys_hash[key] = 0
        if keys[key]:
            cls.keys_hash[key] += 1
        else:
            cls.keys_hash[key] = 0
        if cls.keys_hash[key] % interval == 1:
            return True
        return False