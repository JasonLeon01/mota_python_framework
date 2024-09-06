import sys
import os
from project.scripts.core.system import System
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Audio:
    @classmethod
    def play_voice(cls, file: str):
        if file == '' or not System.is_voice_on:
            return
        file = r'project\assets\voices\{}'.format(file)
        if not os.path.exists(file):
            raise FileNotFoundError(f'Voice file not found: {file}')
        pygame.mixer.Sound(file).play()

    @classmethod
    def play_music(cls, file: str):
        if file == '' or not System.is_music_on:
            return
        file = r'project\assets\musics\{}'.format(file)
        if not os.path.exists(file):
            raise FileNotFoundError(f'Music file not found: {file}')
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)