from pico2d import *
import ramona
import background

def init():
    global player
    global stage_background
    player = ramona.Ramona()
    stage_background = background.Background('1')

    pass

def update(frame_time):
    global player
    global stage_background
    stage_background.update(frame_time)
    player.update(frame_time)
    pass

def render():
    global player
    global stage_background
    clear_canvas()
    stage_background.draw()
    player.draw()
    update_canvas()
    pass