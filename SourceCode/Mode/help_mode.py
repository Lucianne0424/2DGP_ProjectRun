from pico2d import get_events, clear_canvas, update_canvas, load_image
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, \
    SDL_BUTTON_LEFT

from SourceCode.Etc import game_framework, mouse_event, game_world
from SourceCode.Etc.global_variable import canvasSIZE, depth
from SourceCode.Mode import editor_mode, select_mode
from SourceCode.Object.button_object import ButtonObject


def init():
    global image, BGI, hp_image, character_image
    global size_x, size_y
    image = load_image('img/Ui//select_mode_help.png')
    size_x = (canvasSIZE[0] / 2)
    size_y = (canvasSIZE[1] / 2)

    BGI = load_image('img/UI//BGI.png')
    hp_image = load_image('img/Item//Healing.png')
    character_image = [load_image('img/Character//Girl//STAY.png'), load_image('img/Character//Cow//STAY.png'),
                       load_image('img/Character//Magician//STAY.png')]


def finish():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()


def update():
    pass


def draw():
    clear_canvas()
    BGI.draw_to_origin(0, 0, canvasSIZE[0], canvasSIZE[1])
    game_world.render()

    hp_image.draw(1115, 430, 80, 80)
    character_image[0].draw(165, 440)
    character_image[1].draw(380, 420)
    character_image[2].draw(590, 420)

    image.draw(size_x, size_y, 800, 600)
    update_canvas()


def pause(): pass


def resume(): pass
