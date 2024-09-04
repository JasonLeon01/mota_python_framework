import sys
import os
import logging
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Cache:
    __cache = {}

    @classmethod
    def init(cls, directory: str, prefix: str):
        cls.__cache = {}
        for root, dirs, files in os.walk(directory):
            current_path = os.path.relpath(root, directory)
            if current_path != '.':
                current_dict_key = os.path.normpath(current_path).replace(os.sep, '/')
            else:
                current_dict_key = ''
            if current_dict_key not in cls.__cache:
                cls.__cache[current_dict_key] = {}
            for file in files:
                if file.endswith(prefix):
                    full_path = os.path.join(root, file)
                    file_without_ext = os.path.splitext(file)[0]
                    cls.__cache[current_dict_key][file_without_ext] = pygame.image.load(full_path)
                    logging.info(f' Loaded image: {full_path}')
                
    @classmethod
    def get(cls, part: str, file: str):
        if isinstance(file, list):
            return [cls.get(part, f) for f in file]
        if file in cls.__cache[part]:
            return cls.__cache[part][file]
        else:
            raise FileNotFoundError(f"Error: The {part} file '{file}' does not exist.")
                
    @classmethod
    def block(cls, block_file: str):
        return cls.get('blocks', block_file)
    
    @classmethod
    def character(cls, character_file: str):
        return cls.get('characters', character_file)
    
    @classmethod
    def enemy(cls, enemy_file: str):
        return cls.get('enemies', enemy_file)
    
    @classmethod
    def item(cls, item_file: str):
        return cls.get('items', item_file)
    
    @classmethod
    def npc(cls, npc_file: str):
        return cls.get('npcs', npc_file)
    
    @classmethod
    def tileset(cls, tileset_file: str):
        return cls.get('tilesets', tileset_file)

    @classmethod
    def system(cls, system_file: str):
        return cls.get('system', system_file)
