class Config:
    """
    表示一个配置对象。
    """
    
    windowskin_file: str
    """窗口皮肤文件"""
    
    title_file: str
    """标题文件"""
    
    font_name: str
    """字体名称"""
    
    title_bgm: str
    """标题背景音乐"""
    
    cursor_se: str
    """光标音效"""
    
    decision_se: str
    """确认音效"""
    
    cancel_se: str
    """取消音效"""
    
    buzzer_se: str
    """警告音效"""
    
    shop_se: str
    """商店音效"""
    
    save_se: str
    """保存音效"""
    
    load_se: str
    """载入音效"""
    
    gate_se: str
    """门音效"""
    
    stair_se: str
    """楼梯音效"""
    
    get_se: str
    """获得物品音效"""
    
    window_opacity: int
    """窗口透明度"""

    @classmethod
    def init(cls, file: str) -> None:
        """
        初始化配置设置。
        参数: 
            cls: 类对象。
            file: 配置文件的路径。
        """
        pass