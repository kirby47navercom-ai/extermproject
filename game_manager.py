from pico2d import *
import ramona

def init():
    global player
    player = ramona.Ramona()
    pass

def update(frame_time):
    global player
    player.update(frame_time)
    pass

def render():
    global player
    clear_canvas()
    player.draw()
    update_canvas()
    pass