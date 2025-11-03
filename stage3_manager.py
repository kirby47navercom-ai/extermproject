from pico2d import *
import ramona
import background_3stage
import draw_gesture
import ramona_ui
import canvas_size
import stage3_monster


def init():
    global player,stage_background,draw_gest,ramona_ui_,stage3_monster_
    stage_background = background_3stage.Background()
    player = ramona.Ramona()
    stage3_monster_ = stage3_monster.Stage3_Monster()
    ramona_ui_ = ramona_ui.Ramona_UI()
    draw_gest = draw_gesture.GestureRecognizer()

    ramona.GROUND_LEVEL = 25
    ramona.WIDTH_LEVEL = background_3stage.width - 25

    player.x=canvas_size.canvaswidth//2
    player.y=260

    canvas_size.camera_x=0
    canvas_size.camera_y=0

def update(frame_time,events):
    global player,stage_background,draw_gest,ramona_ui_,stage2_monster_
    if not ramona.Ramona_dead:
        stage_background.update(frame_time,events)
        stage3_monster_ = stage3_monster.Stage3_Monster()
        ramona_ui_.update(frame_time,events)
        draw_gest.update(frame_time,events)
    else:
        for event in events:
            if event.type == SDL_KEYDOWN and event.key == SDLK_r:
                ramona.Ramona_dead = False
                ramona.CURRENT_HP= ramona.MAX_HP
                ramona.Ramona_POS_X = 100
                ramona.Ramona_POS_Y = ramona.GROUND_LEVEL
                init()
    player.update(frame_time,events)

    if canvas_size.shake_timer > 0:
        canvas_size.update_shake(frame_time)

    canvas_size.camera_x = canvas_size.scroll_x + canvas_size.shake_x
    canvas_size.camera_y = canvas_size.scroll_y + canvas_size.shake_y



def draw():
    global player,stage_background,draw_gest,ramona_ui_,stage2_monster_
    stage_background.draw()
    player.draw()
    stage3_monster_ = stage3_monster.Stage3_Monster()
    ramona_ui_.draw()
    draw_gest.draw()
