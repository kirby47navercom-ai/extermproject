import draw_gesture
import background_1stage
import hellkitty
import ramona


class Stage2_Monster:
    def __init__(self):
        self.phase_num=0
        self.phase=[]
        self.boss = hellkitty.Boss_Kitty()


    def update(self, frame_time, events=None):
        if '하트' == draw_gesture.result:
            background_1stage.start=True
            draw_gesture.result = None
            self.boss.attack_start=True
        elif background_1stage.start:
            self.boss.update(frame_time, events)
            self.shape_check()
            self.monster_die()
            pass

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
        pass


        pass
    def draw(self):
        if background_1stage.start:
            self.boss.draw()
            pass
