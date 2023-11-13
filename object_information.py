import booster_object
import game_framework
import game_world

import coin_object
import magnet_object
import point_object
from global_variable import stage, Booster_state

stage1_object_pos_y = [
    (2, 1), (0, 1), (0, 1), (3, 2), (0, 3), (1, 4), (0, 3), (0, 2), (0, 1),
    (0, 1), (0, 2), (0, 3), (0, 2), (0, 1), (1, 1), (0, 1), (1, 1), (0, 1),
]  # 오브젝트가 생성 할 값들의 정보 ( stage1_object_pos_y[][i] i가 0이면 어떤 오브젝트인지, 1은 오브젝트의 높이를 뜻함.

object_information = []


def setting_stage():
    global object_information, object_information_len

    if stage == 1:
        object_information = stage1_object_pos_y
        object_information_len = len(object_information)


object_gap_count = 0  # 오브젝트 일정 간격마다 출력하기 위한 변수
object_load_count = 0  # 오브젝트의 배치 정보를 저장한 리스트의 인덱스 값


def object_add():  # 일정 간격으로 오브젝트 생성
    global object_gap_count
    global object_load_count
    object_gap_count = (object_gap_count + 1.0 * game_framework.frame_time)
    if object_gap_count >= (0.2 / game_world.game_speed / Booster_state.return_booster_speed()):  # 1초에 점수 오브젝트 5개 생성
        object_gap_count = 0

        if object_information[object_load_count][0] == 0:
            object_create = point_object.PointObject(50 + object_information[object_load_count][1] * 50)
            game_world.add_object(object_create, 2)
            game_world.add_collision_pair('player:point_object', None, object_create)

        elif object_information[object_load_count][0] == 1:
            object_create = coin_object.CoinObject(50 + object_information[object_load_count][1] * 50)
            game_world.add_object(object_create, 2)
            game_world.add_collision_pair('player:coin_object', None, object_create)

        elif object_information[object_load_count][0] == 2:
            object_create = booster_object.BoosterObject(50 + object_information[object_load_count][1] * 50)
            game_world.add_object(object_create, 2)
            game_world.add_collision_pair('player:booster_object', None, object_create)

        elif object_information[object_load_count][0] == 3:
            object_create = magnet_object.MagnetObject(50 + object_information[object_load_count][1] * 50)
            game_world.add_object(object_create, 2)
            game_world.add_collision_pair('player:magnet_object', None, object_create)

        object_load_count = (object_load_count + 1) % object_information_len
