from pico2d import *
from pattern import *
from resource import *
from random import randint
import canvas_size
from canvas_size import cout
import ramona
import math


class Boss_Ghost:
    def __init__(self):
        self.pattern_set = get_pattern_set()
        self.image = load_image('1stage\\level1-png-sprite.png')
        self.x, self.y = canvas_size.canvaswidth//2, canvas_size.canvasheight+100
        self.hp=500
        self.width, self.height = 70*1.5,104*1.5
        self.frame = 0
        self.dir = 1
        self.timer = 0.0
        self.speed = 50
        self.cutscene=False
        self.cutscene_time=7
        self.cutscene_timer=0.0
        self.shape=self.pattern_set[randint(0,self.pattern_set.__len__()-6)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.7

        self.idle_frame=0


        self.die=False
        self.die_animation=False
        self.die_animation_speed = 8.0
        self.die_frame=0

        self.hit=False
        self.hit_animation = False
        self.hit_animation_speed = 8.0
        self.hit_frame=0

    def update(self, frame_time, events=None):
        if self.cutscene:
            if not self.die_animation and not self.hit_animation:
                #self.move(frame_time)
                pass
            elif self.hit_animation and not self.die_animation:
                self.hit_ghost_animation(frame_time)
            elif self.die_animation:
                self.die_ghost_animation(frame_time)
            self.ramonatoghost()
            self.die_ghost()
        else:
            self.boss_cutscene_on(frame_time)




        self.idle_frame =(self.idle_frame + self.die_animation_speed * frame_time) % 4

        pass

    def boss_cutscene_on(self,frame_time):
        self.cutscene_timer+=frame_time
        if self.cutscene_timer>=self.cutscene_time:
            self.cutscene=True
        else:
            self.y -=self.speed*frame_time
            canvas_size.start_shake(0.1,3)


        pass

    def move(self, frame_time):
        distance = math.sqrt((self.x - ramona.Ramona_POS_X) ** 2 + (self.y - ramona.Ramona_POS_Y) ** 2)
        self.x = self.x + (ramona.Ramona_POS_X - self.x) * self.speed * frame_time / distance
        self.y = self.y + (ramona.Ramona_POS_Y - self.y) * self.speed * frame_time / distance

        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.7

    def pattern1(self):
        pass
    def pattern2(self):
        pass
    def pattern3(self):
        pass
    def pattern4(self):
        pass

    def ramonatoghost(self):
        if collide([ramona.Ramona_POS_X,ramona.Ramona_POS_Y,ramona.Ramona_SIZE_X,ramona.Ramona_SIZE_Y],
                   [self.x,self.y,self.width,self.height]) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible and not self.die_animation:
            if ramona.CURRENT_HP>0:
                ramona.CURRENT_HP-=1
                ramona.Ramona_invincible=True
                ramona.invincible_timer=0.0
                self.die_animation = True
                canvas_size.start_shake(0.5, 5.0)


        pass

    def hit_ghost_animation(self, frame_time):
        self.hit_frame = (self.hit_frame + self.hit_animation_speed * frame_time) % 4
        if int(self.hit_frame) == 3:
            self.hit_animation = False
            self.shape = self.pattern_set[randint(0, self.pattern_set.__len__() - 6)]
            self.shape.x = self.x
            self.shape.y = self.y + self.height * 0.7
        pass

    def die_ghost(self):
        if self.hp<=0 and not self.die_animation:
            self.shape.name='No'
        pass

    def die_ghost_animation(self, frame_time):
        self.die_frame = (self.die_frame + self.die_animation_speed * frame_time) % 4
        if int(self.die_frame) == 3:
            self.die = True
        pass

    def draw(self):

        if not self.die:

            if self.die_animation:
                left, bottom, width, height, jx, jy = boss_ghost_die_coordinate[int(self.die_frame)]
            elif self.hit_animation:
                left, bottom, width, height, jx, jy = boss_ghost_hit_coordinate[int(self.hit_frame)]
            else:  left, bottom, width, height, jx, jy = boss_ghost_idle_coordinate[int(self.idle_frame)]

            if ramona.Ramona_POS_X < self.x:
                self.image.clip_composite_draw(left, bottom, width, height, 0, '', self.x + jx-canvas_size.camera_x, self.y + jy-canvas_size.camera_y, width*1.5, height*1.5)
            else:
                self.image.clip_composite_draw(left, bottom, width, height, 0, 'h', self.x + jx-canvas_size.camera_x, self.y + jy-canvas_size.camera_y, width*1.5, height*1.5)


            if not self.die_animation and self.cutscene:
                self.shape.draw()

