import sys, os, logging
from project.scripts.core.audio import Audio
from project.scripts.core.graphics import Graphics

sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
import pygame


class Animation:
    """
    表示一个动画对象。
    方法:
        __init__(frames, voices): 初始化一个 Animation 对象。
        frame(): 生成一个动画帧。
        update(dst=Graphics.canvas): 通过将当前帧绘制到目标画布来更新动画。
        dispose(): 释放动画资源。
    """
    
    def __init__(self, frames, voices):
        """
        初始化一个 Animation 对象。

        参数:
        frames (list): 动画的帧列表。
        voices (list): 动画的声音列表。

        属性:
        x (int): 动画的 x 坐标。
        y (int): 动画的 y 坐标。
        loop (bool): 指示动画是否应循环。
        __frame_count (int): 当前帧计数。
        __voice_count (int): 当前声音计数。
        """
        
        self.__frames = frames
        self.__voices = voices
        self.x = 0
        self.y = 0
        self.loop = False
        self.__frame_count = 0
        self.__voice_count = 0

    def frame(self):
        """
        生成一个动画帧。

        返回:
            pygame.Surface: 生成的动画帧。
        """
        
        whole = pygame.Surface((320, 320))
        for pic in self.__frames[self.__frame_count].components:
            cache, x, y, opacity = pic
            rect = cache.get_rect()
            rect.x = x + 160
            rect.y = y + 160
            rect.center = (rect.x, rect.y)
            show = cache.copy()
            show.set_alpha(opacity)
            whole.blit(show, rect)
        return whole

    def update(self, dst=Graphics.canvas):
        """
        通过将当前帧绘制到目标画布来更新动画。

        参数:
        - dst (pygame.Surface): 将帧绘制到的目标画布。默认是 Graphics.canvas。
        """
        
        # 更新动画帧
        frame_whole = self.frame()
        rect = frame_whole.get_rect()
        rect.x = self.x
        rect.y = self.y
        rect.center = (self.x, self.y)
        dst.blit(self.frame(), rect)
        
        # 检查是否需要播放语音
        if self.__frame_count == self.__voices[self.__voice_count][0]:
            Audio.play_voice(self.__voices[self.__voice_count][1])
            self.__voice_count += 1
        
        self.__frame_count += 1
        
        # 检查是否到达最后一帧并处理循环或释放资源
        if self.__frame_count == len(self.__frames):
            if self.loop:
                self.__frame_count = 0
                self.__voice_count = 0
            else:
                self.dispose()

    def dispose(self):
        """
        释放动画资源。

        从 Graphics 模块中移除动画并记录成功消息。
        """
        
        Graphics.remove_animation(self)
        logging.info('Animation disposed successfully.')
