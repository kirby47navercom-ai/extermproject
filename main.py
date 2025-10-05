import pico2d
import game_framework
import game_manager
import resource
from canvas_size import *

pico2d.open_canvas(canvaswidth, canvasheight)
pico2d.hide_cursor()
resource.load_resources()
game_framework.ingame(game_manager)
pico2d.close_canvas()

#2022180021 양현빈