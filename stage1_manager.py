from pico2d import *
import ramona
import background
import draw_gesture
import ramona_ui
import stage1_monster
import canvas_size

def init():
    global player,stage_background,draw_gest,ramona_ui_,stage1_monster_
    stage_background = background.Background('1')
    player = ramona.Ramona()
    ramona_ui_ = ramona_ui.Ramona_UI()
    draw_gest = draw_gesture.GestureRecognizer()
    stage1_monster_ = stage1_monster.Stage1_Monster()

    ramona.GROUND_LEVEL = 100
    ramona.WIDTH_LEVEL = canvas_size.canvaswidth-25

    player.x=canvas_size.canvaswidth//2
    player.y=ramona.GROUND_LEVEL


def update(frame_time,events):
    global player,stage_background,draw_gest,ramona_ui_,stage1_monster_
    if not ramona.Ramona_dead:
        stage_background.update(frame_time,events)
        draw_gest.update(frame_time,events)
        ramona_ui_.update(frame_time,events)
        stage1_monster_.update(frame_time,events)
    else:
        for event in events:
            if event.type == SDL_KEYDOWN and event.key == SDLK_r:
                ramona.Ramona_dead = False
                ramona.CURRENT_HP= ramona.MAX_HP
                ramona.Ramona_POS_X = 100
                ramona.Ramona_POS_Y = ramona.GROUND_LEVEL
                init()
    player.update(frame_time,events)



def render():
    global player,stage_background,draw_gest,ramona_ui_,stage1_monster_
    stage_background.draw()
    player.draw()
    ramona_ui_.draw()
    draw_gest.draw()
    stage1_monster_.draw()
