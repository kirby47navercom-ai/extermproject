from pico2d import *
from pattern import *
from resource import *
from random import randint
import canvas_size
from canvas_size import cout
import ramona
import math

SIZE = 1.2


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
        self.speed = 50
        self.cutscene = False
        self.cutscene_time = 7
        self.cutscene_timer = 0.0
        self.shape = self.pattern_set[randint(0, pattern_number)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.7

        self.idle_frame = 0
        pass

    def update(self, frame_time, events=None):


        pass

    def boss_cutscene_on(self, frame_time):


        pass

    def move(self, frame_time):
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
        pass

