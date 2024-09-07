import sys, os, logging
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Cache:
    """
    用于缓存游戏资源的类。
    
    属性:
    - __cache: 缓存字典。
    
    方法:
    - init(directory: str, prefix: str): 初始化缓存，并从指定目录加载图像。
    - get(part: str, file: str): 获取特定文件的缓存内容。
    - block(block_file: str): 从缓存中获取一个块。
    - character(character_file: str): 从缓存中获取一个角色。
    - enemy(enemy_file: str): 从缓存中获取一个敌人。
    - item(item_file: str): 从缓存中获取一个物品。
    - npc(npc_file: str): 从缓存中获取一个 NPC。
    - tileset(tileset_file: str): 从缓存中获取一个图块集。
    - system(system_file: str): 从缓存中获取一个系统文件。
    """
    
    __cache = {}

    @classmethod
    def init(cls, directory: str, prefix: str):
        """
        初始化缓存，并从指定目录加载图像。

        参数:
            directory (str): 图像所在的目录路径。
            prefix (str): 要加载的图像文件的前缀。
        """
        
        cls.__cache = {}
        # 遍历指定目录及其子目录中的所有文件
        for root, _, files in os.walk(directory):
            current_path = os.path.relpath(root, directory)
            if current_path != '.':
                current_dict_key = os.path.normpath(current_path).replace(os.sep, '/')
            else:
                current_dict_key = ''
            if current_dict_key not in cls.__cache:
                cls.__cache[current_dict_key] = {}
            # 加载符合前缀条件的图像文件并存入缓存
            for file in files:
                if file.endswith(prefix):
                    full_path = os.path.join(root, file)
                    file_without_ext = os.path.splitext(file)[0]
                    cls.__cache[current_dict_key][file_without_ext] = pygame.image.load(full_path)
                    logging.info('Loaded image: %s', full_path)
                
    @classmethod
    def get(cls, part: str, file: str):
        """
        获取特定文件的缓存内容。

        参数:
            part (str): 文件存储在缓存中的部分。
            file (str): 要获取的文件名。

        返回:
            object: 文件的缓存内容。

        异常:
            FileNotFoundError: 如果文件在缓存中不存在。
        """
        
        if isinstance(file, list):
            return [cls.get(part, f) for f in file]
        if file in cls.__cache[part]:
            return cls.__cache[part][file]
        else:
            raise FileNotFoundError(f"Error: The {part} file '{file}' does not exist.")
                
    @classmethod
    def block(cls, block_file: str):
        """
        从缓存中获取一个块。

        参数:
        - block_file: 块的文件名。

        返回:
        - 请求的块。
        """
        
        return cls.get('blocks', block_file)
    
    @classmethod
    def character(cls, character_file: str):
        """
        从缓存中获取一个角色。
        
        参数:
        - character_file: 角色的文件名。
        
        返回:
        - 请求的角色。
        """
        
        return cls.get('characters', character_file)
    
    @classmethod
    def enemy(cls, enemy_file: str):
        """
        从缓存中获取一个敌人。
        
        参数:
        - enemy_file: 敌人的文件名。
        
        返回:
        - 请求的敌人。
        """
        
        return cls.get('enemies', enemy_file)
    
    @classmethod
    def item(cls, item_file: str):
        """
        从缓存中获取一个物品。
        
        参数:
        - item_file: 物品的文件名。
        
        返回:
        - 请求的物品。
        """
        
        return cls.get('items', item_file)
    
    @classmethod
    def npc(cls, npc_file: str):
        """
        从缓存中获取一个 NPC。
        
        参数:
        - npc_file: NPC 的文件名。
        
        返回:
        - 请求的 NPC。
        """
        
        return cls.get('npcs', npc_file)
    
    @classmethod
    def tileset(cls, tileset_file: str):
        """
        从缓存中获取一个图块集。
        
        参数:
        - tileset_file: 图块集的文件名。
        
        返回:
        - 请求的图块集。
        """
        
        return cls.get('tilesets', tileset_file)

    @classmethod
    def system(cls, system_file: str):
        """
        从缓存中获取一个系统文件。
        
        参数:
        - system_file: 系统文件的文件名。
        
        返回:
        - 请求的系统文件。
        """
        
        return cls.get('system', system_file)