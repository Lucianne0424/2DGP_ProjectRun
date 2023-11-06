from pico2d import open_canvas, close_canvas

import game_framework
import game_world


import test_play_mode as start_mode


open_canvas(game_world.canvasSIZE[0], game_world.canvasSIZE[1])
game_framework.run(start_mode)
close_canvas()
