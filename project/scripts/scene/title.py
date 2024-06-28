from project.scripts.core.scene import Scene_Base

class Scene(Scene_Base):
    def __init__(self):
        self.load_data_from_json(__file__)
        super().__init__()
        print('LOG: Scene Title launched successfully.')
        
    def update(self):
        super().update()
