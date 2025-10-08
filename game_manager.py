from pico2d import *
import ramona
import background
import mouse_image
import draw_gesture
import canvas_size
import ramona_ui
import some_function
import stage1_monster

def init():
    global player,stage_background,mouse,draw_gest,ramona_ui,stage1_monster
    stage_background = background.Background('1')
    player = ramona.Ramona()
    ramona_ui = ramona_ui.Ramona_UI()
    draw_gest = draw_gesture.GestureRecognizer()
    stage1_monster = stage1_monster.Stage1_Monster()
    mouse = mouse_image.Mouse()

    pass

def update(frame_time):
    global player, stage_background, mouse, draw_gest,stage1_monster
    events = get_events()
    stage_background.update(frame_time,events)
    player.update(frame_time,events)
    ramona_ui.update(frame_time,events)
    draw_gest.update(frame_time,events)
    stage1_monster.update(frame_time,events)
    mouse.update(frame_time,events)

    if canvas_size.shake_timer > 0:
        canvas_size.update_shake(frame_time)
    pass

def render():
    global player, stage_background, mouse, draw_gest,stage1_monster
    clear_canvas()
    stage_background.draw()
    player.draw()
    ramona_ui.draw()
    draw_gest.draw()
    stage1_monster.draw()
    mouse.draw()
    update_canvas()
    pass