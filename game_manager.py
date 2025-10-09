from pico2d import *
import mouse_image
import canvas_size
import stage1_manager

def init():
    global stage1,mouse
    stage1.init()

    mouse = mouse_image.Mouse()

    pass

def update(frame_time):
    global stage1,mouse
    events = get_events()
    stage1.update(frame_time,events)

    mouse.update(frame_time,events)

    if canvas_size.shake_timer > 0:
        canvas_size.update_shake(frame_time)
    pass

def render():
    global stage1,mouse
    clear_canvas()
    stage1.render()
    mouse.draw()
    update_canvas()
    pass