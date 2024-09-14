import pygame

class Cache:
    """
    用于缓存游戏资源的类。
    """
    
    __cache: dict[str, dict[str, pygame.Surface]] # 缓存字典

    @classmethod
    def init(cls, directory: str, prefix: str) -> None:
        """
        初始化缓存，并从指定目录加载图像。
        参数:

            directory (str): 图像所在的目录路径。
            prefix (str): 要加载的图像文件的前缀。
        """
        ...

    @classmethod
    def get(cls, part: str, file: str) -> pygame.Surface:
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
        ...

    @classmethod
    def block(cls, block_file: str) -> pygame.Surface:
        """
        从缓存中获取一个块。

        参数:

            block_file: 块的文件名。

        返回:

            请求的块。
        """
        ...

    @classmethod
    def character(cls, character_file: str) -> pygame.Surface:
        """
        从缓存中获取一个角色。
        
        参数:

            character_file: 角色的文件名。
        
        返回:

            请求的角色。
        """
        ...

    @classmethod
    def enemy(cls, enemy_file: str) -> pygame.Surface:
        """
        从缓存中获取一个敌人。
        
        参数:

            enemy_file: 敌人的文件名。
        
        返回:

            请求的敌人。
        """
        ...

    @classmethod
    def item(cls, item_file: str) -> pygame.Surface:
        """
        从缓存中获取一个物品。
        
        参数:

            item_file: 物品的文件名。
        
        返回:

            请求的物品。
        """
        ...

    @classmethod
    def npc(cls, npc_file: str) -> pygame.Surface:
        """
        从缓存中获取一个 NPC。
        
        参数:

            npc_file: NPC 的文件名。
        
        返回:

            请求的 NPC。
        """
        ...

    @classmethod
    def tileset(cls, tileset_file: str) -> pygame.Surface:
        """
        从缓存中获取一个图块集。
        
        参数:

            tileset_file: 图块集的文件名。
        
        返回:

            请求的图块集。
        """
        ...

    @classmethod
    def system(cls, system_file: str) -> pygame.Surface:
        """
        从缓存中获取一个系统文件。
        
        参数:

            system_file: 系统文件的文件名。
        
        返回:

            请求的系统文件。
        """
        ...
