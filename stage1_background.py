from pico2d import *
import resource

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
            i.draw(400, 300)