from pico2d import *



class Mouse:
    def __init__(self, stage):
        self.normal = load_image('Mouse\\1.png')
        self.paint = load_image('Mouse\\2.png')
        self.x=0
        self.y=0
        pass

    def update(self, frame_time):
        if event.type == SDL_MOUSEMOTION:
            self.x, self.y = event.x, get_canvas_height() - 1 - event.y
        pass

    def draw(self):

        pass