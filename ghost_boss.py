from pico2d import *
from pattern import *
from resource import *
from random import randint
import canvas_size
from canvas_size import cout
import ramona
import math

SIZE=1.2

class Boss_Ghost:
    def __init__(self):
        self.pattern_set = get_pattern_set()
        self.image = load_image('1stage\\level1-png-sprite.png')
        self.x, self.y = canvas_size.canvaswidth//2, canvas_size.canvasheight+100
        self.hp=240
        self.width, self.height = 70*SIZE,104*SIZE
        self.frame = 0
        self.dir = 1
        self.timer = 0.0
        self.speed = 50
        self.cutscene=False
        self.cutscene_time=7
        self.cutscene_timer=0.0
        self.shape=self.pattern_set[randint(0,self.pattern_set.__len__()-1)]
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
        
        self.pattern_num=0
        self.prev_pattern=0
        self.pattern_ready=False
        self.pattern_ready_timer=0.0
        self.pattern_ready_time=1.0
        self.pattern_ready_speed=1000

        self.pattern_state=0

        self.pattern0_ready_timer=0.0
        self.pattern0_ready_time=0.5

        self.pattern1_x,self.pattern1_y=randint(int(self.width), int(canvas_size.canvaswidth - self.width)),canvas_size.canvasheight//2+canvas_size.canvasheight//4
        self.pattern1_frame=0

        self.hit_num=3

        self.attack_timer=0.0
        self.attack_time=8.0

        self.half_hp=False
        
        
        

    def update(self, frame_time, events=None):
        if self.cutscene and self.pattern_ready_timer>= self.pattern_ready_time:
            if not self.die_animation and not self.hit_animation:
                self.move(frame_time)
                pass
            elif self.hit_animation and not self.die_animation:
                self.hit_ghost_animation(frame_time)
            elif self.die_animation:
                self.die_ghost_animation(frame_time)
            self.ramonatoghost()
            self.die_ghost()
        elif self.cutscene:
            self.pattern_ready_timer+=frame_time
        else:
            self.boss_cutscene_on(frame_time)

        if self.hp<=120 and not self.half_hp:
            self.speed=300




        self.idle_frame =(self.idle_frame + self.die_animation_speed * frame_time) % 4

        pass

    def boss_cutscene_on(self,frame_time):
        self.cutscene_timer+=frame_time
        if self.cutscene_timer>=self.cutscene_time:
            self.cutscene=True
            self.speed=100
        else:
            self.y -=self.speed*frame_time
            canvas_size.start_shake(0.1, 3)



        pass

    def move(self, frame_time):
        if self.pattern_num==0:
            self.pattern0(frame_time)
        elif self.pattern_num==1:
            self.pattern1(frame_time)
        elif self.pattern_num==2:
            self.pattern2(frame_time)

    def pattern0(self,frame_time):


        if not self.pattern_ready:
            x,y=self.width,self.height
            self.x,self.y=distance_funtion(self.x,self.y,x,y,frame_time,self.pattern_ready_speed)
            if abs(self.x-x)<=5 and abs(self.y-y)<=5:
                self.pattern_ready=True
        elif self.pattern0_ready_timer<self.pattern0_ready_time:
            self.pattern0_ready_timer+=frame_time
        else:
            self.pattern_state=2
            self.x+=self.speed*6*frame_time


            if self.x>=canvas_size.canvaswidth+50:
                self.rereset()
            
        pass
    def pattern1(self,frame_time):

        if not self.pattern_ready:
            self.x,self.y=distance_funtion(self.x,self.y,self.pattern1_x,self.pattern1_y,frame_time,self.pattern_ready_speed)
            if abs(self.x-self.pattern1_x)<=5 and abs(self.y-self.pattern1_y)<=5:
                self.pattern_ready=True
        elif self.pattern0_ready_timer<self.pattern0_ready_time:
            self.pattern0_ready_timer+=frame_time
            self.pattern1_x, self.pattern1_y = ramona.Ramona_POS_X, ramona.Ramona_POS_Y
        else:
            self.pattern_state=3
            self.x, self.y = distance_funtion(self.x, self.y, self.pattern1_x, self.pattern1_y, frame_time,self.speed*6)
            self.pattern1_frame = (self.pattern1_frame + self.die_animation_speed * frame_time) % 5

            if abs(self.x - self.pattern1_x) <= 5 and abs(self.y - self.pattern1_y) <= 5 and self.pattern_ready:
                self.rereset()

        pass
    def pattern2(self,frame_time):

        self.x,self.y=distance_funtion(self.x,self.y,ramona.Ramona_POS_X,ramona.Ramona_POS_Y,frame_time,self.speed)

        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.7

        self.attack_timer+=frame_time
        if self.attack_timer>=self.attack_time or self.hit_num<=0:
            self.attack_timer=0
            self.pattern_ready_timer=0
            self.pattern_num=self.prev_pattern
        pass

    def rereset(self):
        self.pattern_num = 2
        self.prev_pattern = (self.prev_pattern + 1) % 2
        self.pattern_ready = False
        self.pattern0_ready_timer = 0.0
        self.pattern_state = 0
        self.x = randint(int(self.width), int(canvas_size.canvaswidth - self.width))
        self.y = canvas_size.canvasheight+self.height
        self.hit= 5 if self.hp%100==0 else int((self.hp-int(self.hp/100))/20)
        self.pattern1_x, self.pattern1_y = randint(int(self.width),
        int(canvas_size.canvaswidth - self.width)), canvas_size.canvasheight // 2 + canvas_size.canvasheight // 4

    def ramonatoghost(self):
        if collide([ramona.Ramona_POS_X,ramona.Ramona_POS_Y,ramona.Ramona_SIZE_X,ramona.Ramona_SIZE_Y],
                   [self.x,self.y,self.width,self.height]) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible and not self.die_animation:
            if ramona.CURRENT_HP>0:
                ramona.CURRENT_HP-=1
                ramona.Ramona_invincible=True
                ramona.invincible_timer=0.0
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
                a = boss_ghost_die_coordinate[int(self.die_frame)]
            elif self.hit_animation:
                a = boss_ghost_hit_coordinate[int(self.hit_frame)]
            elif self.pattern_state==1:
                a = boss_ghost_pattern1_coordinate[0]
            elif self.pattern_state==2:
                a = boss_ghost_pattern1_coordinate[1]
            elif self.pattern_state==3:
                a = boss_ghost_pattern2_coordinate[int(self.pattern1_frame)]
            else:  a = boss_ghost_idle_coordinate[int(self.idle_frame)]

            left, bottom, width, height, jx, jy = a


            self.image.clip_composite_draw(left, bottom, width, height, 0, 'h', self.x + jx-canvas_size.camera_x, self.y + jy-canvas_size.camera_y, width*SIZE, height*SIZE)


            if not self.die_animation and self.cutscene and self.pattern_ready_timer>= self.pattern_ready_time and self.hit_num>0 and self.pattern_num==3:
                self.shape.draw()

