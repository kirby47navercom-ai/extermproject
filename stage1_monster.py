import stage1_phase1

ghost_phase1_far=50
ghost_phase1_pos=[-1,-1,1,1,1]


class Stage1_Monster:
    def __init__(self):
        self.phase_num=0
        self.phase=[]
        self.phase.append(stage1_phase1.Stage1_Phase1())

    def update(self, frame_time, events=None):


        self.phase[self.phase_num].update(frame_time,events)


        if self.phase[self.phase_num].phase1.__len__()==0:
            self.phase_num+=1
            self.update(frame_time,events)

        pass
    def draw(self):
        self.phase[self.phase_num].draw()
        pass