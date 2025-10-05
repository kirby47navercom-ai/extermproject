from pico2d import *
from canvas_size import *

check_image_width = 825
check_image_height = 216



class GestureBackground:
    def __init__(self):
        self.check_image = load_image('Canvas\\2.png')
        self.canvas_image = load_image('Canvas\\1.png')
        self.check_image_x = canvaswidth//2
        self.check_image_y = canvasheight-(check_image_height*0.2)
        self.canvas_image_x=canvaswidth//2
        self.canvas_image_y=canvasheight+canvasheight//2

        pass

    def update(self, frame_time, events):
        for event in events:

            if self.canvas_image_y>canvasheight//2:
                self.check_image_y-=10
                self.canvas_image_y-=10
        pass


    def handle_event(self, event):
        pass

    def draw(self):
        self.check_image.clip_draw(0,0,check_image_width,check_image_height,self.check_image_x,self.check_image_y,check_image_width*0.4,check_image_height*0.4)
        self.canvas_image.draw(self.canvas_image_x,self.canvas_image_y)
        pass