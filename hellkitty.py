from pico2d import *

import background
from pattern import *
from resource import *
from random import randint
import canvas_size
from canvas_size import cout
import ramona
import math

SIZE = 1


class Boss_Kitty:
    image = None


    def __init__(self):
        self.pattern_set = get_pattern_set()
        if Boss_Kitty.image == None:
            Boss_Kitty.image = [load_image('2stage\\boss1.png'),load_image('2stage\\boss2.png')]

        self.x, self.y = canvas_size.canvaswidth-300, canvas_size.canvasheight//2
        self.hp = 240
        self.width, self.height = 386 * SIZE, 299 * SIZE
        self.frame = 0
        self.dir = 1
        self.timer = 0.0
        self.speed = 300
        self.cutscene = False
        self.cutscene_time = 7
        self.cutscene_timer = 0.0
        self.shape = self.pattern_set[randint(0, pattern_number)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.7

        self.current_pattern = 0

        self.attack_start=False
        self.attack= []
        self.attack1_time = 0.0
        self.attack1_timer = 1.0
        self.attack1_frame=0
        self.current1_num=5
        self.attack1_num=5

        self.idle_frame = 0
        self.animation_speed = 4.0

        self.die=False
        pass

    def update(self, frame_time, events=None):

        self.idle_frame = (self.idle_frame + self.animation_speed * frame_time) % 2

        self.move(frame_time)

        if not self.attack_start:
            if self.current_pattern == 0:
                self.pattern0(frame_time)
            elif self.current_pattern == 1:
                self.pattern1(frame_time)
            elif self.current_pattern == 2:
                self.pattern2(frame_time)
            elif self.current_pattern == 3:
                self.pattern2(frame_time)


        pass

    def boss_cutscene_on(self, frame_time):


        pass

    def move(self, frame_time):
        self.y += self.speed*frame_time*self.dir
        if self.y >= canvas_size.canvasheight - self.height // 2:
            self.dir = -1
        elif self.y <= self.height // 2:
            self.dir = 1
        pass

    def pattern0(self, frame_time):
        pass

    def pattern1(self, frame_time):

        pass

    def pattern2(self, frame_time):

        pass

    def rereset(self):
        pass
    def ramonatokitty(self):
        pass

    def hit_kitty_animation(self, frame_time):
        pass

    def die_kitty(self):
        pass

    def die_kitty_animation(self, frame_time):
        pass

    def draw(self):
        x,y = boss_kitty_idle_coordinate[int(self.idle_frame)][2:4]
        if background.start:
            self.image[int(self.idle_frame)].clip_draw(0, 0, x, y, self.x, self.y, x * SIZE, y * SIZE)
            cout(int(self.idle_frame))

        pass

