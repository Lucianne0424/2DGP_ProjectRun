from pico2d import get_events, clear_canvas, update_canvas, load_image
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE, SDLK_e, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, \
    SDL_BUTTON_LEFT

from SourceCode.Etc import game_framework, mouse_event, game_world
from SourceCode.Etc.global_variable import canvasSIZE, depth
from SourceCode.Mode import test_play_mode, editor_mode
from SourceCode.Object.button_object import ButtonObject


def init():
    global image
    image = load_image('img/Title//title.png')
    size_x = (canvasSIZE[0] / 2) + 500
    size_y = (canvasSIZE[1] / 2) - 100

    game_world.add_object(ButtonObject(size_x, size_y, 'play', '플레이', 45), depth['Button'])
    game_world.add_object(ButtonObject(size_x, size_y - 100, 'editor', '에디터', 45), depth['Button'])
    game_world.add_object(ButtonObject(size_x, size_y - 200, 'quit', '종   료', 45), depth['Button'])


def finish():
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouse_event.MousePos_x, mouse_event.MousePos_y = mouse_event.Mouse_event.return_mouse_pos(event)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                t = mouse_event.Mouse_event.collision_Ui_object()
                if t != False:
                    if t.command == 'play':
                        t.sound.play()
                        game_framework.change_mode(test_play_mode)
                    elif t.command == 'editor':
                        t.sound.play()
                        game_framework.change_mode(editor_mode)
                    elif t.command == 'quit':
                        t.sound.play()
                        game_framework.quit()


def update():
    pass


def draw():
    clear_canvas()
    image.draw_to_origin(0, 0, canvasSIZE[0], canvasSIZE[1])
    game_world.render()
    update_canvas()


def pause(): pass


def resume(): pass
