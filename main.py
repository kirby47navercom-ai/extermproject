import pico2d
import game_framework
import game_manager
import resource

pico2d.open_canvas(game_framework.screen_width, game_framework.screen_height)
pico2d.hide_cursor()
resource.load_resources()
game_framework.ingame(game_manager)
pico2d.close_canvas()

# 게임공학과 2022180021 양현빈