from math import ceil
import os, psutil, logging, datetime
from project.scripts.core.system import System
from project.scripts.core.viewport import ViewportManager
import pygame
import pygame.freetype

class Graphics:
    __animation_group = []
    __frame_count = 0
    __freeze_Image = None
    __last_frame_time = 0
    __total_time = 0

    @classmethod
    def init(cls):
        cls.__animation_group = []
        cls.__frame_count = 0
        cls.__freeze_Image = None
        cls.__last_frame_time = datetime.datetime.now()
        cls.__debug_font = pygame.freetype.Font(System.font.path, 12)
        logging.info('Graphics initialized.')
    
    @classmethod
    def add_animation(cls, animation):
        cls.__animation_group.append(animation)
        logging.info('Animation added. %s', animation)

    @classmethod
    def remove_animation(cls, animation):
        cls.__animation_group.remove(animation)
        logging.info('Animation removed. %s', animation)

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
                    logging.info('Mouse wheel event detected. %s', System.wheel)
            else:
                System.wheel = 0
        
        System.canvas.fill((0, 0, 0, 0))
        ViewportManager.update()
        
        for animation in cls.__animation_group:
            animation.update()
            if animation.has_reach_end():
                if animation.loop:
                    animation.reset()
                else:
                    cls.remove_animation(animation)

        if cls.__freeze_Image is not None:
            System.default_viewport.blit(cls.__freeze_Image, (0, 0))
        
        if os.environ.get('DEBUG') == 'True':
            cls.debug_info(System.default_viewport)
        
        width, height = System.get_size()
        System.canvas.blit(pygame.transform.smoothscale(System.default_viewport, (width * System.get_scale(), height * System.get_scale())), (0, 0))
        pygame.display.flip()
        cls.__frame_count += 1
        System.clock.tick(System.frame_rate)

    @classmethod
    def debug_info(cls, draw_surface):
        now_time = datetime.datetime.now()
        delta_time = now_time - cls.__last_frame_time
        cls.__last_frame_time = now_time
        cls.__total_time += delta_time.total_seconds()
        cls.__debug_font.render_to(draw_surface, (0, 0), f'FPS: {1.0 / delta_time.total_seconds():.2f}', (255, 255, 255))
        cls.__debug_font.render_to(draw_surface, (0, 16), f'Average FPS: {cls.__frame_count / cls.__total_time:.2f}', (255, 255, 255))
        process = psutil.Process()
        cls.__debug_font.render_to(draw_surface, (0, 32), f'Memory Usage: {process.memory_info().rss / (1024 * 1024):.2f}MB', (255, 255, 255))

    @classmethod
    def freeze(cls):
        cls.__freeze_Image = System.default_viewport.copy()

    @classmethod
    def transition(cls, time=20):
        for i in range(time):
            cls.__freeze_Image.set_alpha(255 - ceil(255.0 / time) * i)
            cls.update()
        cls.__freeze_Image = None
