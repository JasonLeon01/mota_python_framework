import logging
import project.scripts.core.method as method

class Config:
    """
    表示一个配置对象。
    
    方法:
        init(cls, file): 初始化配置设置。
    
    属性:
        windowskin_file: 窗口皮肤文件。
        title_file: 标题文件。
        font_name: 字体名称。
        title_bgm: 标题背景音乐。
        cursor_se: 光标音效。
        decision_se: 确认音效。
        cancel_se: 取消音效。
        buzzer_se: 警告音效。
        shop_se: 商店音效。
        save_se: 保存音效。
        load_se: 载入音效。
        gate_se: 门音效。
        stair_se: 楼梯音效。
        get_se: 获得物品音效。
        window_opacity: 窗口透明度。
    """
    windowskin_file = None
    title_file = None
    font_name = None
    title_bgm = None
    cursor_se = None
    decision_se = None
    cancel_se = None
    buzzer_se = None
    shop_se = None
    save_se = None
    load_se = None
    gate_se = None
    stair_se = None
    get_se = None
    window_opacity = None

    @classmethod
    def init(cls, file):
        """
        初始化配置设置。
        参数: 
            cls: 类对象。
            file: 配置文件的路径。
        """
        config = method.load_json_file(file)
        
        cls.windowskin_file = config['windowskin_file']
        cls.title_file = config['title_file']
        cls.font_name = config['font_name']
        cls.title_bgm = config['title_bgm']
        cls.cursor_se = config['cursor_se']
        cls.decision_se = config['decision_se']
        cls.cancel_se = config['cancel_se']
        cls.buzzer_se = config['buzzer_se']
        cls.shop_se = config['shop_se']
        cls.save_se = config['save_se']
        cls.load_se = config['load_se']
        cls.gate_se = config['gate_se']
        cls.stair_se = config['stair_se']
        cls.get_se = config['get_se']
        cls.window_opacity = config['window_opacity']
        logging.info('Config loaded successfully.')
        