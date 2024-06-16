import os
import sys

from project.scripts.core.system import mota_system

project_directory = os.getcwd()
sys.path.append(os.path.join(project_directory, 'custom_lib'))
import pygame

class Graphics:
    def __init__(self, system = mota_system):
        self.__system = system
        self.__sprite_group = pygame.sprite.Group()
        self.__surface_group = []
    
    def add_sprite(self, sprite):
        self.__sprite_group.add(sprite)
        
    def remove_sprite(self, sprite):
        self.__sprite_group.remove(sprite)
    
    def add_surface(self, surface):
        self.__surface_group.append(surface)
        
    def remove_surface(self, surface):
        self.__surface_group.remove(surface)
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__system.running = False
                return
        import project.scripts.core.sprite as sprite
        import project.scripts.core.surface as surface
        total_count = len(self.__surface_group) + len(self.__sprite_group)
        count = 0
        self.__system.canvas.fill((0, 0, 0))
        canvas = pygame.Surface((640, 480))
        while count < total_count:
            for surface in self.__surface_group:
                if surface.z == count:
                    canvas.blit(surface, surface.get_pos())
                    count += 1
            for sprite in self.__sprite_group:
                if sprite.z == count:
                    canvas.blit(sprite.image, sprite.rect)
                    count += 1
        self.__system.canvas.blit(canvas, (0, 0))#(canvas.scale(__system.get_size()), (0, 0))
        pygame.display.flip()
        self.__system.clock.tick(self.__system.frame_rate)

mota_graphics = Graphics()