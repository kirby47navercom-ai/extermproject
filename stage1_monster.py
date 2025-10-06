from pico2d import *

import resource
from canvas_size import *
from ramona import *
from resource import *
import random
import math

from sheetyong import ghost_image

ghost_phase1_far=50
ghost_phase1_pos=[-1,-1,1,1,1]

ghost_speed=200



class Stage1_Monster:
    def __init__(self):
        self.phase1_monster=[  [ghost_phase1_pos[i]*canvaswidth,random.randint(0,canvasheight)] for i in range(5)]
        self.phase_num=1
        pass
    def update(self, frame_time, events=None):
        if self.phase_num==1:
            self.phase1(frame_time)
        pass

    def phase1(self,frame_time):
        for i in range(self.phase1_monster.__len__()):
            distance = math.sqrt((self.phase1_monster[i][0]-Ramona_POS_X)**2+(self.phase1_monster[i][1]-Ramona_POS_Y)**2)
            self.phase1_monster[i][0]=self.phase1_monster[i][0]+(Ramona_POS_X-self.phase1_monster[i][0])*ghost_speed*frame_time/distance
            self.phase1_monster[i][1]=self.phase1_monster[i][1]+(Ramona_POS_Y-self.phase1_monster[i][1])*ghost_speed*frame_time/distance
        pass

    def draw(self):
        if self.phase_num==1:
            for i in range(self.phase1_monster.__len__()):
                left, bottom, width, height, jx, jy = ghost_idle_coordinate
                ghost_image.clip_composite_draw(left, bottom, width, height, 0, '', self.phase1_monster[i][0] + jx, self.phase1_monster[i][1] + jy, width,height)

        pass