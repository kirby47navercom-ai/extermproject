from pico2d import *
import resource


class Ramona:
    def init(self):
        self.x, self.y = 100, 150
        self.frame = 0
        self.dir = 0
        self.hp = 5
        self.state = 'idle'
        self.hittime = 0
        self.animation_speed = 8.0
        self.image = resource.ramona_image
        self.coordinate = resource.ramona_coordinate



    def update(self,frame_time):

        self.handle_event(self,frame_time)
        pass

    def handle_event(self,frame_time):
        global events, state
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT or event.key == ord("a") or event.key == ord("A"):
                    if event.key == SDLK_LSHIFT:
                        state = 'run'
                    else:
                        state = 'walk'
                        self.dir= -1
                        self.walk(self,True,frame_time)
                elif event.key == SDLK_RIGHT or event.key == ord("d") or event.key == ord("D"):
                    if event.key == SDLK_LSHIFT:
                        state = 'run'
                    else:
                        state = 'walk'
                        self.dir = 1
                        self.walk(self, False, frame_time)

                elif event.key == SDLK_SPACE:
                    pass

                elif event.key == SDLK_ESCAPE:
                    quit()
            elif event.type == SDL_KEYUP:
                self.state = 'idle'
            elif self.state == 'idle':
                self.idle(self,frame_time)

        if self.state != state:
            self.frame = 0

    def walk(self,flip,frame_time):
        ramona_walk_speed = 200.0
        self.x+=ramona_walk_speed * frame_time * self.dir
        self.frame = (self.frame + self.animation_speed * frame_time) % 6
        pass

    def idle(self,frame_time):
        self.frame = (self.frame + self.animation_speed * frame_time) % 6
        pass

    def draw(self):

        pass
