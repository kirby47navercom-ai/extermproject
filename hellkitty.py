from pico2d import *

import background
from pattern import *
from resource import *
from random import randint
import canvas_size
from canvas_size import cout
import ramona
import resource
import math

SIZE = 1


class Boss_Kitty:
    image = None
    attack1_image=None
    little_image = None
    def __init__(self):
        self.pattern_set = get_pattern_set()
        if Boss_Kitty.image == None:
            Boss_Kitty.image = [load_image('2stage\\boss1.png'),load_image('2stage\\boss2.png')]
        if Boss_Kitty.attack1_image == None:
            Boss_Kitty.attack1_image = resource.boss_kitty_attack_image
        if Boss_Kitty.little_image == None:
            Boss_Kitty.little_image = load_image('2stage\\157.png')

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
        self.attack_init=False

        self.attack1= []
        self.attack1_effect=[] #현재 위치  크기 프레임
        self.attack1_time = 0.0
        self.attack1_timer = 0.2
        self.attack1_frame=0
        self.attack1_num=8
        self.attack1_player_speed=1200.0
        self.attack1_speed=40.0
        self.attack1_effect_speed=8.0

        self.attack2=[]
        self.attack2_init=False
        self.attack2_init_speed = 300
        self.attack2_effect = []
        self.attack2_time = 0.0
        self.attack2_timer = 0.2
        self.attack2_frame = 0
        self.attack2_num = 8
        self.attack2_player_speed = 800.0
        self.attack2_speed = 40.0
        self.attack2_effect_speed = 8.0

        self.idle_frame = 0
        self.animation_speed = 4.0

        self.die=False
        pass

    def update(self, frame_time, events=None):

        self.idle_frame = (self.idle_frame + self.animation_speed * frame_time) % 2

        if not self.attack2_init:
            self.move(frame_time)

        if self.attack_start:
            if self.current_pattern == 0:
                self.pattern0(frame_time)
            elif self.current_pattern == 1:
                self.pattern1(frame_time)
            elif self.current_pattern == 2:
                self.pattern2(frame_time)
            elif self.current_pattern == 3:
                self.pattern2(frame_time)

        if self.attack1_effect.__len__()>0:
            for i in range(len(self.attack1_effect)-1, -1, -1):
                self.attack1_effect[i][4]=(self.attack1_effect[i][4] + self.attack1_speed * frame_time) % 28
                self.attack1_effect[i][2]-=self.attack1_effect_speed*frame_time
                self.attack1_effect[i][3]-=self.attack1_effect_speed*frame_time
                if self.attack1_effect[i][2]<=0 or self.attack1_effect[i][3]<=0:
                    self.attack1_effect.pop(i)
                pass


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
        if not self.attack_init:
            self.attack1.append([self.x, self.y,0,ramona.Ramona_POS_X,ramona.Ramona_POS_Y,0.0])#현재 위치, 프레임, 캐릭 위치 점점 늘어남, 이펙트 나오는 시간
            canvas_size.start_shake(0.1, 5)
            self.attack_init = True
            pass
        else:
            for i in range(len(self.attack1)-1, -1, -1):
                self.attack1[i][2]= (self.attack1[i][2] + self.attack1_speed * frame_time) % 28
                self.attack1[i][0],self.attack1[i][1],self.attack1[i][3],self.attack1[i][4]=canvas_size.distance_funtion2(self.attack1[i][0],self.attack1[i][1],self.attack1[i][3],self.attack1[i][4],frame_time,self.attack1_player_speed,self.attack1[i][3],self.attack1[i][4])
                self.attack1[i][5]+=frame_time

                if self.attack1[i][5]>self.attack1_timer:
                    self.attack1_effect.append([self.attack1[i][0],self.attack1[i][1],20,20,0])
                    self.attack1[i][5]=0


                if self.attack1[i][0]<-50 or self.ramonatoattack1(i):
                    canvas_size.start_shake(0.1, 5)
                    self.attack1_num -=1
                    self.attack1.pop(i)
                    if self.attack1_num==0:
                        break
                    self.attack1.append([self.x, self.y, 0, ramona.Ramona_POS_X, ramona.Ramona_POS_Y,0.0])

                pass

            if self.attack1_num==0:
                self.current_pattern=1
                self.attack_init=False
                self.attack1_num=5
                self.attack2_init=True


        pass

    def pattern1(self, frame_time):
        if not self.attack_init:
            x,self.y = canvas_size.distance_funtion(0,self.y,0,ramona.Ramona_POS_Y,frame_time,self.attack2_init_speed)

            pass
        else:
            pass

        pass

    def pattern2(self, frame_time):

        pass

    def rereset(self):
        pass
    def ramonatoattack1(self,i):
        ax, ay = self.attack1[i][0], self.attack1[i][1]
        rx, ry = ramona.Ramona_POS_X, ramona.Ramona_POS_Y
        threshold = 40  # 충돌 반경: 필요에 따라 조정
        dx = ax - rx
        dy = ay - ry
        b = dx * dx + dy * dy <= threshold * threshold and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible
        if b:
            if ramona.CURRENT_HP>0:
                ramona.CURRENT_HP-=1
                ramona.Ramona_invincible=True
                ramona.invincible_timer=0.0
                canvas_size.start_shake(0.5, 5.0)
        return b

    def hit_kitty_animation(self, frame_time):
        pass

    def die_kitty(self):
        pass

    def die_kitty_animation(self, frame_time):
        pass

    def draw(self):



        bx,by = boss_kitty_idle_coordinate[int(self.idle_frame)][2:4]

        if background.start:

            if self.attack1_num > 0 and self.current_pattern==0 and self.attack1.__len__()>0:
                for i in self.attack1:
                    ax,ay= boss_kitty_attack_coordinate[int(i[2])][2:4]
                    Boss_Kitty.attack1_image[int(i[2])].clip_draw(0,0,ax,ay,i[0]-canvas_size.camera_x,i[1]-canvas_size.camera_y,ax*1.5,ay*1.5)
            if self.attack1_effect.__len__()>0:
                for i in self.attack1_effect:
                    ex,ey= boss_kitty_attack_coordinate[int(i[4])][2:4]
                    Boss_Kitty.attack1_image[int(i[2])].clip_draw(0,0,ex,ey,i[0]-canvas_size.camera_x,i[1]-canvas_size.camera_y,i[2],i[3])




            self.image[int(self.idle_frame)].clip_draw(0, 0, bx, by, self.x-canvas_size.camera_x, self.y-canvas_size.camera_y, bx * SIZE, by * SIZE)


        pass

