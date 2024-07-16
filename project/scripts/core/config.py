import project.scripts.core.method as method

class Config:
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
        print('LOG: Config loaded successfully.')
        