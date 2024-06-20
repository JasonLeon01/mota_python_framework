import os
import json

class Config:
    def __init__(self, file):
        with open(file, 'r', encoding='utf-8') as file:
            config_json = file.read()
        config = json.loads(config_json)
        
        self.windowskin_file = config['windowskin_file']
        self.title_file = config['title_file']
        self.font_name = config['font_name']
        self.title_bgm = config['title_bgm']
        self.cursor_se = config['cursor_se']
        self.decision_se = config['decision_se']
        self.cancel_se = config['cancel_se']
        self.buzzer_se = config['buzzer_se']
        self.shop_se = config['shop_se']
        self.save_se = config['save_se']
        self.load_se = config['load_se']
        self.gate_se = config['gate_se']
        self.stair_se = config['stair_se']
        self.get_se = config['get_se']
        self.window_opacity = config['window_opacity']
        print('LOG: Config loaded successfully.')
        
mota_config = Config(r'project\data\system\config.json')