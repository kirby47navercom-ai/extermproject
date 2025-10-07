from pico2d import *
from pattern import *
from resource import *
from random import randint
import ramona
import math


class Ghost:
    def __init__(self):
        pattern_set=get_pattern_set()

        self.image = load_image('1stage\\level1-png-sprite.png')
        self.x, self.y = 0, 0
        self.hp=20
        self.width, self.height = 59, 76
        self.frame = 0
        self.dir = 1
        self.timer = 0.0
        self.speed = 50
        self.shape=pattern_set[randint(0,pattern_set.__len__()-6)]

    def update(self, frame_time, events=None):

        distance = math.sqrt((self.x - ramona.Ramona_POS_X) ** 2 + (self.y - ramona.Ramona_POS_Y) ** 2)
        self.x = self.x + (ramona.Ramona_POS_X - self.x) * self.speed * frame_time / distance
        self.y = self.y + (ramona.Ramona_POS_Y - self.y) * self.speed * frame_time / distance

        self.shape.x=self.x
        self.shape.y=self.y+self.height*0.7

        self.ramonatoghost()

        pass

    def ramonatoghost(self):
        if collide([ramona.Ramona_POS_X,ramona.Ramona_POS_Y,ramona.Ramona_SIZE_X,ramona.Ramona_SIZE_Y],[self.x,self.y,self.width,self.height]) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible:
            if ramona.CURRENT_HP>0:
                ramona.CURRENT_HP-=1
                ramona.Ramona_invincible=True
                ramona.invincible_timer=0.0

        pass



    def draw(self):
        left, bottom, width, height, jx, jy = ghost_idle_coordinate
        if ramona.Ramona_POS_X<self.x:
            self.image.clip_composite_draw(left, bottom, width, height, 0, '', self.x + jx, self.y + jy,width,height)
        else:
            self.image.clip_composite_draw(left, bottom, width, height, 0, 'h', self.x + jx, self.y + jy, width, height)

        self.shape.draw()

