from pico2d import *
from pattern import *
from resource import *
from random import randint
import ramona
import math

class Ghost:
    def __init__(self):
        self.image = load_image('monster\\ghost_normal.png')
        self.x, self.y = None, None
        self.hp=None
        self.width, self.height = 59, 76
        self.frame = 0
        self.dir = 1
        self.timer = 0.0
        self.speed = 50
        self.shape=pattern_set[randint(0,pattern_set.__len__()-1)]

    def update(self, frame_time, events=None):

        distance = math.sqrt((self.x - ramona.Ramona_POS_X) ** 2 + (self.y - ramona.Ramona_POS_Y) ** 2)
        self.x = self.x + (ramona.Ramona_POS_X - self.x) * self.speed * frame_time / distance
        self.y = self.y + (ramona.Ramona_POS_Y - self.y) * self.speed * frame_time / distance

        self.shape.x=self.x
        self.shape.y=self.y+self.height//2
        pass

    def draw(self):
        left, bottom, width, height, jx, jy = ghost_idle_coordinate
        if ramona.Ramona_POS_X<self.x:
            self.image.clip_composite_draw(left, bottom, width, height, 0, '', self.x + jx, self.y + jy,width,height)
        else:
            self.image.clip_composite_draw(left, bottom, width, height, 0, 'h', self.x + jx, self.y + jy, width, height)

        self.shape.draw()

