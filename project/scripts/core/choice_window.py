import os, sys, math, logging
from project.scripts.core.audio import Audio
from project.scripts.core.config import Config
from project.scripts.core.graphics import Graphics
from project.scripts.core.system import System
from project.scripts.core.window import Window
from project.scripts.core.input import Input
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame

class ChoiceWindow(Window):
    """
    表示一个选择窗口。
    
    方法:
        __init__(size: int): 初始化一个 ChoiceWindow 对象。
        rows(): 返回 ChoiceWindow 的行数。
        update_cursor_rect(): 更新光标的矩形。
        mouse_in_rect(): 判断鼠标是否在 ChoiceWindow 的矩形内。
        confirm(): 判定是否确认，含有鼠标点击和键盘触发两种情况。
        cancel(): 判定是否取消，含有鼠标点击和键盘触发两种情况。
        _key_response(): 处理键盘输入，包括上下左右键，用于选择。
        _mouse_response(): 处理鼠标输入，包括鼠标滚轮，用于选择。
        update(dst=Graphics.canvas): 更新 ChoiceWindow 对象。
    """
    
    def __init__(self, size):
        """
        初始化一个ChoiceWindow对象。

        参数:
            size (int): ChoiceWindow的大小。

        属性:
            column (int): ChoiceWindow的列位置。
            cursor_height (int): ChoiceWindow中光标的高度。
            index (int): ChoiceWindow中当前项目的索引。
            items (int): ChoiceWindow中项目的总数。
            is_active (bool): 表示ChoiceWindow是否处于活动状态。
        """

        super().__init__(size)
        self.column = 1
        self.cursor_height = 32
        self.index = 0
        self.items = 1
        self.is_active = True
    
    def rows(self):
        """
        返回ChoiceWindow的行数。
        
        返回:
            int: ChoiceWindow的行数。
        """

        return int(math.ceil(1.0 * self.items / self.column))

    def update_cursor_rect(self):
        """
        更新光标的矩形。
        """
        
        # 计算光标的位置
        row = self.index / self.column
        cursor_width = self.get_size()[0] / self.column - 32
        x = self.index % self.column * (cursor_width + 32)
        y = int(row) * self.cursor_height
        if self.contents:
            y -= self.contents.oy
        self.set_rect(x, y, cursor_width, self.cursor_height)

    def mouse_in_rect(self):
        """
        判断鼠标是否在ChoiceWindow的矩形内。
        """

        return Input.in_rect((self.x + 16, self.y + 16, self.get_size()[0] - 32, self.get_size()[1] - 32))
    
    def confirm(self):
        """
        判定是否确认，含有鼠标点击和键盘触发两种情况。
        """

        # 按下确认键的情况
        if Input.trigger_confirm():
            return True
        
        # 鼠标点击的情况
        if self.mouse_in_rect():
            if Input.left_click('trigger'):
                # 计算鼠标点击的索引
                x, y = Input.get_mouse_pos()
                screen_index = (y - self.y - 16) // self.cursor_height
                now_index = screen_index * self.column + (x - self.x - 16) // (self.get_size()[0] / self.column - 32) + self.column * (self.contents.oy // self.cursor_height)
                logging.info('Caught index on screen is %s, now index is %s', now_index, self.index)
                
                # 如果索引相同，则确认
                if now_index == self.index:
                    return True
                
                # 否则更新索引
                Audio.play_voice(Config.cursor_se)
                self.index = now_index
        return False

    def cancel(self):
        """
        判定是否取消，含有鼠标点击和键盘触发两种情况。
        """

        return self.mouse_in_rect() and Input.trigger(pygame.K_ESCAPE) or Input.right_click('repeat')

    def _key_response(self):
        """
        处理键盘输入，包括上下左右键，用于选择。
        """

        if Input.repeat(pygame.K_UP):
            if (self.column == 1 and Input.trigger(pygame.K_UP)) or self.index >= self.column:
                self.index = (self.index - self.column + self.items) % self.items
                Audio.play_voice(Config.cursor_se)
        if Input.repeat(pygame.K_DOWN):
            if (self.column == 1 and Input.trigger(pygame.K_DOWN)) or self.index < self.items - self.column:
                self.index = (self.index + self.column) % self.items
                Audio.play_voice(Config.cursor_se)
        if Input.repeat(pygame.K_LEFT):
            if self.column > 1 and self.index > 0:
                self.index = (self.index - 1 + self.items) % self.items
                Audio.play_voice(Config.cursor_se)
        if Input.repeat(pygame.K_RIGHT):
            if self.column > 1 and self.index < self.items - 1:
                self.index = (self.index + 1) % self.items
                Audio.play_voice(Config.cursor_se)

    def _mouse_response(self):
        """
        处理鼠标输入，包括鼠标滚轮，用于选择。
        """

        if self.mouse_in_rect() and System.wheel != 0:
            if System.wheel > 0:
                self.index = (self.index - 1 + self.items) % self.items
                Audio.play_voice(Config.cursor_se)
            elif System.wheel < 0:
                self.index = (self.index + 1) % self.items
                Audio.play_voice(Config.cursor_se)
            System.wheel = 0

    def update(self, dst = Graphics.canvas):
        """
        更新ChoiceWindow对象。
        
        参数:
            dst (pygame.Surface): 目标画布。
        """

        super().update(dst)
        
        # 如果ChoiceWindow不活动或者没有项目或者索引小于0，则返回
        if not self.is_active or self.items == 0 or self.index < 0:
            return
        
        # 更新光标的位置
        if self.index >= self.items:
            self.index = self.items - 1
        
        # 处理输入
        self._key_response()
        self._mouse_response()
        
        # 根据当前光标的位置调整内容的位置
        if self.contents:
            if (self.index // self.column) * self.cursor_height - self.contents.oy + 32 > self.get_size()[1] - 32:
                self.contents.oy = (self.index // self.column) * self.cursor_height - self.get_size()[1] + 64
            if (self.index // self.column) * self.cursor_height - self.contents.oy < 0:
                self.contents.oy = (self.index // self.column) * self.cursor_height
        
        # 更新光标的矩形
        self.update_cursor_rect()
