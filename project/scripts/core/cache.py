import os, logging
import pygame

class Cache:
    __cache = {}

    @classmethod
    def init(cls, directory, prefix):
        cls.__cache = {}
        for root, _, files in os.walk(directory):
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
                    logging.info('Loaded image: %s', full_path)
                
    @classmethod
    def get(cls, part, file):
        if isinstance(file, list):
            return [cls.get(part, f) for f in file]
        if file in cls.__cache[part]:
            return cls.__cache[part][file]
        else:
            raise FileNotFoundError(f"Error: The {part} file '{file}' does not exist.")
                
    @classmethod
    def block(cls, block_file):
        return cls.get('blocks', block_file)
    
    @classmethod
    def character(cls, character_file):
        return cls.get('characters', character_file)
    
    @classmethod
    def enemy(cls, enemy_file):
        return cls.get('enemies', enemy_file)
    
    @classmethod
    def item(cls, item_file):
        return cls.get('items', item_file)
    
    @classmethod
    def npc(cls, npc_file):
        return cls.get('npcs', npc_file)
    
    @classmethod
    def tileset(cls, tileset_file):
        return cls.get('tilesets', tileset_file)

    @classmethod
    def system(cls, system_file):
        return cls.get('system', system_file)
