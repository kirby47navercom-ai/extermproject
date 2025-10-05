from pico2d import *
from canvas_size import *

check_image_width = 825
check_image_height = 216



class GestureBackground:
    def __init__(self):
        self.check_image = load_image('Canvas\\1.png')
        self.canvas_image = load_image('Canvas\\2.png')
        self.check_image_x = 400
        self.check_image_y = 300
        pass

    def update(self, frame_time, events):
        pass

    def draw(self):
        self.check_image.clip_draw(0,0,check_image_width,check_image_height,self.check_image_x,self.check_image_y,check_image_width*0.7,check_image_height*0.7)
        pass