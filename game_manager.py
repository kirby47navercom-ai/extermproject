from pico2d import *
import ramona
import background
import mouse_image
import draw_gesture
import some_function

def init():
    global player,stage_background,mouse,draw_gest
    stage_background = background.Background('1')
    player = ramona.Ramona()
    draw_gest = draw_gesture.GestureRecognizer()
    mouse = mouse_image.Mouse()

    pass

def update(frame_time):
    global player, stage_background, mouse, draw_gest
    events = get_events()
    stage_background.update(frame_time)
    player.update(frame_time,events)
    draw_gest.update(frame_time,events)
    mouse.update(frame_time,events)
    pass

def render():
    global player, stage_background, mouse, draw_gest
    clear_canvas()
    stage_background.draw()
    player.draw()
    draw_gest.draw()
    mouse.draw()
    update_canvas()
    pass