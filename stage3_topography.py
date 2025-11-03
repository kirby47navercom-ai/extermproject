import background_3stage
from random import randint
import canvas_size
import ramona
import resource
import math





class Stage3_Terrain:
    def __init__(self,i):
        self.terrain_y = [randint(100, 400) for _ in range(5)]
        self.terrain_x = [randint(100, background_3stage.width - 100) for _ in range(5)]
        self.terrain_width = 100
        self.terrain_height = 20
        self.pattern=i
        pass

    def update(self, frame_time):
        pass

    def draw(self):
        for i in range(5):
            resource.terrain3.clip_composite_draw(0, 0, 128, 32, 0, '', self.terrain_x[i]-canvas_size.camera_x, self.terrain_y[i]-canvas_size.camera_y, self.terrain_width, self.terrain_height)
        pass