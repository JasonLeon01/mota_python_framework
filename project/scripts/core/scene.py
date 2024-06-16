from project.scripts.core.graphics import mota_graphics

class Scene_Base:
    def update(self):
        mota_graphics.update()
        
    def quit(self):
        for attr_name, attr_value in self.__dict__.items():
            if hasattr(attr_value, 'dispose'):
                attr_value.dispose()
                
    def __del__(self):
        self.quit()