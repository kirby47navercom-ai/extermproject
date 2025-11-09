from pico2d import *

import background_2stage
from boss_hp import Boss_HP
from pattern import *
from resource import *
from random import randint
import canvas_size
from canvas_size import cout
import ramona
import resource
import math

SIZE = 1.8





class Boss_Siho:
    def __init__(self):
        self.pattern_set = get_pattern_set()

        self.x, self.y = 1000, 300
        self.boss_hp = 240
        self.hp = self.boss_hp
        self.hp_bar = Boss_HP()
        self.width, self.height = 386 * SIZE, 299 * SIZE
        self.frame = 0
        self.dir = ''
        self.timer = 0.0
        self.speed = 100
        self.shape = self.pattern_set[randint(0, pattern_number)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.2
        self.idle_frame = 0
        self.animation_speed = 8.0

        self.pattern_num=0

        #패턴 0
        self.appear_animation = False
        self.appear_frame = 0
        self.appear_timer = 0.0
        self.appear_time = 4.0

        #패턴 1
        self.idle_frame = 0
        self.idle_timer = 0.0
        self.idle_time = 1.0



        self.hit = False
        self.hit_animation = False
        self.hit_time = 0.0
        self.die = False
        self.die_animation = False
        self.die_animation_speed = 2.0
        self.die_frame = 0






    def update(self, frame_time, events=None):
        if not self.appear_animation:
            self.appear_frame = (self.appear_frame + self.animation_speed * frame_time) % 4
            self.appear_timer += frame_time
            if self.appear_timer >= self.appear_time:
                self.appear_animation = True
        else:
            pattern_method = getattr(self, f'pattern{self.pattern_num}', None)
            if pattern_method:
                pattern_method(frame_time)




        self.dir = '' if ramona.Ramona_POS_X > self.x else 'h'


    def pattern0(self, frame_time):
        self.appear_frame = (self.appear_frame + self.animation_speed * frame_time) % 8
        if int(self.appear_frame) == 7:
            self.pattern_num=1

    def pattern1(self, frame_time):
        self.idle_frame = (self.idle_frame + self.animation_speed * frame_time) % 2
        self.idle_timer += frame_time
        if self.idle_timer >= self.idle_time:
            pass
    def pattern2(self, frame_time):

            pass
    def pattern3(self, frame_time):

            pass
    def pattern4(self, frame_time):

            pass
    def pattern5(self, frame_time):

            pass





    def draw(self):
        if not self.appear_animation:
            boss_siho_appear_image[int(self.appear_frame)].clip_composite_draw(0, 0, 64, 64,0,self.dir, self.x - canvas_size.camera_x,
                                                                     self.y - canvas_size.camera_y,
                                                                     64 * SIZE, 64 * SIZE)
        elif self.appear_animation and self.pattern_num==0:
            boss_siho_appear_image[int(self.appear_frame)].clip_composite_draw(0, 0, 64, 64, 0, self.dir,
                                                                               self.x - canvas_size.camera_x,
                                                                               self.y - canvas_size.camera_y,
                                                                               64 * SIZE, 64 * SIZE)
        elif self.appear_animation and self.pattern_num == 1:
            boss_siho_appear_image[int(self.appear_frame)].clip_composite_draw(0, 0, 64, 64, 0, self.dir,
                                                                               self.x - canvas_size.camera_x,
                                                                               self.y - canvas_size.camera_y,
                                                                               64 * SIZE, 64 * SIZE)



