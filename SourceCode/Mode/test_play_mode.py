from pico2d import *

from SourceCode.Character.player import Player
from SourceCode.Etc import game_framework, game_speed, game_world
from SourceCode.Etc.global_variable import canvasSIZE
from SourceCode.Object import point_object
from SourceCode.Stage.background import BackGround
from SourceCode.Stage.object_information import setting_stage, object_add


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F1:
            game_speed.speed = min(10.0, game_speed.speed + 0.5)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F2:
            game_speed.speed = max(1.0, game_speed.speed - 0.5)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F5:
            point_object.point_object_level = (point_object.point_object_level) % 17 + 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F4:
            if game_speed.speed <= 0.0:
                game_speed.speed = 1.0
            else:
                game_speed.speed = 0.0

        else:
            player.handle_event(event)


def init():
    global player

    player = Player()
    game_world.add_object(player, 1)

    game_world.add_collision_pair('player:point_object', player, None)
    game_world.add_collision_pair('player:coin_object', player, None)
    game_world.add_collision_pair('player:booster_object', player, None)
    game_world.add_collision_pair('player:magnet_object', player, None)

    game_world.add_object(BackGround(0), 0)
    game_world.add_object(BackGround(canvasSIZE[0]), 0)

    setting_stage()


def update():
    if game_speed.Game_Speed.pauseGame() == False: return
    game_world.updata()
    object_add()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()
    pass


def pause(): pass


def resume(): pass
