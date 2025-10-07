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
        self.ghost_imagen=load_image('1stage\\level1-png-sprite.png')
        self.phase1=[Ghost() for _ in range(5)]


        pass
    def update(self, frame_time, events=None):
        for i in self.phase1.__len__():
            self.phase1[i].update(self.ghost_imagen)
        pass

    def phase1(self,frame_time):

        pass

    def draw(self):
        for i in self.phase1.__len__():
            self.phase1[i].draw()
        pass