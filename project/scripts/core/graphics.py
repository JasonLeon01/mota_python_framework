import os
import sys

from project.scripts.core.system import System

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Graphics:
    __sprite_group = []
    __surface_group = []
    __window_group = []
    canvas = pygame.Surface((640, 480))

    @classmethod
    def init(cls):
        cls.__sprite_group = []
        cls.__surface_group = []
        cls.__window_group = []
        cls.canvas = pygame.Surface((640, 480))
        print('LOG: Graphics initialized.')
    
    @classmethod
    def add_window(cls, window):
        cls.__window_group.append(window)
        print('LOG: Window added.')

    @classmethod
    def remove_window(cls, window):
        cls.__window_group.remove(window)
        print('LOG: Window removed.')

    @classmethod
    def add_sprite(cls, sprite):
        cls.__sprite_group.append(sprite)
        print('LOG: Sprite added.')
        
    @classmethod
    def remove_sprite(cls, sprite):
        cls.__sprite_group.remove(sprite)
        print('LOG: Sprite removed.')
    
    @classmethod
    def add_surface(cls, surface):
        cls.__surface_group.append(surface)
        print('LOG: Surface added.')
    
    @classmethod
    def remove_surface(cls, surface):
        cls.__surface_group.remove(surface)
        print('LOG: Surface removed.')
        
    @classmethod
    def update(cls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                System.running = False
                System.scene.quit()
                return
        import project.scripts.core.sprite as sprite
        import project.scripts.core.surface as surface
        total_count = len(cls.__window_group) + len(cls.__surface_group) + len(cls.__sprite_group)
        count, z = 0, 0
        System.canvas.fill((0, 0, 0, 0))
        cls.canvas.fill((0, 0, 0, 0))
        while count < total_count:
            for surface in cls.__surface_group:
                if surface.z == z:
                    surface.update()
                    count += 1
            for sprite in cls.__sprite_group:
                if sprite.z == z:
                    sprite.update()
                    count += 1
            for window in cls.__window_group:
                if window.z == z:
                    window.update()
                    count += 1
            z += 1
        System.canvas.blit(pygame.transform.scale(cls.canvas, System.get_size()), (0, 0))
        pygame.display.update()
        System.clock.tick(System.frame_rate)
