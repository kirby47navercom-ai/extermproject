from pico2d import *
import canvas_size
import game_framework
import home_mode
import resource


black_background = None
clear = None
food = []
perfect = None


def init():
    # 로고 이미지를 로드
    global black_background,clear,food,perfect
    black_background = load_image('배경\\black_background.png')
    clear = load_image('배경\\clear.png')
    food = [load_image('배경\\sugar.png'),load_image('배경\\water.png'),
            load_image('배경\\lemon.png')]
    perfect = load_image('배경\\perfect_no.png')



def update(frame_time,events):
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, canvas_size.canvasheight - 1 - event.y




def draw():
    if black_background:
        black_background.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    if clear:
        clear.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if canvas_size.collide_check:
        draw_rectangle(15, 130, 305, 545)
        draw_rectangle(500, 130, 790, 545)
        draw_rectangle(965, 130, 1255, 545)
        draw_rectangle(1145, 585, 1255, 690)
        draw_rectangle(495, 605, 855, 670)




def finish():

    pass



def pause():
    pass
def resume():
    pass
