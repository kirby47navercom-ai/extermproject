from pico2d import *
ramona_coordinate = [
    (0, 0, 30, 64,0,0),
    (33, 0, 30, 64,0,0),
    (66, 0, 29, 64,0,0),
    (99, 0, 30, 64,0,0),
    (131, 0, 31, 64,0,0),
    (165, 0, 31, 64,0,0),
]
ramona_walk_coordinate = [
    (0, 0, 28, 64,0,0),
    (31, 0, 30, 64,0,0),
    (64, 0, 33, 64,0,0),
    (100, 0, 31, 66,0,0),
    (134, 0, 29, 66,0,0),
    (166, 0, 33, 64,0,0),
]
ramona_run_coordinate =[
    (0, 0, 47, 59,0,0),
    (50, 0, 42, 65,0,0),
    (95, 5, 47, 59,0,0),
    (145, 3, 45, 59,0,0),
    (193, 0, 46, 59,0,0),
    (242, 0, 40, 65,0,0),
    (285, 5, 46, 59,0,0),
    (334, 0, 44, 61,0,0)
]
ramona_jump_coordinate =[
    (1, 0, 41, 51,0,0),
    (45, 12, 36, 65,0,0),
    (84, 14, 41, 61,0,0),
    (128, 18, 44, 58,0,0),
    (175, 20, 45, 53,0,0),
    (223, 18, 46, 56,0,0),
    (272, 14, 47, 62,0,0),
    (322, 7, 45, 69,0,0),
    (370, 0, 42, 52,0,0)
]
ramona_double_jump_coordinate =[
    (0, 0, 44, 44,0,0),
    (47, 5, 45, 34,0,0),
    (95, 0, 33, 46,0,0),
    (131, 5, 42, 39,0,0),
    (176, 5, 37, 47,0,0),
]
ramona_hit_coordinate=[
    (0, 0, 44, 65,0,0),
    (47, 0, 40, 63,0,0),
    (90, 0, 36, 63,0,0),
    (129, 0, 31, 65,0,0),
]
ramona_evade_coordinate =[
    (0, 0, 44, 64,0,0),
    (47, 0, 54, 43,0,0),
    (104, 0, 41, 43,0,0),
    (148, 0, 46, 35,0,0),
    (197, 0, 50, 41,0,0),
    (250, 0, 37, 50,0,0),
    (290, 0, 32, 56,0,0)
]
ramona_getup_coordinate =[
    (0, 0, 68, 32,0,0),
    (71, 0, 68, 32,0,0),
    (142, 2, 47, 40,0,0),
    (192, 2, 47, 42,0,0),
    (242, 3, 55, 68,0,0),
    (300, 28, 57, 43,0,0),
    (360, 8, 45, 69,0,0),
    (408, 3, 42, 52,0,0),
    (453, 3, 31, 65,0,0)
]
ramona_dead_coordinate =[
    (0, 0, 39, 62,0,0),
    (42, 9, 50, 56,0,0),
    (95, 25, 71, 43,0,0),
    (169, 38, 67, 36,0,0),
    (239, 35, 68, 45,0,0),
    (310, 30, 60, 58,0,0),
    (373, 18, 60, 62,0,0),
    (436, 0, 46, 38,0,0),
    (485, 5, 67, 30,0,0),
    (555, 5, 65, 31,0,0),
    (623, 0, 68, 28,0,0),
    (694, 0, 68, 29,0,0),
    (765, 0, 68, 29,0,0)
]
ramona_revive_coordinate =[
    (0, 0, 70, 153,0,0),
    (73, 0, 49, 142,0,0),
    (125, 0, 50, 142,0,0),
    (178, 0, 56, 93,0,0),
    (237, 0, 58, 105,0,0),
    (298, 0, 55, 115,0,0),
    (356, 0, 58, 121,0,0),
    (417, 0, 34, 126,0,0)
]
ramona_stageclear_coordinate =[
    (0, 0, 42, 52,0,0),
    (45, 0, 40, 55,0,0),
    (88, 6, 36, 68,0,0),
    (127, 8, 36, 68,0,0),
    (166, 7, 36, 68,0,0),
    (205, 6, 36, 66,0,0),
    (244, 0, 40, 65,0,0)
]
ramona_gameclear_coordinate =[
    (0, 0, 31, 67,0,0),
    (34, 0, 32, 66,0,0),
    (69, 0, 38, 60,0,0),
    (151, 0, 36, 61,0,0),
    (190, 0, 36, 61,0,0),
    (229, 0, 36, 61,0,0),
    (268, 0, 32, 62,0,0)
]
ramona_action1_coordinate =[
    (0, 0, 55, 63,0,0),
    (58, 0, 38, 82,-5,10),
    (97, 0, 56, 75,-7,9),
    (156, 0, 55, 79,-5,10),
    (214, 0, 77, 82,14,10),
    (294, 0, 69, 58,16,-2),
    (366, 0, 68, 61,16,-2),
    (437, 0, 52, 65,0,0)
]
ramona_action2_coordinate =[
    (0, 0, 52, 60,0,0),
    (55, 0, 75, 49,55,-12),
    (133, 0, 70, 50,55,-10),
    (206, 0, 60, 57,45,-4),
    (269, 0, 50, 62,35,-0)
]
ramana_action3_coordinate =[
    (0, 0, 45, 73, 0, 0),
    (48, 0, 45, 75, 0, 0),
    (96, 0, 46, 76, 0, 0),
    (145, 0, 46, 70, 0, 0),
    (194, 0, 40, 65, 0, 0)
]
ramona_action4_coordinate =[
    (0, 0, 60, 64, 0-30, 0),
    (63, 0, 60, 75, 26-30, 12),
    (126, 0, 38, 75, 30-30, 13),
    (167, 0, 99, 60, 50-30, 0),
    (269, 0, 74, 59, 75-30, -2),
    (346, 0, 73, 60, 75-30, -2),
    (422, 0, 62, 63, 60-30, 0),
    (487, 0, 52, 65, 50-30, 0)
]
ramona_action5_coordinate =[
    (0, 0, 30, 62, 0 ,0),
    (33, 0, 42, 65, 10, 0),
    (78, 0, 45, 66, 10, 0),
    (126, 0, 47, 66, 8, 0),
    (176, 0, 45, 66, 10, 0),
    (224, 0, 81, 63, 50, 0),
    (308, 0, 80, 67, 50, 8),
    (391, 0, 80, 59, 50, 0),
    (474, 0, 84, 59, 50, 0),
    (561, 0, 85, 59, 50, 0),
    (649, 0, 48, 60, 0, 0),
    (700, 0, 38, 62, 0, 0),
    (741, 0, 30, 65, 0, 0)
]
ramona_action6_coordinate =[
    (0, 0, 54, 61, 0, 0),
    (57, 0, 56, 59, 0, 0),
    (116, 0, 90, 51, 70, 0),
    (209, 0, 86, 53, 70, 0),
    (298, 0, 86, 53, 70, 0),
    (387, 0, 86, 53, 70, 0),
    (476, 0, 81, 57, 50, 0),
    (560, 0, 52, 65, 10, 8),
]


class Ramona:
    def init(self):
        self.x, self.y = 100, 150
        self.frame = 0
        self.dir = 0
        self.hp = 5
        self.state = 'idle'
        self.hittime = 0
        self.animation_speed = 8.0
        self.image_idle = load_image('Ramona\\Ramona_idle.png')
        self.image_walk = load_image('Ramona\\Ramona_walk.png')
        self.image_run = load_image('Ramona\\Ramona_run.png')
        self.image_jump = load_image('Ramona\\Ramona_jump.png')
        self.image_double_jump = load_image('Ramona\\Ramona_double_jump.png')
        self.image_hit = load_image('Ramona\\Ramona_hit.png')
        self.image_evade = load_image('Ramona\\Ramona_evade.png')
        self.image_getup = load_image('Ramona\\Ramona_getup.png')
        self.image_dead = load_image('Ramona\\Ramona_dead.png')
        self.image_revived = load_image('Ramona\\Ramona_revived.png')
        self.image_stageclear = load_image('Ramona\\Ramona_stageclear.png')
        self.image_gameclear = load_image('Ramona\\Ramona_gameclear.png')
        self.image_action1 = load_image('Ramona\\Ramona_action1.png')
        self.image_action2 = load_image('Ramona\\Ramona_action2.png')
        self.image_action3 = load_image('Ramona\\Ramona_action3.png')
        self.image_action4 = load_image('Ramona\\Ramona_action4.png')
        self.image_action5 = load_image('Ramona\\Ramona_action5.png')
        self.image_action6 = load_image('Ramona\\Ramona_action6.png')
        self.image = {'idle':self.image_idle,'walk':self.image_walk,'run':self.image_run,'jump':self.image_jump,
                      'double_jump':self.image_double_jump,'hit':self.image_hit,'evade':
                      self.image_evade,'getup':self.image_getup,'dead':self.image_dead,'revive':self.image_revived,
                      'stageclear':self.image_stageclear,'gameclear':self.image_gameclear,'action1':self.image_action1,
                        'action2':self.image_action2,'action3':self.image_action3,'action4':self.image_action4,
                        'action5':self.image_action5,'action6':self.image_action6}


    def update(self,frame_time):

        self.handle_event(self,frame_time)
        pass

    def handle_event(self,frame_time):
        global events, state
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT or event.key == ord("a") or event.key == ord("A"):
                    if event.key == SDLK_LSHIFT:
                        state = 'run'
                    else:
                        state = 'walk'
                        self.dir= -1
                        self.walk(self,True,frame_time)
                elif event.key == SDLK_RIGHT or event.key == ord("d") or event.key == ord("D"):
                    if event.key == SDLK_LSHIFT:
                        state = 'run'
                    else:
                        state = 'walk'
                        self.dir = 1
                        self.walk(self, False, frame_time)

                elif event.key == SDLK_SPACE:
                    pass

                elif event.key == SDLK_ESCAPE:
                    quit()
            elif event.type == SDL_KEYUP:
                self.state = 'idle'
            elif self.state == 'idle':
                self.idle(self,frame_time)

        if self.state != state:
            self.frame = 0

    def walk(self,flip,frame_time):
        ramona_walk_speed = 200.0
        self.x+=ramona_walk_speed * frame_time * self.dir
        self.frame = (self.frame + self.animation_speed * frame_time) % 6
        pass

    def idle(self,frame_time):
        self.frame = (self.frame + self.animation_speed * frame_time) % 6
        pass

    def draw(self):

        pass
