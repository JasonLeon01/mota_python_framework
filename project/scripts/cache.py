import sys
import os
project_directory = os.getcwd()
sys.path.append(os.path.join(project_directory, 'custom_lib'))
import pygame

class Cache:
    def __init__(self, directory, prefix):
        self.cache = {}
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.png'):
                    full_path = os.path.join(root, file)
                    relative_path = os.path.relpath(full_path, directory)[:-4]
                    final_path = prefix + relative_path
                    self.cache[relative_path] = pygame.image.load(full_path)
