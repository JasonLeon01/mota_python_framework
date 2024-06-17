import os
import sys

from project.scripts.core.system import mota_system

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Graphics:
    def __init__(self, system = mota_system):
        self.__system = system
        self.__sprite_group = []
        self.__surface_group = []
        self.canvas = pygame.Surface((640, 480))
    
    def add_sprite(self, sprite):
        self.__sprite_group.append(sprite)
        
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
                self.__system.scene.quit()
                return
        import project.scripts.core.sprite as sprite
        import project.scripts.core.surface as surface
        total_count = len(self.__surface_group) + len(self.__sprite_group)
        count, z = 0, 0
        self.__system.canvas.fill((0, 0, 0))
        self.canvas.fill((0, 0, 0))
        while count < total_count:
            for surface in self.__surface_group:
                if surface.z == z:
                    surface.update()
                    count += 1
            for sprite in self.__sprite_group:
                if sprite.z == z:
                    sprite.update()
                    count += 1
            z += 1
        self.__system.canvas.blit(pygame.transform.scale(self.canvas, self.__system.get_size()), (0, 0))
        pygame.display.update()
        self.__system.clock.tick(self.__system.frame_rate)

mota_graphics = Graphics()