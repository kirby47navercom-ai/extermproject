from pico2d import *
import mouse_image
import canvas_size
import stage1_manager
import stage2_manager
import stage3_manager
import background_1stage

def init():
    #stage1_manager.init()
    #stage2_manager.init()
    stage3_manager.init()


    pass

def update(frame_time,events):
    #stage1_manager.update(frame_time,events)
    #stage2_manager.update(frame_time,events)
    stage3_manager.update(frame_time,events)

    pass

def draw():
    #stage1_manager.draw()
    #stage2_manager.draw()
    stage3_manager.draw()
    pass