import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Cache:
    __cache = {}

    @classmethod
    def init(cls, directory, prefix):
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
                if file.endswith('.png'):
                    full_path = os.path.join(root, file)
                    file_without_ext = os.path.splitext(file)[0]
                    cls.__cache[current_dict_key][file_without_ext] = pygame.image.load(full_path)
                    print(f'LOG: Loaded image: {full_path}')
                
    @classmethod
    def block(cls, block_file):
        if isinstance(block_file, list):
            return [cls.block(block) for block in block_file]
        if block_file in cls.__cache['blocks']:
            return cls.__cache['blocks'][block_file]
        else:
            raise FileNotFoundError(f"Error: The block file '{block_file}' does not exist.")
    
    @classmethod
    def character(cls, character_file):
        if isinstance(character_file, list):
            return [cls.character(character) for character in character_file]
        if character_file in cls.__cache['characters']:
            return cls.__cache['characters'][character_file]
        else:
            raise FileNotFoundError(f"Error: The character file '{character_file}' does not exist.")
    
    @classmethod
    def enemy(cls, enemy_file):
        if isinstance(enemy_file, list):
            return [cls.enemy(enemy) for enemy in enemy_file]
        if enemy_file in cls.__cache['enemies']:
            return cls.__cache['enemies'][enemy_file]
        else:
            raise FileNotFoundError(f"Error: The enemy file '{enemy_file}' does not exist.")
    
    @classmethod
    def item(cls, item_file):
        if isinstance(item_file, list):
            return [cls.item(item) for item in item_file]
        if item_file in cls.__cache['items']:
            return cls.__cache['items'][item_file]
        else:
            raise FileNotFoundError(f"Error: The item file '{item_file}' does not exist.")
    
    @classmethod
    def npc(cls, npc_file):
        if isinstance(npc_file, list):
            return [cls.npc(npc) for npc in npc_file]
        if npc_file in cls.__cache['npcs']:
            return cls.__cache['npcs'][npc_file]
        else:
            raise FileNotFoundError(f"Error: The NPC file '{npc_file}' does not exist.")
    
    @classmethod
    def tileset(cls, tileset_file):
        if isinstance(tileset_file, list):
            return [cls.tileset(tileset) for tileset in tileset_file]
        if tileset_file in cls.__cache['tilesets']:
            return cls.__cache['tilesets'][tileset_file]
        else:
            raise FileNotFoundError(f"Error: The tileset file '{tileset_file}' does not exist.")

    @classmethod
    def system(cls, system_file):
        if isinstance(system_file, list):
            return [cls.system(system) for system in system_file]
        if system_file in cls.__cache['system']:
            return cls.__cache['system'][system_file]
        else:
            raise FileNotFoundError(f"Error: The system file '{system_file}' does not exist.")
