from pico2d import *
import ramona
import background
import mouse_image

def init():
    global player,stage_background,mouse
    player = ramona.Ramona()
    stage_background = background.Background('1')
    #mouse = mouse_image.Mouse()

    pass

def update(frame_time):
    global player, stage_background
    stage_background.update(frame_time)
    player.update(frame_time)
    #mouse.update(frame_time)
    pass

def render():
    global player, stage_background
    clear_canvas()
    stage_background.draw()
    player.draw()
    #mouse.draw()
    update_canvas()
    pass