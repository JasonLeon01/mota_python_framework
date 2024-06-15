class Config:
    def __init__(self, config_json):
        config = json.loads(config_json)
        main_config = config.get("main", {})
        
        self.title = main_config.get("title", "")
        self.windowskinName = main_config.get("windowskinname", "")
        self.titleName = main_config.get("titlename", "")
        self.fontName = main_config.get("fontname", "")
        self.titleBGM = main_config.get("titlebgm", "")
        self.cursorSE = main_config.get("cursorse", "")
        self.decisionSE = main_config.get("decisionse", "")
        self.cancelSE = main_config.get("cancelse", "")
        self.buzzerSE = main_config.get("buzzerse", "")
        self.shopSE = main_config.get("shopse", "")
        self.saveSE = main_config.get("savese", "")
        self.loadSE = main_config.get("loadse", "")
        self.gateSE = main_config.get("gatese", "")
        self.stairSE = main_config.get("stairse", "")
        self.getSE = main_config.get("getse", "")
        self.windowOpacity = int(main_config.get("windowopacity", 0))
        