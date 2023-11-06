from pico2d import *

import game_framework
import game_world
from background import BackGround
from object_information import setting_stage
from player import Player
from point_object import PointObject, add_point_object


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
             player.handle_event(event)

def init():
    global player

    player = Player()
    game_world.add_object(player, 1)

    game_world.add_object(BackGround(0), 0)
    game_world.add_object(BackGround(game_world.canvasSIZE[0]), 0)



def update():
    game_world.updata()
    add_point_object()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()
    pass

def pause(): pass

def resume(): pass