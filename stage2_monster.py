import draw_gesture
import background
import hellkitty


class Stage2_Monster:
    def __init__(self):
        self.phase_num=0
        self.phase=[]
        self.boss = hellkitty.Boss_Kitty()


    def update(self, frame_time, events=None):
        if '하트' == draw_gesture.result:
            background.start=True
            draw_gesture.result = None
            self.boss.attack_start=True
        elif background.start:
            self.boss.update(frame_time, events)
            pass






        pass
    def draw(self):
        if background.start:
            self.boss.draw()
            pass
