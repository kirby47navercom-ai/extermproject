from pico2d import *

import resource
from canvas_size import *
import ramona
from resource import *
import random
import math
from ghost_normal import *

ghost_phase1_far=50
ghost_phase1_pos=[-1,-1,1,1,1]

ghost_speed=50

class Stage1_Monster:
    def __init__(self):
        self.phase1=[Ghost() for _ in range(5)]

        for i in range(self.phase1.__len__()):
            self.phase1[i].x=0 if ghost_phase1_pos[i] == -1 else canvaswidth+ghost_phase1_pos[i]*ghost_phase1_far
            self.phase1[i].y=random.randint(0,canvasheight)
        pass
    def update(self, frame_time, events=None):
        for i in range(self.phase1.__len__()):
            self.phase1[i].update(frame_time,events)
        pass

    def shape_check(self,frame_time):

        pass

    def draw(self):
        for i in range(self.phase1.__len__()):
            self.phase1[i].draw()
        pass