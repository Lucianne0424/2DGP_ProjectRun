from pico2d import open_canvas, close_canvas

import game_framework

# import test_play_mode as start_mode
import title_mode as start_mode
from global_variable import canvasSIZE

open_canvas(canvasSIZE[0], canvasSIZE[1])
game_framework.run(start_mode)
close_canvas()
