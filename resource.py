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
ramona_coordinate = {'idle': ramona_coordinate, 'walk': ramona_walk_coordinate, 'run': ramona_run_coordinate,
                     'jump': ramona_jump_coordinate, 'double_jump': ramona_double_jump_coordinate,
                     'hit': ramona_hit_coordinate, 'evade': ramona_evade_coordinate, 'getup': ramona_getup_coordinate,
                     'dead': ramona_dead_coordinate, 'revive': ramona_revive_coordinate, 'stageclear': ramona_stageclear_coordinate,
                     'gameclear': ramona_gameclear_coordinate, 'action1': ramona_action1_coordinate, 'action2': ramona_action2_coordinate,
                     'action3': ramana_action3_coordinate, 'action4': ramona_action4_coordinate, 'action5': ramona_action5_coordinate, 'action6': ramona_action6_coordinate}

image_idle = None
image_walk = None
image_run = None
image_jump = None
image_double_jump = None
image_hit = None
image_evade = None
image_getup = None
image_dead = None
image_revived = None
image_stageclear = None
image_gameclear = None
image_action1 = None
image_action2 = None
image_action3 = None
image_action4 = None
image_action5 = None
image_action6 = None

ramona_image = {}  # 비어있는 dict 준비

# 함수로 묶기
def load_resources():
    global image_idle, image_walk, image_run, image_jump, image_double_jump
    global image_hit, image_evade, image_getup, image_dead, image_revived
    global image_stageclear, image_gameclear
    global image_action1, image_action2, image_action3, image_action4, image_action5, image_action6
    global ramona_image

    image_idle = load_image('Ramona\\Ramona_idle.png')
    image_walk = load_image('Ramona\\Ramona_walk.png')
    image_run = load_image('Ramona\\Ramona_run.png')
    image_jump = load_image('Ramona\\Ramona_jump.png')
    image_double_jump = load_image('Ramona\\Ramona_double_jump.png')
    image_hit = load_image('Ramona\\Ramona_hit.png')
    image_evade = load_image('Ramona\\Ramona_evade.png')
    image_getup = load_image('Ramona\\Ramona_getup.png')
    image_dead = load_image('Ramona\\Ramona_dead.png')
    image_revived = load_image('Ramona\\Ramona_revived.png')
    image_stageclear = load_image('Ramona\\Ramona_stageclear.png')
    image_gameclear = load_image('Ramona\\Ramona_gameclear.png')
    image_action1 = load_image('Ramona\\Ramona_action1.png')
    image_action2 = load_image('Ramona\\Ramona_action2.png')
    image_action3 = load_image('Ramona\\Ramona_action3.png')
    image_action4 = load_image('Ramona\\Ramona_action4.png')
    image_action5 = load_image('Ramona\\Ramona_action5.png')
    image_action6 = load_image('Ramona\\Ramona_action6.png')

    ramona_image = {
        'idle': image_idle, 'walk': image_walk, 'run': image_run, 'jump': image_jump,
        'double_jump': image_double_jump, 'hit': image_hit, 'evade': image_evade,
        'getup': image_getup, 'dead': image_dead, 'revive': image_revived,
        'stageclear': image_stageclear, 'gameclear': image_gameclear, 'action1': image_action1,
        'action2': image_action2, 'action3': image_action3, 'action4': image_action4,
        'action5': image_action5, 'action6': image_action6
    }