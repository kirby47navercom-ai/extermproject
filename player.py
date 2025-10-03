from pico2d import *



class Player:
    def init(self):
        self.x, self.y = 100, 150
        self.frame = 0
        self.dir = 0
        self.image = load_image('resource/image/player.png')
        self.hp = 5
        self.state = 'idle'
        self.hittime = 0
        self.image_idle = load_image('Ramona\\Ramona_idle.png')
        self.image_walk = load_image('Ramona\\Ramona_walk.png')
        self.image_run = load_image('Ramona\\Ramona_run.png')
        self.image_jump = load_image('Ramona\\Ramona_jump.png')
        self.image_double_jump = load_image('Ramona\\Ramona_double_jump.png')
        self.image_hit = load_image('Ramona\\Ramona_hit.png')
        self.image_evade = load_image('Ramona\\Ramona_evade.png')
        self.image_getup = load_image('Ramona\\Ramona_getup.png')
        self.image_dead = load_image('Ramona\\Ramona_dead.png')
        self.image_revived = load_image('Ramona\\Ramona_revived.png')
        self.image_stageclear = load_image('Ramona\\Ramona_stageclear.png')
        self.image_gameclear = load_image('Ramona\\Ramona_gameclear.png')
        self.image_action1 = load_image('Ramona\\Ramona_action1.png')
        self.image_action2 = load_image('Ramona\\Ramona_action2.png')
        self.image_action3 = load_image('Ramona\\Ramona_action3.png')
        self.image_action4 = load_image('Ramona\\Ramona_action4.png')
        self.image_action5 = load_image('Ramona\\Ramona_action5.png')
        self.image_action6 = load_image('Ramona\\Ramona_action6.png')

    def update(self):

        self.handle_event(self)
        pass

    def handle_event(self):
        global events, state
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT or event.key == ord("a") or event.key == ord("A"):
                    if event.key == SDLK_LSHIFT:
                        state = 'run'
                    else:
                        state = 'walk'
                        self.walk(self,True)
                elif event.key == SDLK_RIGHT or event.key == ord("d") or event.key == ord("D"):
                    if event.key == SDLK_LSHIFT:
                        state = 'run'
                    else:
                        state = 'walk'

                elif event.key == SDLK_SPACE:
                    pass

                elif event.key == SDLK_ESCAPE:
                    quit()
            elif event.type == SDL_KEYUP:
                self.state = 'idle'

        if self.state != state:
            self.frame = 0

    def walk(self,flip):

        pass

    def draw(self):

        pass
