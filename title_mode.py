from pico2d import load_image, get_events, clear_canvas, update_canvas, get_time
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import test_play_mode
from game_world import canvasSIZE
from image_load import image_load


def init():
    global image
    image = image_load('img/Title','title.png')

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


def update():
    pass
def draw():
    clear_canvas()
    image.draw_to_origin(0, 0, canvasSIZE[0],canvasSIZE[1])
    update_canvas()

def pause(): pass
def resume(): pass