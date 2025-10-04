from pico2d import *
import ramona
import stage1_background

def init():
    global player
    global stage1
    player = ramona.Ramona()
    stage1 = stage1_background.Background('1')

    pass

def update(frame_time):
    global player
    stage1.update()
    player.update(frame_time)
    pass

def render():
    global player
    clear_canvas()
    stage1.draw()
    player.draw()
    update_canvas()
    pass