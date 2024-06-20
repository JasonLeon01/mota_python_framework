import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Cache:
    def __init__(self, directory, prefix):
        self.__cache = {}
        for root, dirs, files in os.walk(directory):
            current_path = os.path.relpath(root, directory)
            if current_path != '.':
                current_dict_key = os.path.normpath(current_path).replace(os.sep, '/')
            else:
                current_dict_key = ''
            if current_dict_key not in self.__cache:
                self.__cache[current_dict_key] = {}
            for file in files:
                if file.endswith('.png'):
                    full_path = os.path.join(root, file)
                    file_without_ext = os.path.splitext(file)[0]
                    self.__cache[current_dict_key][file_without_ext] = pygame.image.load(full_path)
                    print(f'LOG: Loaded image: {full_path}')
                
    def block(self, block_file):
        if isinstance(block_file, list):
            return [self.block(block) for block in block_file]
        if block_file in self.__cache['blocks']:
            return self.__cache['blocks'][block_file]
        else:
            raise ValueError(f"Error: The block file '{block_file}' does not exist.")
            sys.exit(1)
                    
    def character(self, character_file):
        if isinstance(character_file, list):
            return [self.character(character) for character in character_file]
        if character_file in self.__cache['characters']:
            return self.__cache['characters'][character_file]
        else:
            raise ValueError(f"Error: The character file '{character_file}' does not exist.")
            sys.exit(1)
    
    def enemy(self, enemy_file):
        if isinstance(enemy_file, list):
            return [self.enemy(enemy) for enemy in enemy_file]
        if enemy_file in self.__cache['enemies']:
            return self.__cache['enemies'][enemy_file]
        else:
            raise ValueError(f"Error: The enemy file '{enemy_file}' does not exist.")
            sys.exit(1)
    
    def item(self, item_file):
        if isinstance(item_file, list):
            return [self.item(item) for item in item_file]
        if item_file in self.__cache['items']:
            return self.__cache['items'][item_file]
        else:
            raise ValueError(f"Error: The item file '{item_file}' does not exist.")
            sys.exit(1)
    
    def npc(self, npc_file):
        if isinstance(npc_file, list):
            return [self.npc(npc) for npc in npc_file]
        if npc_file in self.__cache['npcs']:
            return self.__cache['npcs'][npc_file]
        else:
            raise ValueError(f"Error: The NPC file '{npc_file}' does not exist.")
            sys.exit(1)
    
    def tileset(self, tileset_file):
        if isinstance(tileset_file, list):
            return [self.tileset(tileset) for tileset in tileset_file]
        if tileset_file in self.__cache['tilesets']:
            return self.__cache['tilesets'][tileset_file]
        else:
            raise ValueError(f"Error: The tileset file '{tileset_file}' does not exist.")
            sys.exit(1)
            
    def system(self, system_file):
        if isinstance(system_file, list):
            return [self.system(system) for system in system_file]
        if system_file in self.__cache['system']:
            return self.__cache['system'][system_file]
        else:
            raise ValueError(f"Error: The system file '{system_file}' does not exist.")
            sys.exit(1)
            
mota_cache = Cache(r'project\assets', '.png')