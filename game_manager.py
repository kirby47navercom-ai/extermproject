from pico2d import *
import ramona
import background
import mouse_image
import gesture_background
import draw_gesture

def init():
    global player,stage_background,mouse,gesture_bg,draw_gest
    stage_background = background.Background('1')
    gesture_bg = gesture_background.GestureBackground()
    player = ramona.Ramona()
    draw_gest = draw_gesture.GestureRecognizer()
    mouse = mouse_image.Mouse()

    pass

def update(frame_time):
    global player,stage_background,mouse,gesture_bg
    events = get_events()
    stage_background.update(frame_time)
    gesture_bg.update(frame_time,events)
    player.update(frame_time,events)
    draw_gest.update(frame_time,events)
    mouse.update(frame_time,events)
    pass

def render():
    global player,stage_background,mouse,gesture_bg
    clear_canvas()
    stage_background.draw()
    gesture_bg.draw()
    player.draw()
    draw_gest.draw()
    mouse.draw()
    update_canvas()
    pass