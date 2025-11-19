from pico2d import *
import ramona
import background_2stage
import draw_gesture
import ramona_ui
import stage2_monster
import canvas_size
import game_framework
import game_world

ramona_instance = None
monster_instance = None


def init():
    global ramona_instance, monster_instance
    game_world.clear()

    stage_background = background_2stage.Background()
    ramona.GROUND_LEVEL = 70
    ramona.WIDTH_LEVEL = 320

    ramona_instance = ramona.Ramona()
    monster_instance = stage2_monster.Stage2_Monster()

    ramona_ui_instance = ramona_ui.Ramona_UI()
    draw_gest_instance = draw_gesture.GestureRecognizer()

    game_world.add_object(stage_background, 0)
    game_world.add_object(monster_instance, 1)
    game_world.add_object(ramona_instance, 2)
    game_world.add_object(ramona_ui_instance, 3)
    game_world.add_object(draw_gest_instance, 3)

    background_2stage.start = False

    ramona_instance.x = 50
    ramona_instance.y = ramona.GROUND_LEVEL
    ramona.Ramona_POS_X = ramona_instance.x
    ramona.Ramona_POS_Y = ramona_instance.y

    canvas_size.camera_x = 0
    canvas_size.camera_y = 0
    ramona.Ramona_retry = False
    ramona.Ramona_dead = False


def update(frame_time, events):
    if not ramona.Ramona_dead:
        game_world.update(frame_time, events)
    elif ramona.Ramona_retry:
        for event in events:
            if event.type == SDL_KEYDOWN and event.key == SDLK_r:
                ramona.Ramona_dead = False
                ramona.CURRENT_HP = ramona.MAX_HP
                init()
                return
    if ramona.Ramona_dead:
        if ramona_instance:
            ramona_instance.update(frame_time, events)

    if canvas_size.shake_timer > 0:
        canvas_size.update_shake(frame_time)

    canvas_size.camera_x = canvas_size.scroll_x + canvas_size.shake_x
    canvas_size.camera_y = canvas_size.scroll_y + canvas_size.shake_y


def draw():
    game_world.render()


def finish():
    game_world.clear()


def pause(): pass


def resume(): pass