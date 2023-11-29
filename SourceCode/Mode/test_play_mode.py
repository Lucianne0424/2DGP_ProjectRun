from pico2d import *

from SourceCode.Character.girl_character import Girl_Character
from SourceCode.Etc import game_framework, game_speed, game_world
from SourceCode.Etc.global_variable import canvasSIZE
from SourceCode.Object import point_object
from SourceCode.Object.hurdle_object import HurdleObject
from SourceCode.Object.tile_object import TileObject
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

    player = Girl_Character()
    game_world.add_object(player, 3)
    collision_pair_setting()

    game_world.add_object(BackGround(0), 0)
    game_world.add_object(BackGround(canvasSIZE[0]), 0)

    # 테스트 타일 출력
    tile_object = [TileObject(0, 0)]
    game_world.add_object(tile_object[0], 1)
    for i in range(1, 100):
        tile_object.append(TileObject(i % 4, tile_object[i-1].w + tile_object[i-1].x))
        game_world.add_object(tile_object[i], 1)
        game_world.add_collision_pair('player:tile_object', None, tile_object[i])

    # 테스트 장애물 출력
    hurdle = HurdleObject('Ghost', 1000, 100)
    game_world.add_object(hurdle, 2)
    game_world.add_collision_pair('player:hurdle_object', None, hurdle)

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
    game_world.clear()
    pass


def pause(): pass


def resume(): pass
