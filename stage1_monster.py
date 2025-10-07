import stage1_phase1

ghost_phase1_far=50
ghost_phase1_pos=[-1,-1,1,1,1]


class Stage1_Monster:
    def __init__(self):
        self.phase_num=1
        self.phase=[]
        self.phase.append(stage1_phase1.Stage1_Phase1())

    def update(self, frame_time, events=None):
        if self.phase_num==1:
            self.phase[0].update(frame_time,events)
        pass
    def draw(self):
        if self.phase_num==1:
            self.phase[0].draw()
        pass