import os, sys, logging
from project.scripts.core.graphics import Graphics
from project.scripts.core.system import System
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class Surface(pygame.Surface):
    """
    画布类。
    该类继承自pygame.Surface，提供了一系列的方法，用于绘制图像。
    
    属性:
        x: 画布的x坐标。
        y: 画布的y坐标。
        ox: 画布的原点x坐标。
        oy: 画布的原点y坐标。
        z: 画布的z坐标。
        size: 画布的尺寸。
        angle: 画布的旋转角度。
        opacity: 画布的透明度。
        scale: 画布的缩放比例。
        is_visible: 画布的可见性。
        is_centre: 画布的中心标志。
        _sprite_group: 画布的精灵组。
        
    方法:
        add_sprite: 添加精灵到画布中。
        remove_sprite: 从画布中移除精灵。
        clear_sprite: 清除画布中的精灵。
        draw_text: 在画布上绘制文本。
        clear: 清除画布。
        update: 更新画布。
        dispose: 释放画布。
        get_color: 获取颜色。
    """
    
    def __init__(self, size, pos = (0, 0)):
        """
        初始化一个画布对象。

        参数:
            size (tuple): 画布的尺寸。
            pos (tuple, optional): 画布的位置。默认为(0, 0)。
            
        属性:
            x: 画布的x坐标。
            y: 画布的y坐标。
            ox: 画布的原点x坐标。
            oy: 画布的原点y坐标。
            z: 画布的z坐标。
            size: 画布的尺寸。
            angle: 画布的旋转角度。
            opacity: 画布的透明度。
            scale: 画布的缩放比例。
            is_visible: 画布的可见性。
            is_centre: 画布的中心标志。
            _sprite_group: 画布的精灵组。
        """
        
        super().__init__(size, pygame.SRCALPHA)
        self.x, self.y = pos
        self.ox = 0
        self.oy = 0
        self.z = 0
        self.size = size
        self.angle = 0
        self.opacity = 255
        self.scale = 1.0
        self.is_visible = True
        self.is_centre = False
        self._sprite_group = []
        logging.info('Surface initialized.')
        
    def add_sprite(self, sprite):
        """
        添加精灵到画布中。
        
        参数:
            sprite: 精灵对象。
        """

        self._sprite_group.append(sprite)
        logging.info('Sprite added into surface. %s', sprite)
        
    def remove_sprite(self, sprite):
        """
        从画布中移除精灵。
        
        参数:
            sprite: 精灵对象。
        """

        self._sprite_group.remove(sprite)
        logging.info('Sprite removed from surface. %s', sprite)

    def clear_sprite(self):
        """
        清除画布中的精灵。
        """

        self._sprite_group.clear()
        logging.info('Sprite cleared from surface. %s', self)

    def draw_text(self, x, y, width, height, text, pos = 0, colour = (255, 255, 255, 255), font = System.font):
        """
        在画布上绘制文本。
        
        参数:
            x: 绘制的x坐标。
            y: 绘制的y坐标。
            width: 绘制的宽度。
            height: 绘制的高度。
            text: 绘制的文本。
            pos: 绘制的位置。0为左对齐，1为居中，2为右对齐。默认为0。
            colour: 绘制的颜色。默认为白色。
            font: 绘制的字体。默认为System.font。
        """

        # 根据文本、宽度和高度计算绘制的位置
        logging.info('text %s', text)
        size = font.size(text)
        dx, dy = 0, 0
        if size[0] < width:
            if (pos == 1):
                dx = (width - size[0]) / 2
            if (pos == 2):
                dx = width - size[0]
        if size[1] < height:
            dy = (height - size[1]) / 2
        text_surface = font.render(text, True, colour)
        self.blit(text_surface, (x + dx, y + dy), (0, 0, min(size[0], width), min(size[1], height)))
        logging.info('Text drawn. %s', text)

    def clear(self, need_log = False):
        """
        清除画布。
        
        参数:
            need_log: 是否需要记录日志。默认为False。
        """

        self.fill((0, 0, 0, 0))
        if need_log:
            logging.info('Surface cleared. %s', self)
        
    def update(self, dst = Graphics.canvas):
        """
        更新画布。
        
        参数:
            dst: 目标画布。默认为Graphics.canvas。
        """

        # 如果画布不可见，则不更新
        if not self.is_visible:
            return
        
        # 角度取模
        self.angle = self.angle % 360
        
        row_surface = self.copy()
        # 更新画布精灵
        for sprite in self._sprite_group:
            sprite.update(row_surface)
        if self.scale != 1.0 or self.angle != 0:
            draw_surface = pygame.transform.rotozoom(row_surface, self.angle, self.scale)
        else:
            draw_surface = row_surface
        
        # 设置画布不透明度
        draw_surface.set_alpha(self.opacity)
        
        # 绘制画布
        rect = draw_surface.get_rect()
        rect.x = self.x - self.ox
        rect.y = self.y - self.oy
        if self.is_centre:
            rect.center = (self.x, self.y)
        dst.blit(draw_surface, (rect.x, rect.y))
        
    def dispose(self):
        """
        释放画布。
        """

        self._sprite_group.clear()
        Graphics.remove_surface(self)
        logging.info('Surface disposed. %s', self)
    
    def get_color(self, clr):
        """
        获取颜色。
        
        参数:
            clr: 颜色名称。
        """

        color_map = {
            "white": (255, 255, 255, 255),
            "gray": (175, 175, 175, 255),
            "dkgray": (192, 192, 192, 255),
            "black": (0, 0, 0, 255),
            "red": (255, 50, 50, 255),
            "yellow": (255, 255, 128, 255),
            "orange": (255, 185, 25, 255),
            "brown": (200, 150, 75, 255),
            "blue": (128, 255, 255, 255),
            "dkblue": (128, 185, 255, 255),
            "green": (128, 255, 128, 255),
            "pink": (255, 128, 255, 255)
        }
        return color_map.get(clr, (255, 255, 255, 255))
