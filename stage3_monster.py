import draw_gesture
import background_3stage
import stage3_topography
import siho
import ramona
from random import randint


class Stage3_Monster:
    def __init__(self):
        self.phase_num=0
        self.phase=[]
        self.boss=siho.Boss_Siho
        self.floor_num=randint(1,3)
        self.floor = stage3_topography.Stage3_Terrain(self.floor_num)




    def update(self, frame_time, events=None):

            self.floor.update(frame_time, events)
            #self.shape_check()

    def shape_check(self):
        if self.boss.shape.name == draw_gesture.result and self.boss.hp>0:
            self.boss.hp -= ramona.Ramona_attack
            ramona.Ramona_smash = True
            self.boss.hit_animation=True
            if self.boss.hp <= 0:
                self.boss.hp = 0
                self.boss.die_animation=True

        draw_gesture.result = None

        pass

    def monster_die(self):
        if self.boss.die:
            pass




    def draw(self):
        self.floor.draw()

