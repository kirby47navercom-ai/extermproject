from pico2d import *
from canvas_size import *

class GestureBackground:
    def __init__(self):
        self.image = load_image('Canvas\\1.png')
        self.x = 400
        self.y = 300
        pass

    def update(self, frame_time, events):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        pass