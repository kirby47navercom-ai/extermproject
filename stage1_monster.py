from pico2d import *

import resource
from canvas_size import *
import ramona
from resource import *
import random
import math

ghost_phase1_far=50
ghost_phase1_pos=[-1,-1,1,1,1]

ghost_speed=100



class Stage1_Monster:
    def __init__(self):
        self.ghost_imagen=load_image('1stage\\level1-png-sprite.png')
        self.phase1_monster=[  [0 if ghost_phase1_pos[i] == -1 else canvaswidth+ghost_phase1_pos[i]*ghost_phase1_far,random.randint(0,canvasheight)] for i in range(5)]
        self.phase_num=1
        pass
    def update(self, frame_time, events=None):
        if self.phase_num==1:
            self.phase1(frame_time)
        pass

    def phase1(self,frame_time):
        for i in range(self.phase1_monster.__len__()):
            distance = math.sqrt((self.phase1_monster[i][0]-ramona.Ramona_POS_X)**2+(self.phase1_monster[i][1]-ramona.Ramona_POS_Y)**2)
            self.phase1_monster[i][0]=self.phase1_monster[i][0]+(ramona.Ramona_POS_X-self.phase1_monster[i][0])*ghost_speed*frame_time/distance
            self.phase1_monster[i][1]=self.phase1_monster[i][1]+(ramona.Ramona_POS_Y-self.phase1_monster[i][1])*ghost_speed*frame_time/distance
        pass

    def draw(self):
        if self.phase_num==1:
            for i in range(self.phase1_monster.__len__()):
                left, bottom, width, height, jx, jy = ghost_idle_coordinate
                self.ghost_imagen.clip_draw(left, bottom, width, height, self.phase1_monster[i][0], self.phase1_monster[i][1], width, height)
        pass