from pico2d import *

open_canvas(1920,1200)
grass = load_image('grass.png')
ramona = (load_image('Ramona\\Ramona_idle.png'),load_image('Ramona\\Ramona_walk.png'),load_image('Ramona\\Ramona_run.png'),load_image('Ramona\\Ramona_jump.png'),
          load_image('Ramona\\Ramona_double_jump.png'),load_image('Ramona\\Ramona_hit.png'),load_image('Ramona\\Ramona_evade.png'),load_image('Ramona\\Ramona_getup.png'),
          load_image('Ramona\\Ramona_dead.png'),load_image('Ramona\\Ramona_revived.png'),load_image('Ramona\\Ramona_stageclear.png'),
          load_image('Ramona\\Ramona_gameclear.png'),load_image('Ramona\\Ramona_action1.png'),load_image('Ramona\\Ramona_action2.png'),load_image('Ramona\\Ramona_action3.png'),
          load_image('Ramona\\Ramona_action4.png'),load_image('Ramona\\Ramona_action5.png'),load_image('Ramona\\Ramona_action6.png'))
ramona_idle_coordinate = [
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


frame = 0
x,y=400,300



def ramona_idle_ani():
    for i in range(2):
        for j in ramona_idle_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[0].clip_composite_draw(left, bottom, width, height, 0, '', x, y, width*2, height*2)
            update_canvas()
            delay(0.1)
def ramona_walk_ani():
    global x,y
    for i in range(2):

        for j in ramona_walk_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[1].clip_composite_draw(left, bottom, width, height, 0, '', x, y, width*2, height*2)
            x+=5
            update_canvas()
            delay(0.1)
    x,y=400,300
def ramona_run_ani():
    global x, y
    for i in range(2):
        for j in ramona_run_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[2].clip_composite_draw(left, bottom, width, height, 0, '', x, y, width*2, height*2)
            x += 5
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_jump_ani():
    global x, y
    z=False
    for i in range(2):
        z = False
        x, y = 400, 300
        for j in ramona_jump_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[3].clip_composite_draw(left, bottom, width, height, 0, '', x, y, width*2, height*2)
            if z==False:
                y += 20
                if y>=380:
                    z=True
            elif z==True:
                y -= 20
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_double_jump_ani():
    global x, y
    z = False
    for i in range(2):
        z = False
        x, y = 400, 300
        for j in ramona_double_jump_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[4].clip_composite_draw(left, bottom, width, height, 0, '', x, y, width*2, height*2)
            if z == False:
                y += 20
                if y >= 340:
                    z = True
            elif z == True:
                y -= 20
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_hit_ani():
    global x, y
    for i in range(2):
        z = False
        x, y = 400, 300
        for j in ramona_hit_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[5].clip_composite_draw(left, bottom, width, height, 0, '', x, y, width*2, height*2)
            if z == False:
                x -= 10
                if x >= 360:
                    z = True
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_evade_ani():
    global x, y
    for i in range(2):
        for j in ramona_evade_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[6].clip_composite_draw(left, bottom, width, height, 0, '', x, y, width*2, height*2)
            x+=10
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_getup_ani():
    global x, y
    for i in range(2):
        for j in ramona_getup_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[7].clip_composite_draw(left, bottom, width, height, 0, '', x, y, width*2, height*2)
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_dead_ani():
    global x, y
    for i in range(2):
        for j in ramona_dead_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[8].clip_composite_draw(left, bottom, width, height, 0, '', x, y, width*2, height*2)
            #x-=5
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_revive_ani():
    global x, y
    for i in range(2):
        for j in ramona_revive_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[9].clip_composite_draw(left, bottom, width, height, 0, '', x, y, width*2, height*2)
            #x-=5
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_stageclear_ani():
    global x, y

    for i in range(2):
        x, y = 400, 300
        z = False
        for j in ramona_stageclear_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[10].clip_composite_draw(left, bottom, width, height, 0, '', x, y, width*2, height*2)
            if z==False:
                y+=10
                if y>=330:
                    z=True
            elif z==True:
                y-=10

            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_gameclear_ani():
    global x, y

    for i in range(2):
        x, y = 400, 300
        z = False
        for j in ramona_gameclear_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[11].clip_composite_draw(left, bottom, width, height, 0, '', x, y, width*2, height*2)
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_action1_ani():
    global x, y

    for i in range(2):
        x, y = 400, 300
        z = False
        for j in ramona_action1_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[12].clip_composite_draw(left, bottom, width, height, 0, '', x+jx, y+jy, width*2, height*2)
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_action2_ani():
    global x, y
    for i in range(2):
        x, y = 400, 300
        z = False
        for j in ramona_action2_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[13].clip_composite_draw(left, bottom, width, height, 0, '', x+jx, y+jy, width*2, height*2)
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_action3_ani():
    global x, y
    for i in range(2):
        x, y = 400, 300
        z = False
        for j in ramana_action3_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[14].clip_composite_draw(left, bottom, width, height, 0, '', x+jx, y+jy, width*2, height*2)
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_action4_ani():
    global x, y
    for i in range(2):
        x, y = 400, 300
        z = False
        for j in ramona_action4_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[15].clip_composite_draw(left, bottom, width, height, 0, '', x+jx, y+jy, width*2, height*2)
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_action5_ani():
    global x, y
    for i in range(2):
        x, y = 400, 300
        z = False
        for j in ramona_action5_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[16].clip_composite_draw(left, bottom, width, height, 0, '', x+jx, y+jy, width*2, height*2)
            update_canvas()
            delay(0.1)
    x, y = 400, 300
def ramona_action6_ani():
    global x, y
    for i in range(2):
        x, y = 400, 300
        z = False
        for j in ramona_action6_coordinate:
            clear_canvas()
            grass.draw(400, 30)
            left, bottom, width, height,jx,jy = j
            ramona[17].clip_composite_draw(left, bottom, width, height, 0, '', x+jx, y+jy, width*2, height*2)
            update_canvas()
            delay(0.1)
    x, y = 400, 300

while True:


    ramona_idle_ani()
    ramona_walk_ani()
    ramona_run_ani()
    ramona_jump_ani()
    ramona_double_jump_ani()
    ramona_hit_ani()
    ramona_evade_ani()
    ramona_getup_ani()
    ramona_dead_ani()
    ramona_revive_ani()
    ramona_stageclear_ani()
    ramona_gameclear_ani()
    ramona_action1_ani()
    ramona_action2_ani()
    ramona_action3_ani()
    ramona_action4_ani()
    ramona_action5_ani()
    ramona_action6_ani()

    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                close_canvas()


