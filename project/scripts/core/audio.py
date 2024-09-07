import sys, os
from project.scripts.core.system import System
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Audio:
    """
    播放音频文件。
    方法:
        play_voice(cls, file: str): 播放语音文件。
        play_music(cls, file: str): 播放指定的音乐文件。
    """
    
    @classmethod
    def play_voice(cls, file: str):
        """
        播放声音文件。

        参数:
            file (str): 要播放的声音文件的名称。

        异常:
            FileNotFoundError: 如果未找到声音文件。
        """
        
        if file == '' or not System.is_voice_on:
            return
        file = r'project\assets\voices\{}'.format(file)
        if not os.path.exists(file):
            raise FileNotFoundError(f'Voice file not found: {file}')
        pygame.mixer.Sound(file).play()

    @classmethod
    def play_music(cls, file: str):
        """
        播放指定的音乐文件。

        参数:
            file (str): 要播放的音乐文件的名称。

        异常:
            FileNotFoundError: 如果未找到指定的音乐文件。
        """
        
        if file == '' or not System.is_music_on:
            return
        file = r'project\assets\musics\{}'.format(file)
        if not os.path.exists(file):
            raise FileNotFoundError(f'Music file not found: {file}')
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
