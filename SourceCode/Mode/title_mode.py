from pico2d import get_events, clear_canvas, update_canvas, load_image
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE, SDLK_e

from SourceCode.Etc import game_framework
from SourceCode.Etc.global_variable import canvasSIZE
from SourceCode.Mode import test_play_mode, editor_mode


def init():
    global image
    image = load_image('img/Title//title.png')


def finish():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(test_play_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_e:
            game_framework.change_mode(editor_mode)


def update():
    pass


def draw():
    clear_canvas()
    image.draw_to_origin(0, 0, canvasSIZE[0], canvasSIZE[1])
    update_canvas()


def pause(): pass


def resume(): pass
