from pico2d import *
import mouse_image
import canvas_size
import stage1_manager
import stage2_manager
import background_1stage

def init():
    global mouse
    #stage1_manager.init()
    stage2_manager.init()

    mouse = mouse_image.Mouse()

    pass

def update(frame_time):
    global mouse
    events = get_events()
    #stage1_manager.update(frame_time,events)
    stage2_manager.update(frame_time,events)

    mouse.update(frame_time,events)

    if canvas_size.shake_timer > 0:
        canvas_size.update_shake(frame_time)
    pass

def draw():
    global mouse
    clear_canvas()
    #ㅁstage1_manager.draw()
    stage2_manager.draw()
    mouse.draw()
    update_canvas()
    pass