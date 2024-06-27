import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Audio:
    @classmethod
    def play_voice(cls, file):
        if file == '':
            return
        file = r'project\assets\voice\{}'.format(file)
        if not os.path.exists(file):
            raise FileNotFoundError(f'Voice file not found: {file}')
        pygame.mixer.Sound(file).play()

    @classmethod
    def play_music(cls, file):
        if file == '':
            return
        file = r'project\assets\music\{}'.format(file)
        if not os.path.exists(file):
            raise FileNotFoundError(f'Music file not found: {file}')
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)