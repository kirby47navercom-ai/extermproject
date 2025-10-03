from pico2d import *
import ramona

def init():
    global ramona
    ramona = ramona.Ramona()
    pass

def update(frame_time):
    global ramona
    ramona.update(frame_time)
    pass

def render():
    global ramona
    clear_canvas()
    ramona.draw()
    update_canvas()
    pass