import logging
from project.scripts.core.system import System

class ViewportManager():
    _viewport_dictionary = {}

    @classmethod
    def init(cls):
        from project.scripts.core.surface import Surface
        cls._viewport_dictionary[id(None)] = Surface((System.get_size()), (0, 0))

    @classmethod
    def add_viewport(cls, viewport):
        cls._viewport_dictionary[id(viewport)] = viewport
        logging.info('Viewport added. %s', viewport)
    
    @classmethod
    def remove_viewport(cls, viewport):
        cls._viewport_dictionary.pop(id(viewport))
        logging.info('Viewport removed. %s', viewport)

    @classmethod
    def add_sprite(cls, sprite, viewport = None):
        if id(viewport) in cls._viewport_dictionary:
            cls._viewport_dictionary[id(viewport)].add_sprite(sprite)
        else:
            logging.info('Viewport not found and will be created %s', viewport)
            cls.add_viewport(viewport)
            cls.add_sprite(sprite)
    
    @classmethod
    def remove_sprite(cls, sprite, viewport = None):
        if id(viewport) in cls._viewport_dictionary:
            cls._viewport_dictionary[id(viewport)].remove_sprite(sprite)
        else:
            logging.info('Viewport not found in viewport dictionary %s', viewport)

    @classmethod
    def add_surface(cls, surface, viewport = None):
        if id(viewport) in cls._viewport_dictionary:
            cls._viewport_dictionary[id(viewport)].add_surface(surface)
        else:
            logging.info('Viewport not found and will be created %s', viewport)
            cls.add_viewport(viewport)
            cls.add_surface(surface)

    @classmethod
    def remove_surface(cls, surface, viewport = None):
        if id(viewport) in cls._viewport_dictionary:
            cls._viewport_dictionary[id(viewport)].remove_surface(surface)
        else:
            logging.info('Viewport not found in get_viewport() dictionary %s', viewport)

    @classmethod
    def update(cls):
        total_count = len(cls._viewport_dictionary)
        count, z = 0, 0
        System.default_viewport.fill((0, 0, 0, 0))
        while count < total_count:
            for viewport in cls._viewport_dictionary.values():
                if viewport.z == z:
                    viewport.update(System.default_viewport)
                    count += 1
            z += 1
