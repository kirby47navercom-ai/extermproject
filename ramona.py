from pico2d import *
import time
import resource


# 물리
GRAVITY = 2000.0
GROUND_LEVEL = 100
# 속도 (pixel/sec)
WALK_SPEED = 200.0
RUN_SPEED = 350.0
EVADE_SPEED = 500.0
JUMP_POWER = 600.0
# 시간
EVADE_DURATION = 0.3
DOUBLE_TAP_INTERVAL = 0.2
EVADE_COOLDOWN = 1.5

canvaswidth = 1280
canvasheight = 720

A_DOWN, D_DOWN, A_UP, D_UP = range(4)
SHIFT_DOWN, SHIFT_UP, SPACE_DOWN, SPACE_UP = range(4, 8)
A_D_TAP, D_D_TAP = range(8, 10)


key_event_table = {
    (SDL_KEYDOWN, SDLK_a): A_DOWN,
    (SDL_KEYDOWN, SDLK_d): D_DOWN,
    (SDL_KEYUP, SDLK_a): A_UP,
    (SDL_KEYUP, SDLK_d): D_UP,
    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): SHIFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP, # SPACE_UP 추가
}



class IdleState:
    def enter(self, event):
        self.dir = 0
        self.frame = 0

    def exit(self, event):
        pass

    def do(self, frame_time):
        self.y_velocity -= GRAVITY * frame_time
        self.y += self.y_velocity * frame_time
        self.frame = (self.frame + self.animation_speed * frame_time) % 6

    def draw(self):
        self.draw_sprite('idle')

    def handle_event(self, event):
        if event == A_DOWN or event == D_DOWN:
            self.change_state(WalkState, event)
        elif event == SPACE_DOWN:
            self.change_state(JumpState, event)
        elif event == A_D_TAP or event == D_D_TAP:
            self.change_state(EvadeState, event)


class WalkState:
    def enter(self, event):
        if event == A_DOWN:
            self.dir = -1
        elif event == D_DOWN:
            self.dir = 1

    def exit(self, event):
        pass

    def do(self, frame_time):
        self.x += self.dir * WALK_SPEED * frame_time
        self.y_velocity -= GRAVITY * frame_time
        self.y += self.y_velocity * frame_time
        self.frame = (self.frame + self.animation_speed * frame_time) % 6

    def draw(self):
        self.draw_sprite('walk')

    def handle_event(self, event):
        if event == A_UP and self.dir == -1:
            self.change_state(IdleState, event)
        elif event == D_UP and self.dir == 1:
            self.change_state(IdleState, event)
        elif event == SHIFT_DOWN:
            self.change_state(RunState, event)
        elif event == SPACE_DOWN:
            self.change_state(JumpState, event)
        elif event == A_D_TAP or event == D_D_TAP:
            self.change_state(EvadeState, event)


class RunState:
    def enter(self, event):

        pass

    def exit(self, event):
        pass

    def do(self, frame_time):
        self.x += self.dir * RUN_SPEED * frame_time
        self.y_velocity -= GRAVITY * frame_time
        self.y += self.y_velocity * frame_time
        self.frame = (self.frame + self.animation_speed * 1.5 * frame_time) % 6

    def draw(self):
        self.draw_sprite('run')

    def handle_event(self, event):
        if event == A_UP and self.dir == -1:
            self.change_state(IdleState, event)
        elif event == D_UP and self.dir == 1:
            self.change_state(IdleState, event)
        elif event == SHIFT_UP:
            self.change_state(WalkState, event)
        elif event == SPACE_DOWN:
            self.change_state(JumpState, event)


class EvadeState:
    def enter(self, event):
        if event == A_D_TAP:
            self.dir = -1
        elif event == D_D_TAP:
            self.dir = 1
        self.evade_timer = EVADE_DURATION
        self.evade_cooldown_timer = EVADE_COOLDOWN

    def exit(self, event):
        pass

    def do(self, frame_time):
        self.y_velocity -= GRAVITY * frame_time
        self.y += self.y_velocity * frame_time
        self.x += self.dir * EVADE_SPEED * frame_time
        self.evade_timer -= frame_time
        if self.evade_timer <= 0:
            if self.a_pressed or self.d_pressed:
                self.change_state(WalkState, None)
            else:
                self.change_state(IdleState, None)
        self.frame = (self.frame + self.animation_speed * 2.0 * frame_time) % 6

    def draw(self):
        self.draw_sprite('evade')

    def handle_event(self, event):
        pass


class JumpState:
    def enter(self, event):
        if self.jump_count < 2:
            self.y_velocity = JUMP_POWER
            self.jump_count += 1

            if self.jump_count > 1:
                self.frame = 0

    def exit(self, event):
        pass

    def do(self, frame_time):
        if self.a_pressed and not self.d_pressed:
            self.dir = -1
        elif self.d_pressed and not self.a_pressed:
            self.dir = 1

        self.x += self.dir * WALK_SPEED * frame_time


        self.y_velocity -= GRAVITY * frame_time
        self.y += self.y_velocity * frame_time


        if self.jump_count > 1:
            self.frame = (self.frame + self.animation_speed*2.0 * frame_time) % 5

        if self.y <= GROUND_LEVEL:
            self.y = GROUND_LEVEL
            self.y_velocity = 0
            self.jump_count = 0
            if self.a_pressed or self.d_pressed:
                self.change_state(WalkState, None)
            else:
                self.change_state(IdleState, None)

    def draw(self):
        if self.jump_count > 1:
            self.draw_sprite('double_jump')
        else:
            self.draw_sprite('jump', frame_idx=2)

    def handle_event(self, event):
        if event == SPACE_DOWN and self.jump_count < 2:
            self.cur_state.enter(self, event)

        elif event == SPACE_UP:
            if self.y_velocity > 0:
                self.y_velocity *= 0.5



class Ramona:
    def __init__(self):
        self.x, self.y = 100, GROUND_LEVEL
        self.y_velocity = 0
        self.frame = 0.0
        self.dir = 0
        self.flip = False
        self.animation_speed = 8.0
        self.hp = 3
        self.image = resource.ramona_image
        self.coordinate = resource.ramona_coordinate

        self.last_key_time = {'a': 0, 'd': 0}
        self.jump_count = 0
        self.evade_cooldown_timer = 0.0

        # 키 눌림 상태 추적
        self.a_pressed = False
        self.d_pressed = False

        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def change_state(self, new_state, event):
        if self.cur_state != new_state:
            self.cur_state.exit(self, event)
            self.cur_state = new_state
            self.cur_state.enter(self, event)

    def update(self, frame_time):
        self.handle_event(frame_time)
        self.cur_state.do(self, frame_time)


        if self.evade_cooldown_timer > 0:
            self.evade_cooldown_timer -= frame_time


        if self.cur_state in [IdleState, WalkState, RunState]:
            if self.a_pressed == self.d_pressed:
                self.dir = 0
                if self.cur_state in [WalkState, RunState]:
                    self.change_state(IdleState, None)
            elif self.a_pressed:
                self.dir = -1
                if self.cur_state == IdleState:
                    self.change_state(WalkState, None)
            elif self.d_pressed:
                self.dir = 1
                if self.cur_state == IdleState:
                    self.change_state(WalkState, None)


        self.x = clamp(25, self.x, canvaswidth - 25)
        self.y = clamp(GROUND_LEVEL, self.y, 864 - 50)

        if self.dir == -1:
            self.flip = True
        elif self.dir == 1:
            self.flip = False

    def handle_event(self, frame_time):
        events = get_events()
        for event in events:
            if (event.type, event.key) in key_event_table:
                key_event = key_event_table[(event.type, event.key)]


                if key_event == A_DOWN:
                    self.a_pressed = True
                elif key_event == A_UP:
                    self.a_pressed = False
                elif key_event == D_DOWN:
                    self.d_pressed = True
                elif key_event == D_UP:
                    self.d_pressed = False
                elif key_event == SHIFT_DOWN:
                    self.shift_pressed = True
                elif key_event == SHIFT_UP:
                    self.shift_pressed = False


                if key_event == A_DOWN and self.evade_cooldown_timer <= 0:
                    if time.time() - self.last_key_time['a'] < DOUBLE_TAP_INTERVAL:
                        self.cur_state.handle_event(self, A_D_TAP)
                    else:
                        self.cur_state.handle_event(self, A_DOWN)
                    self.last_key_time['a'] = time.time()
                elif key_event == D_DOWN and self.evade_cooldown_timer <= 0:
                    if time.time() - self.last_key_time['d'] < DOUBLE_TAP_INTERVAL:
                        self.cur_state.handle_event(self, D_D_TAP)
                    else:
                        self.cur_state.handle_event(self, D_DOWN)
                    self.last_key_time['d'] = time.time()
                else:
                    self.cur_state.handle_event(self, key_event)

            elif event.key == SDLK_ESCAPE:
                quit()

    def draw_sprite(self, state_name, frame_idx=None):
        if frame_idx is None:
            frame_idx = int(self.frame)

        if state_name not in self.coordinate or frame_idx >= len(self.coordinate[state_name]):
            return

        left, bottom, width, height, jx, jy = self.coordinate[state_name][frame_idx]

        if not self.flip:
            self.image[state_name].clip_draw(left, bottom, width, height, self.x+jx, self.y+jy, width, height)
        else:
            self.image[state_name].clip_composite_draw(left, bottom, width, height, 0, 'h', self.x+jx, self.y+jy, width,
                                                       height)

    def draw(self):
        self.cur_state.draw(self)