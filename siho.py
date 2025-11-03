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

SIZE = 1





class Boss_Siho:
    image = None
    attack1_image = None
    attack2_image = None
    little_image = None
    die_image = None

    def __init__(self):
        self.pattern_set = get_pattern_set()


        self.x, self.y = canvas_size.canvaswidth - 300, canvas_size.canvasheight // 2
        self.boss_hp = 240
        self.hp = self.boss_hp
        self.hp_bar = Boss_HP()
        self.width, self.height = 386 * SIZE, 299 * SIZE
        self.frame = 0
        self.dir = 1
        self.timer = 0.0
        self.speed = 300
        self.shape = self.pattern_set[randint(0, pattern_number)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.2
        self.idle_frame = 0
        self.animation_speed = 4.0





    def update(self, frame_time, events=None):
        pass

    def draw(self):
        pass

    # --- 나머지 Helper 함수들 ---
    def move(self, frame_time):
        self.y += self.speed * frame_time * self.dir
        if self.y >= canvas_size.canvasheight - self.height // 2:
            self.dir = -1
        elif self.y <= self.height // 2:
            self.dir = 1

    def ramonatoattack(self, i):
        ax, ay = self.attack1[i][0], self.attack1[i][1]
        rx, ry = ramona.Ramona_POS_X, ramona.Ramona_POS_Y
        threshold = 40
        dx, dy = ax - rx, ay - ry
        b = (
                        dx * dx + dy * dy <= threshold * threshold) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible
        if b:
            if ramona.CURRENT_HP > 0:
                ramona.CURRENT_HP -= 1
                ramona.Ramona_invincible = True
                ramona.invincible_timer = 0.0
                canvas_size.start_shake(0.5, 5.0)
        return b

