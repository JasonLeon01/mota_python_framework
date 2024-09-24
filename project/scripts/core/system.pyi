import pygame
import pygame.freetype

class System:
    """
    系统类。

    该类提供了系统的基本属性和方法。
    """
    
    __width: int
    """窗口宽度"""
    
    __height: int
    """窗口高度"""
    
    __scale: float
    """窗口缩放比例"""
    
    canvas: pygame.Surface
    """窗口画布"""
    
    title: str
    """窗口标题"""
    
    font: pygame.freetype.Font
    """窗口字体"""
    
    frame_rate: int
    """窗口帧率"""
    
    running: bool
    """窗口运行标志"""
    
    clock: pygame.time.Clock
    """窗口时钟"""
    
    is_music_on: bool
    """音乐开关"""
    
    is_voice_on: bool
    """音效开关"""
    
    scene: any
    """场景对象"""
    
    wheel: int
    """鼠标滚轮值"""
    
    default_viewport: pygame.Surface
    """默认视口"""

    @classmethod
    def init(cls, inifile: str) -> None:
        """
        初始化系统的基本属性。
        
        参数:

            inifile (str): INI文件路径。
        """
        pass
        
    @classmethod
    def get_size(cls) -> tuple[int, int]:
        """
        获取窗口尺寸。
        
        返回:

            tuple: 窗口尺寸。
        """
        pass
    
    @classmethod
    def get_scale(cls) -> float:
        """
        获取窗口缩放比例。
        
        返回:

            float: 窗口缩放比例。
        """
        pass
    
    @classmethod
    def change_scale(cls, scale: float) -> None:
        """
        更改窗口缩放比例。
        
        参数:

            scale (float): 缩放比例。
        """
        pass

    @classmethod
    def get_variable(cls, name: str) -> any:
        """
        获取系统变量。
        
        参数:

            name (str): 变量名。
        """
        pass