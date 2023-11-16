from pico2d import open_canvas, close_canvas

from SourceCode.Etc import game_framework
from SourceCode.Etc.global_variable import canvasSIZE
from SourceCode.Mode import test_play_mode, title_mode

open_canvas(canvasSIZE[0], canvasSIZE[1])
game_framework.run(title_mode)
close_canvas()
