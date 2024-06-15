import os
import json

class Config:
    def __init__(self):
        with open(r'project\data\system\config.json', 'r', encoding='utf-8') as file:
            config_json = file.read()
        config = json.loads(config_json)
        main_config = config.get("main", {})
        
        self.title = main_config.get("title", "")
        self.windowskin_file = main_config.get("windowskin_file", "")
        self.title_file = main_config.get("title_file", "")
        self.font_name = main_config.get("font_name", "")
        self.title_bgm = main_config.get("title_bgm", "")
        self.cursor_se = main_config.get("cursor_se", "")
        self.decision_se = main_config.get("decision_se", "")
        self.cancel_se = main_config.get("cancel_se", "")
        self.buzzer_se = main_config.get("buzzer_se", "")
        self.shop_se = main_config.get("shop_se", "")
        self.save_se = main_config.get("save_se", "")
        self.load_se = main_config.get("load_se", "")
        self.gate_se = main_config.get("gate_se", "")
        self.stair_se = main_config.get("stair_se", "")
        self.get_se = main_config.get("get_se", "")
        self.window_opacity = int(main_config.get("window_opacity", 0))
        