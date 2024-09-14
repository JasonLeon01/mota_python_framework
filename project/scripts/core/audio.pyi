import pygame

class Audio:
    """
    播放音频文件。
    """
    
    @classmethod
    def play_voice(cls, file: str) -> None:
        """
        播放声音文件。

        参数:
        
            file (str): 要播放的声音文件的名称。

        异常:
        
            FileNotFoundError: 如果未找到声音文件。
        """
        pass

    @classmethod
    def play_music(cls, file: str) -> None:
        """
        播放指定的音乐文件。

        参数:
        
            file (str): 要播放的音乐文件的名称。

        异常:
        
            FileNotFoundError: 如果未找到指定的音乐文件。
        """
        pass
