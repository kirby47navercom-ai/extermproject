from pico2d import *
import canvas_size
import game_framework
import resource


ending_image = []
current_image=0


def init():
    # 로고 이미지를 로드
    global ending_image

    if ending_image == None:
        ending_image = resource.end_image




def update(frame_time, events):
    global current_image

    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, canvas_size.canvasheight - 1 - event.y
            if current_image < 6:
                current_image += 1
            else:
                game_framework.pop_mode()




def draw():
    global ending_image,current_image
    if ending_image and current_image<7:
        ending_image[current_image].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)



def finish():
    pass


def pause():
    pass


def resume():
    pass
