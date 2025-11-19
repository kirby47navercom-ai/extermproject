from pico2d import *
import canvas_size
import game_framework
import stage1_manager

image = None

def init():
    # 로고 이미지를 로드
    global image, logo_start_time

    image = load_image('배경//main.png')
    pass

def update(frame_time,events):
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, get_canvas_height() - 1 - event.y
            if 250 <= x <= 600 and 140 <= y <= 235:
                canvas_size.collide_check = True
            elif 250 <= x <= 600 and 260 <= y <= 355:
                game_framework.change_mode(stage1_manager)

def draw():
    # 로고 이미지를 그려준다
    image.draw(canvas_size.canvaswidth//2, canvas_size.canvasheight//2)
    if canvas_size.collide_check:
        i = 120
        j=100
        draw_rectangle(250, 140+i, 600, 235+i)#시작
        draw_rectangle(250,140,600,235)#환경
        draw_rectangle(250+j, 140, 600+j, 235)  # 환경

    pass

def finish():
    global image
    del image
    pass




def pause():
    pass
def resume():
    pass