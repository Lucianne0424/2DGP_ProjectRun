from pico2d import *

from SourceCode.Character.magician_character import Magician_Character
from SourceCode.Etc import game_framework, game_speed, game_world, global_variable
from SourceCode.Etc.global_variable import canvasSIZE, depth
from SourceCode.Object import point_object
from SourceCode.Stage.background import BackGround
from SourceCode.Stage.create_object import setting_stage, object_create


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


def collision_pair_setting():
    global player
    game_world.add_collision_pair('player:point_object', player, None)
    game_world.add_collision_pair('player:coin_object', player, None)
    game_world.add_collision_pair('player:booster_object', player, None)
    game_world.add_collision_pair('player:magnet_object', player, None)
    game_world.add_collision_pair('player:tile_object', player, None)
    game_world.add_collision_pair('player:hurdle_object', player, None)
    game_world.add_collision_pair('player:healing_object', player, None)

def init():
    global player

    player = Magician_Character()
    game_world.add_object(player, depth['Player'])
    collision_pair_setting()

    game_world.add_object(BackGround(0), depth['BackGround'])
    game_world.add_object(BackGround(canvasSIZE[0]), depth['BackGround'])

    global_variable.score = 0
    setting_stage()


def update():
    if game_speed.Game_Speed.pauseGame() == False: return
    game_world.updata()
    object_create()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    pass


def pause(): pass


def resume(): pass
