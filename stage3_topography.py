from pico2d import *
import background_3stage
from random import randint
import canvas_size
import ramona
import resource
import math


width = 1980


class Stage3_Terrain:
    vine_image = None
    water_image = None
    flame_image = None
    vine_needle_appear_image = None
    vine_needle_disappear_image = None
    water_wave_image = None
    flame_ball_image = None
    def __init__(self,i):
        self.terrain_y = [randint(100, 400) for _ in range(5)]
        self.terrain_x = [randint(100, background_3stage.width - 100) for _ in range(5)]
        self.terrain_width = 960
        self.terrain_height = 128
        self.pattern = 2
        self.old_pattern = i
        self.speed = 15
        if Stage3_Terrain.vine_image == None:
            Stage3_Terrain.vine_image = resource.fox_vine_background_image
            Stage3_Terrain.water_image = resource.fox_water_background_image
            Stage3_Terrain.flame_image = resource.fox_flame_background_image
            Stage3_Terrain.vine_needle_appear_image = resource.fox_vine_needle_appear_image
            Stage3_Terrain.vine_needle_disappear_image = resource.fox_vine_needle_disappear_image
            Stage3_Terrain.water_wave_image = resource.fox_water_wave_image
            Stage3_Terrain.flame_ball_image = resource.fox_flame_ball_image

        self.vine_needle_appear_frame = 0
        self.vine_needle_disappear_frame = 0

        self.water_frame = 0
        self.water_wave_frame = 0



        self.flame_frame=0
        self.flame_ball_frame = 0






    def update(self, frame_time, events=None):
        if self.pattern==2:
            self.water_frame = (self.water_frame + frame_time * self.speed) % 8
        elif self.pattern==3:
            self.flame_frame = (self.flame_frame + frame_time * self.speed) % 5

        self.falldown()

    def falldown(self):
        if ramona.Ramona_POS_Y<self.terrain_height-10:
            print (ramona.Ramona_POS_Y, self.terrain_height)



    def draw(self):
        camerax = canvas_size.shake_x+ canvas_size.camera_x
        cameray= canvas_size.shake_y+ canvas_size.camera_y
        if self.pattern==1:
            Stage3_Terrain.vine_image[0].clip_draw(0, 0, self.terrain_width, self.terrain_height,
                                                width // 2 - camerax,
                                                -10 - cameray,
                                                self.terrain_width*2.5, self.terrain_height*2)

        elif self.pattern==2:
            Stage3_Terrain.water_image[int(self.water_frame)].clip_draw(0, 0, self.terrain_width, self.terrain_height,
                                                width // 2 - camerax,
                                                -10 - cameray,
                                                self.terrain_width*2.5, self.terrain_height*2)
        elif self.pattern==3:
            Stage3_Terrain.flame_image[int(self.flame_frame)].clip_draw(0, 0, self.terrain_width, self.terrain_height,
                                                width // 2 - camerax,
                                                -10 - cameray,
                                                self.terrain_width*2.5, self.terrain_height*2)

        if canvas_size.collide_check:
            draw_rectangle(self.terrain_width-self.terrain_width*2.5/2, -self.terrain_height+10,
                       self.terrain_width+self.terrain_width*2.5/2, self.terrain_height-10)

