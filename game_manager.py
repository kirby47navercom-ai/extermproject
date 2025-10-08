from pico2d import *
import mouse_image
import canvas_size
import stage1_manager

def init():
    global stage1_manager,mouse
    stage1_manager.init()

    mouse = mouse_image.Mouse()

    pass

def update(frame_time):
    global stage1_manager,mouse
    events = get_events()
    stage1_manager.update(frame_time,events)

    mouse.update(frame_time,events)

    if canvas_size.shake_timer > 0:
        canvas_size.update_shake(frame_time)
    pass

def render():
    global stage1_manager,mouse
    clear_canvas()
    stage1_manager.render()
    mouse.draw()
    update_canvas()
    pass