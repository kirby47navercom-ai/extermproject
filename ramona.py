from pico2d import *
import resource


class Ramona:
    def __init__(self):
        self.x, self.y = 100, 150
        self.frame = 0
        self.dir = 0
        self.hp = 5
        self.state = 'idle'
        self.flip = False
        self.hittime = 0
        self.animation_speed = 8.0
        self.image = resource.ramona_image
        self.coordinate = resource.ramona_coordinate



    def update(self,frame_time):

        self.handle_event(frame_time)
        self.move_update(frame_time)
        pass

    def handle_event(self,frame_time):
        state = self.state
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == ord("a") or event.key == ord("A"):
                    self.flip = True
                    if event.key == SDLK_LSHIFT:
                        state = 'run'
                    else:
                        state = 'walk'
                        self.dir= -1
                elif event.key == ord("d") or event.key == ord("D"):
                    self.flip = False
                    if event.key == SDLK_LSHIFT:
                        state = 'run'
                    else:
                        state = 'walk'
                        self.dir = 1

                elif event.key == SDLK_SPACE:
                    pass

                elif event.key == SDLK_ESCAPE:
                    quit()
            else: state='idle'

            if self.state != state:
                self.frame = 0

            self.state = state

    def move_update(self,frame_time):
        if self.state == 'idle':
            self.idle(frame_time)
        elif self.state == 'walk':
            self.walk(frame_time)
        pass

    def walk(self,frame_time):
        ramona_walk_speed = 200.0
        self.x+=ramona_walk_speed * frame_time * self.dir
        self.frame = (self.frame + self.animation_speed * frame_time) % 6
        pass

    def idle(self,frame_time):
        self.frame = (self.frame + self.animation_speed * frame_time) % 6
        pass

    def draw(self):
        frame_idx = int(self.frame)
        left, bottom, width, height, jx, jy = self.coordinate[self.state][frame_idx]
        if not self.flip:
            self.image[self.state].clip_composite_draw(left, bottom, width, height, 0, '', self.x, self.y, width * 2, height * 2)
        else:
            self.image[self.state].clip_composite_draw(left, bottom, width, height, 0, 'h', self.x, self.y, width * 2, height * 2)
        pass
