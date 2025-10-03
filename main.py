import pico2d
import game_framework
import game_manager


pico2d.open_canvas(game_framework.screen_width, game_framework.screen_height)
game_framework.ingame(game_manager)
pico2d.close_canvas()

# 2022180021 양현빈