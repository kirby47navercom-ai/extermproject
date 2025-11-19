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
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(stage1_manager)

def draw():
    # 로고 이미지를 그려준다
    image.draw(canvas_size.canvaswidth//2, canvas_size.canvasheight//2)
    pass

def finish():
    global image
    del image
    pass




def pause():
    pass
def resume():
    pass