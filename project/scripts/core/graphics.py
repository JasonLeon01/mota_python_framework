from math import ceil
import os
import sys
from project.scripts.core.system import System
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Graphics:
    __sprite_group = []
    __surface_group = []
    __window_group = []
    __animation_group = []
    __frame_count = 0
    __freeze_Image = None
    canvas = pygame.Surface((640, 480))

    @classmethod
    def init(cls):
        cls.__sprite_group = []
        cls.__surface_group = []
        cls.__window_group = []
        cls.__animation_group = []
        cls.__frame_count = 0
        cls.__freeze_Image = None
        cls.canvas = pygame.Surface((640, 480))
        print('LOG: Graphics initialized.')
    
    @classmethod
    def add_window(cls, window):
        cls.__window_group.append(window)
        print('LOG: Window added.', window)

    @classmethod
    def remove_window(cls, window):
        cls.__window_group.remove(window)
        print('LOG: Window removed.', window)

    @classmethod
    def add_sprite(cls, sprite):
        cls.__sprite_group.append(sprite)
        print('LOG: Sprite added.', sprite)
        
    @classmethod
    def remove_sprite(cls, sprite):
        cls.__sprite_group.remove(sprite)
        print('LOG: Sprite removed.', sprite)
    
    @classmethod
    def add_surface(cls, surface):
        cls.__surface_group.append(surface)
        print('LOG: Surface added.', surface)
    
    @classmethod
    def remove_surface(cls, surface):
        cls.__surface_group.remove(surface)
        print('LOG: Surface removed.', surface)

    @classmethod
    def add_animation(cls, animation):
        cls.__animation_group.append(animation)
        print('LOG: Animation added.', animation)

    @classmethod
    def remove_animation(cls, animation):
        cls.__animation_group.remove(animation)
        print('LOG: Animation removed.', animation)

    @classmethod
    def frame_count(cls):
        return cls.__frame_count
        
    @classmethod
    def update(cls):
        for event in pygame.event.get():
            if System.running and event.type == pygame.QUIT:
                System.running = False
                System.scene.quit()
                return
            elif event.type == pygame.MOUSEWHEEL:
                if event.y != 0:
                    System.wheel = event.y
                    print('LOG: Mouse wheel event detected.', System.wheel)
            else:
                System.wheel = 0
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
        for animation in cls.__animation_group:
            animation.update()
        draw_surface = cls.canvas.copy()
        if cls.__freeze_Image is not None:
            draw_surface.blit(cls.__freeze_Image, (0, 0))
        System.canvas.blit(pygame.transform.smoothscale(draw_surface, System.get_size()), (0, 0))
        pygame.display.update()
        cls.__frame_count += 1
        System.clock.tick(System.frame_rate)

    @classmethod
    def freeze(cls):
        cls.__freeze_Image = cls.canvas.copy()

    @classmethod
    def transition(cls, time = 20):
        for i in range(time):
            cls.__freeze_Image.set_alpha(255 - ceil(255.0 / time) * i)
            cls.update()
        cls.__freeze_Image = None