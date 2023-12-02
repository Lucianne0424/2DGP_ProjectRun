from pico2d import get_events, clear_canvas, update_canvas, load_image, load_font
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE, SDLK_e

from SourceCode.Etc import game_framework, game_world, game_speed
from SourceCode.Etc.global_variable import canvasSIZE, depth
from SourceCode.Mode import test_play_mode, editor_mode, title_mode
from SourceCode.Object import booster_object, magnet_object


class UI:
    def __init__(self):
        self.image = load_image('img/UI//score_screen.png')
        UI.font = load_font('.//DataFile//ENCR10B.TTF', 10)


    def draw(self):
        self.image.draw(canvasSIZE[0] / 2, canvasSIZE[1] / 2, 800, 600)

    def update(self):
        pass


def init():
    game_world.add_object(UI(), depth['UI'])


def finish():
    game_world.clear()

    # 초기화
    game_speed.speed = 1.0
    game_speed.pauseTime = False
    booster_object.Booster_state.reset()
    magnet_object.Magnet_state.reset()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(title_mode)


def update():
    pass


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause(): pass


def resume(): pass
