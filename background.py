from pico2d import *
import resource

stage1width = 1980
stage1height = 1080

canvaswidth = 1280
canvasheight = 720

class Background:
    def __init__(self, stage):
        if stage == '1':
            self.background = [load_image('1stage\\1.png'), load_image('1stage\\2.png'),
                                   load_image('1stage\\3.png'),
                                   load_image('1stage\\4.png'), load_image('1stage\\5.png'),
                                   load_image('1stage\\6.png'),
                                   load_image('1stage\\7.png'), load_image('1stage\\8.png'), ]
        pass

    def update(self):
        pass

    def draw(self):
        for i in self.background:
            i.clip_draw(0, 0, stage1width, stage1height, canvaswidth//2,canvasheight//2  , stage1width*0.7, stage1height*0.7)
