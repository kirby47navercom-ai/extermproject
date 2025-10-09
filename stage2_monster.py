import draw_gesture
import background



class Stage2_Monster:
    def __init__(self):
        self.phase_num=0
        self.phase=[]


    def update(self, frame_time, events=None):
        if '하트' == draw_gesture.result:
            background.start=True
            draw_gesture.result = None






        pass
    def draw(self):

        pass