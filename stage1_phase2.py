from ghost_normal import *
import draw_gesture

ghost_phase_far=50
ghost_phase_pos=[-1,1,-1,1,-1,1,-1,1]

class Stage1_Phase2:
    def __init__(self):
        self.phase=[Ghost() for _ in range(ghost_phase_pos.__sizeof__())]
        for i in range(self.phase.__len__()):
            self.phase[i].x=0 if ghost_phase_pos[i] == -1 else canvaswidth+ghost_phase_pos[i]*ghost_phase_far
            self.phase[i].y=random.randint(0,canvasheight)

        self.num = 2

        pass
    def update(self, frame_time, events=None):

        for i in range(self.num):
            self.phase[i].update(frame_time,events)

        self.shape_check()
        self.monster_die()
        pass

    def shape_check(self):
        for i in range(self.num):
            if self.phase[self.phase.__len__()-1].shape.name==draw_gesture.result:
                self.phase[self.phase.__len__()-1].hp-=ramona.Ramona_attack
                self.phase[self.phase.__len__()-1].hit_animation=True
                self.phase[self.phase.__len__()-1].hit_frame = 0
                ramona.Ramona_smash = True
                canvas_size.start_shake(0.5, 5.0)

        draw_gesture.result=None

        pass
    def monster_die(self):
        if self.phase[self.phase.__len__()-1].die:
            self.phase.pop(self.phase.__len__()-1)
            self.num -= 1
            if self.num == 0: self.num = 2
        pass
    def draw(self):
        self.phase[self.phase.__len__()-1].draw()
        pass