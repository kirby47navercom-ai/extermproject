from pico2d import *

import background
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


class Boss_Kitty:
    image = None
    attack1_image=None
    attack2_image=None
    little_image = None
    def __init__(self):
        self.pattern_set = get_pattern_set()
        if Boss_Kitty.image == None:
            Boss_Kitty.image = [load_image('2stage\\boss1.png'),load_image('2stage\\boss2.png')]

        self.x, self.y = canvas_size.canvaswidth-300, canvas_size.canvasheight//2
        self.boss_hp=300
        self.hp = self.boss_hp
        self.hp_bar = Boss_HP()
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
        self.shape.y = self.y + self.height * 0.2

        self.current_pattern = 2

        self.attack_start=False
        self.attack_init=False

        self.hit = False
        self.hit_animation = False
        self.hit_time = 0.0

        self.die = False
        self.die_animation = False
        self.die_animation_speed = 2.0
        self.die_frame = 0

        if Boss_Kitty.attack1_image == None:
            Boss_Kitty.attack1_image = resource.boss_kitty_attack_image
        self.attack1= []
        self.attack1_effect=[] #현재 위치  크기 프레임
        self.attack1_time = 0.0
        self.attack1_timer = 0.2
        self.attack1_frame=0
        self.attack1_num=8
        self.attack1_player_speed=1200.0
        self.attack1_speed=40.0
        self.attack1_effect_speed=8.0

        if Boss_Kitty.attack2_image == None:
            Boss_Kitty.attack2_image = resource.boss_kitty_uibim_image
        self.attack2=[]
        self.attack2_init=False
        self.attack2_init_speed = 300
        self.attack2_init_time = 0.0
        self.attack2_init_timer = 2.0
        self.attack2_time = 0.0
        self.attack2_timer = 2.0
        self.attack2_frame = 0
        self.attack2_num = 3
        self.attack2_speed = 40.0

        if Boss_Kitty.little_image == None:
            Boss_Kitty.little_image = load_image('2stage\\157.png')
        self.attack3=[]
        self.attack3_init=False
        self.attack3_init_speed = 300
        self.attack3_init_time = 0.0
        self.attack3_init_timer = 2.0
        self.attack3_time = 0.0
        self.attack3_timer = 2.0
        self.attack3_frame = 0
        self.attack3_num = 8
        self.attack3_speed = 40.0
        # ▼▼▼ [추가] 패턴 3(꼬마 키티)용 변수 ▼▼▼
        self.attack3_spawn_interval = 0.5  # 0.5초마다 1마리씩 스폰
        self.attack3_spawned_count = 0  # 지금까지 스폰한 횟수
        self.attack3_vertical_speed = 150.0  # 낙하 속도
        self.attack3_dance_amplitude = 50.0  # 좌우로 흔들리는 폭
        self.attack3_dance_frequency = 3.0  # 좌우로 흔들리는 빠르기

        # 리소스에서 꼬마 키티의 크기 정보를 미리 가져옴
        w, h = resource.little_kitty_idle_coordinate[2:4]
        self.attack3_kitty_size = (w, h)

        self.idle_frame = 0
        self.animation_speed = 4.0

        self.die=False
        pass

    def update(self, frame_time, events=None):

        self.idle_frame = (self.idle_frame + self.animation_speed * frame_time) % 2

        if not (self.current_pattern==1 and self.attack2_init):
            self.move(frame_time)

        if self.attack_start:
            if self.current_pattern == 0:
                self.pattern0(frame_time)
            elif self.current_pattern == 1:
                self.pattern1(frame_time)
            elif self.current_pattern == 2:
                self.pattern2(frame_time)
            elif self.current_pattern == 3:
                self.pattern3(frame_time)

        if self.attack1_effect.__len__()>0:
            for i in range(len(self.attack1_effect)-1, -1, -1):
                self.attack1_effect[i][4]=(self.attack1_effect[i][4] + self.attack1_speed * frame_time) % 28
                self.attack1_effect[i][2]-=self.attack1_effect_speed*frame_time
                self.attack1_effect[i][3]-=self.attack1_effect_speed*frame_time
                if self.attack1_effect[i][2]<=0 or self.attack1_effect[i][3]<=0:
                    self.attack1_effect.pop(i)
                pass
        if not self.die_animation and self.hp>0:
            self.shape.x = self.x
            self.shape.y = self.y + self.height * 0.2

        if self.hit_animation:
            self.hit_kitty_animation()
        if self.hit:
            self.hit_timer(frame_time)

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


                if self.attack1[i][0]<-50 or self.ramonatoattack0(i):
                    canvas_size.start_shake(0.1, 5)
                    self.attack1_num -=1
                    self.attack1.pop(i)
                    if self.attack1_num==0:
                        break
                    self.attack1.append([self.x, self.y, 0, ramona.Ramona_POS_X, ramona.Ramona_POS_Y,0.0])

                pass

            if self.attack1_num==0:
                self.current_pattern=1
                self.attack_init=True
                self.attack2_init = True
                self.attack1_num=5


        pass

    def pattern1(self, frame_time):
        if self.attack_init:
            x,self.y = canvas_size.distance_funtion(0,self.y,0,ramona.Ramona_POS_Y,frame_time,self.attack2_init_speed)
            self.attack2_init_time += frame_time
            if self.attack2_init_time>self.attack2_init_timer:
                self.attack_init=False
                self.attack2_init_time=0.0
                self.attack2.append([ramona.Ramona_POS_Y,0,0.0,0])#플레이어 y, 프레임, 타이머, 공격 타입
            pass

        else:
            for i in range(len(self.attack2)-1, -1, -1):
                if self.attack2[i][3]==0:
                    self.attack2[i][2]+=frame_time
                    if self.attack2[i][2]>self.attack2_timer:
                        self.attack2_init = False
                        self.attack2[i][3]=1
                        self.attack2[i][2] = 0.0
                        self.attack2[i][1] = 0
                        canvas_size.start_shake(1,10)
                        if self.attack2_num>0:
                            self.attack2_num-=1
                            self.attack2.append([ramona.Ramona_POS_Y, 0, 0.0, 0])

                elif self.attack2[i][3]==1:
                    if self.attack2[i][2] < self.attack2_timer-1.0:
                        if self.attack2[i][1]<3:
                            self.attack2[i][1] = (self.attack2[i][1] + self.attack2_speed * frame_time)
                        self.ramonatoattack1(self.attack2[i])
                        self.attack2[i][2] += frame_time
                    else:
                        self.attack2[i][1] = (self.attack2[i][1] + self.attack2_speed * frame_time*0.7)
                        if int(self.attack2[i][1])>6:
                            self.attack2.pop(i)
            if self.attack2_num==0 and self.attack2.__len__()==0:
                self.current_pattern=2
                self.attack_init=False
                self.attack2_init=False
                self.attack2_num=3



    def pattern2(self, frame_time):
        # 1. 준비(Wind-up) 단계: 공격 시작 전 2초 대기
        if not self.attack_init:
            self.attack3_init_time += frame_time
            self.attack_init = True  # 공격 시작
            self.attack3_time = 0.0  # 스폰 타이머 초기화
            self.attack3_spawned_count = 0  # 스폰 카운트 초기화

        # 2. 공격(Attack) 단계: 꼬마 키티 스폰 및 업데이트
        else:
            # --- 2-1. 스폰 로직 ---
            self.attack3_time += frame_time
            # 8마리 미만으로 스폰했고, 스폰 간격이 되었다면
            if self.attack3_spawned_count < self.attack3_num and self.attack3_time >= self.attack3_spawn_interval:
                # 화면 상단 랜덤 x 위치에 꼬마 키티 생성
                origin_x = randint(5, canvas_size.canvaswidth//2 - 40)
                # [중심x, 현재y, sin파동을 위한 내부시간]
                self.attack3.append([origin_x, canvas_size.canvasheight + 50, 0.0])
                self.attack3_time = 0.0  # 스폰 타이머 리셋
                self.attack3_spawned_count += 1

            # --- 2-2. 꼬마 키티 이동 및 충돌/삭제 로직 (리스트를 거꾸로 순회) ---
            for i in range(len(self.attack3) - 1, -1, -1):
                kitty = self.attack3[i]

                # 내부 시간 증가 (sin 함수에 사용)
                kitty[2] += frame_time
                # y좌표 감소 (낙하)
                kitty[1] -= self.attack3_vertical_speed * frame_time

                # 춤추는 x좌표 계산
                current_x = kitty[0] + self.attack3_dance_amplitude * math.sin(kitty[2] * self.attack3_dance_frequency)

                # 플레이어와 충돌 검사
                kitty_w, kitty_h = self.attack3_kitty_size
                kitty_box = (current_x, kitty[1], kitty_w, kitty_h)
                player_box = (ramona.Ramona_POS_X, ramona.Ramona_POS_Y, ramona.Ramona_SIZE_X, ramona.Ramona_SIZE_Y)

                if resource.collide(player_box,
                                    kitty_box) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible:
                    ramona.CURRENT_HP -= 1
                    ramona.Ramona_invincible = True
                    canvas_size.start_shake(0.5, 5.0)

                # 화면 밖으로 나가면 제거
                elif kitty[1] < -50:
                    self.attack3.pop(i)

            # --- 2-3. 패턴 종료 로직 ---
            # 8마리 스폰이 끝났고, 화면에 남은 꼬마 키티도 없으면
            if self.attack3_spawned_count == self.attack3_num and len(self.attack3) == 0:
                self.current_pattern = 3  # "패턴 4"로 이동 (pattern3 함수가 필요함)
                self.attack_init = False  # 다음 패턴을 위해 wind-up 상태로
                self.attack3_init_time = 0.0
                self.attack3_spawned_count = 0
        pass
    def pattern3(self, frame_time):
        pass

    def rereset(self):
        pass
    def ramonatoattack0(self,i):
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
    def ramonatoattack1(self,i):
        b = resource.collide([ramona.Ramona_POS_X,ramona.Ramona_POS_Y,ramona.Ramona_SIZE_X,ramona.Ramona_SIZE_Y],
                   [canvas_size.canvaswidth//2,i[0],boss_kitty_uibim_coordinate[int(i[1])][2],int(boss_kitty_uibim_coordinate[int(i[1])][3]//2)]) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible
        if b:
            if ramona.CURRENT_HP>0:
                ramona.CURRENT_HP-=1
                ramona.Ramona_invincible=True
                ramona.invincible_timer=0.0
                canvas_size.start_shake(0.5, 5.0)

    def hit_kitty_animation(self):
        self.shape = self.pattern_set[randint(0,pattern_number)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.2
        self.hit_animation = False
        self.hit=True
        pass
    def hit_timer(self,frame_time):
        self.hit_time += frame_time
        if self.hit_time>0.5:
            self.hit=False
            self.hit_time=0.0
        pass


    def die_kitty(self):
        pass

    def die_kitty_animation(self, frame_time):
        pass

    def draw(self):



        bx,by = boss_kitty_idle_coordinate[int(self.idle_frame)][2:4]

        if background.start:
            # ▼▼▼ [추가] 꼬마 키티(attack3) 그리기 ▼▼▼
            if len(self.attack3) > 0:
                w, h = self.attack3_kitty_size
                # 리소스 파일에서 꼬마 키티의 스프라이트 정보 가져오기
                left, bottom, width, height, jx, jy = resource.little_kitty_idle_coordinate

                for kitty in self.attack3:
                    origin_x, current_y, internal_time = kitty
                    # 춤추는 x좌표 계산
                    current_x = origin_x + self.attack3_dance_amplitude * math.sin(internal_time * self.attack3_dance_frequency)

                    self.little_image.clip_draw(left, bottom, width, height,current_x - canvas_size.camera_x,current_y - canvas_size.camera_y, w * 1.5, h * 1.5)


            if self.attack1_num > 0 and self.attack1.__len__()>0:
                for i in self.attack1:
                    ax,ay= boss_kitty_attack_coordinate[int(i[2])][2:4]
                    Boss_Kitty.attack1_image[int(i[2])].clip_draw(0,0,ax,ay,i[0]-canvas_size.camera_x,i[1]-canvas_size.camera_y,ax*1.5,ay*1.5)

            if  self.attack2.__len__()>0:
                for i in self.attack2:
                    ax,ay= boss_kitty_uibim_coordinate[int(i[1])][2:4]
                    Boss_Kitty.attack2_image[int(i[1])].clip_draw(0,0,ax,ay,self.x - 100 - canvas_size.camera_x,i[0]-canvas_size.camera_y,ax*1.5,ay*0.5)

            if self.attack1_effect.__len__()>0:
                for i in self.attack1_effect:
                    ex,ey= boss_kitty_attack_coordinate[int(i[4])][2:4]
                    Boss_Kitty.attack1_image[int(i[2])].clip_draw(0,0,ex,ey,i[0]-canvas_size.camera_x,i[1]-canvas_size.camera_y,i[2],i[3])

            if self.hit:
                if (get_time() % 0.2) > 0.1:
                    self.image[int(self.idle_frame)].clip_draw(0, 0, bx, by, self.x-canvas_size.camera_x, self.y-canvas_size.camera_y, bx * SIZE, by * SIZE)
            else:
                self.image[int(self.idle_frame)].clip_draw(0, 0, bx, by, self.x-canvas_size.camera_x, self.y-canvas_size.camera_y, bx * SIZE, by * SIZE)

            if not self.die_animation:
                self.shape.draw(0.6,0.6)
                self.hp_bar.draw(self.hp, self.boss_hp)



