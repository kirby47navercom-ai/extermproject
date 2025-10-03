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
        pass
