from project.scripts.core.cache import Cache
from project.scripts.core.sprite import Sprite
from project.scripts.core.graphics import Graphics
from project.scripts.core.viewport import ViewportManager
from project.scripts.module.object import Object
from project.scripts.core.surface import Surface
import pygame

class Map:
    def __init__(self, pos = (192, 32)):
        self.name = ''
        self.width = 11
        self.height = 11
        self.tileset = None
        self.bgm = None
        self.background = None
        self.tile = []
        # 地图主视口，用来限制显示
        self.viewport = Surface((416, 416), pos)
        # 地图画面视口
        self.viewport2 = None
        
    def get_size(self):
        return self.width, self.height
    
    def load_map(self, map_data):
        # 读取地图数据
        self.name = map_data['name']
        self.width = map_data['width']
        self.height = map_data['height']
        if self.viewport2:
            ViewportManager.remove_viewport(self.viewport2)
            self.viewport2.clear()
            self.viewport2.clear_sprite()
        self.viewport2 = Surface((self.width * 32, self.height * 32))
        self.tileset = map_data['tileset']
        self.bgm = map_data['bgm']
        self.background = map_data['background']
        self.tile = map_data['tile']

        # 读取事件数据
        for obj in map_data['objects']:
            frames = []
            cache = Cache.character(obj['file'])
            frame_count = cache.get_rect().width // 32
            for i in range(frame_count):
                frames.append(pygame.Surface.subsurface(cache, (i * 32, obj['loc'][1], 32, 32)))
            add_obj = Object(Sprite(frames), (obj['pos'][0], obj['pos'][1]), obj['interval'], eval(obj['move']))
            add_obj.id = obj['id']
            add_obj.name = obj['name']
            add_obj.condition = obj['condition']
            add_obj.todo = obj['todo']
            self.viewport2.add_sprite(add_obj)

    def update(self, dst):
        self.viewport.clear()
        self.viewport.blit(self.background, (0, 0))
        self.viewport2.clear()
        _, __, width, height = self.tileset.get_rect()
        line_max = width // 32
        column_max = height // 32
        for tile in self.tile:
            for y in range(column_max):
                for x in range(line_max):
                    tile_id = tile[y][x]
                    if tile_id == 0:
                        continue
                    self.viewport2.blit(self.tileset, (x * 32, y * 32), ((tile_id - 1) % line_max * 32, (tile_id - 1) // line_max * 32, 32, 32))
        if self.width < 13:
            self.viewport2.x = (13 - self.width) * 16
        else:
            self.viewport2.x = 0
        if self.height < 13:
            self.viewport2.y = (13 - self.height) * 16
        else:
            self.viewport2.y = 0
        self.viewport2.update(self.viewport)
        self.viewport.update(dst)
