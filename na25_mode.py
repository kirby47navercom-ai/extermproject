from pico2d import *
import canvas_size
import game_framework
import resource
import home_mode


coin = None
coin_font = None

def init():
    # 로고 이미지를 로드
    global coin,coin_font


    coin = load_image('배경\\coin.png')
    coin_font = load_font('Font\\경기천년바탕_Bold.ttf', 80)

def update(frame_time,events):
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, canvas_size.canvasheight - 1 - event.y
            if 495 <= x <= 855 and 585 <= y <= 690:
                game_framework.change_mode(home_mode)



def draw():

    coin.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    coin_font.draw(80, canvas_size.canvasheight-40, 'X '+str(resource.coin), (0, 0, 0))
    if canvas_size.collide_check:
        draw_rectangle(495, 585, 855, 690)




def finish():

    pass



def pause():
    pass
def resume():
    pass
