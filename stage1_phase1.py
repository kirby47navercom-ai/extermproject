from ghost_normal import *
import draw_gesture

ghost_phase1_far=50
ghost_phase1_pos=[-1,-1,1,1,1]

class Stage1_Phase1:
    def __init__(self):
        self.phase1=[Ghost() for _ in range(5)]
        for i in range(self.phase1.__len__()):
            self.phase1[i].x=0 if ghost_phase1_pos[i] == -1 else canvaswidth+ghost_phase1_pos[i]*ghost_phase1_far
            self.phase1[i].y=random.randint(0,canvasheight)



        pass
    def update(self, frame_time, events=None):
        self.phase1[self.phase1.__len__()-1].update(frame_time,events)

        self.shape_check()
        self.monster_die()
        pass

    def shape_check(self):
        if self.phase1[self.phase1.__len__()-1].shape.name==draw_gesture.result:
            self.phase1[self.phase1.__len__()-1].hp-=ramona.Ramona_attack
            self.phase1[self.phase1.__len__()-1].hit_animation=True
            self.phase1[self.phase1.__len__()-1].hit_frame = 0
            ramona.Ramona_smash = True
            canvas_size.start_shake(0.5, 5.0)

        draw_gesture.result=None

        pass
    def monster_die(self):
        if self.phase1[self.phase1.__len__()-1].die:
            self.phase1.pop(self.phase1.__len__()-1)
        pass
    def draw(self):
        self.phase1[self.phase1.__len__()-1].draw()
        pass