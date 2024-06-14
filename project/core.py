import time
import configparser
from scripts import config
import sys
sys.path.append('custom_lib')
import arcade

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.viewport_left = 0
        self.viewport_bottom = 0

        arcade.set_background_color(arcade.color.BLACK)
    def setup(self):
        pass
    def on_draw(self):
        self.clear()

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('mota.ini')
    width, height = 640, 480
    width = int(width * config["Mota"].getfloat("resolution", 640))
    height = int(height * config["Mota"].getfloat("resolution", 480))
    title = config["Mota"].get("title", "Mota")
    
    window = GameWindow(width, height, title)
    window.setup()
    arcade.run()
    
    time.sleep(1)