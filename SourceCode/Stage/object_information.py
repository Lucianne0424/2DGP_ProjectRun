from SourceCode.Etc import game_speed, game_framework, game_world
from SourceCode.Etc.global_variable import stage
from SourceCode.Object import booster_object, point_object, coin_object, magnet_object

stage1_object_pos_y = [
    (4, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
    (1, 1), (1, 1), (1, 1), (1, 2), (1, 3), (2, 4), (1, 3), (1, 2), (1, 1),
    (1, 1), (1, 2), (1, 3), (1, 2), (3, 1), (1, 1), (1, 1), (1, 1), (1, 1),

    (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
    (1, 1), (1, 2), (1, 1), (1, 2), (1, 3), (2, 4), (1, 3), (1, 2), (1, 1),
    (1, 1), (1, 2), (1, 3), (1, 2), (3, 1), (1, 1), (1, 1), (1, 1), (1, 1),

    (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
    (1, 1), (1, 1), (1, 1), (1, 2), (1, 3), (1, 4), (2, 5), (1, 4), (1, 3),
    (1, 2), (1, 1), (1, 1), (1, 1), (1, 2), (2, 3), (1, 2), (1, 1), (1, 1),
    (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
]  # 오브젝트가 생성 할 값들의 정보 ( stage1_object_pos_y[][i] i가 0이면 어떤 오브젝트인지, 1은 오브젝트의 높이를 뜻함. 나중에는 파일 로드로 변경 예정

object_information = []


def setting_stage():
    global object_information, object_information_len

    if stage == 1:
        object_information = stage1_object_pos_y
        object_information_len = len(object_information)


object_gap_count = 0  # 오브젝트 일정 간격마다 출력하기 위한 변수
object_load_count = 0  # 오브젝트의 배치 정보를 저장한 리스트의 인덱스 값


def object_add():  # 일정 간격으로 오브젝트 생성
    if game_speed.speed <= 0.0: return
    global object_gap_count
    global object_load_count
    object_gap_count = (object_gap_count + 1.0 * game_framework.frame_time)
    if object_gap_count >= (0.2 / game_speed.speed / booster_object.Booster_state.return_booster_speed()):  # 1초에 점수 오브젝트 5개 생성
        object_gap_count = 0

        if object_information[object_load_count][0] == 1:
            object_create = point_object.PointObject(50 + object_information[object_load_count][1] * 50)
            game_world.add_object(object_create, 2)
            game_world.add_collision_pair('player:point_object', None, object_create)

        elif object_information[object_load_count][0] == 2:
            object_create = coin_object.CoinObject(50 + object_information[object_load_count][1] * 50)
            game_world.add_object(object_create, 2)
            game_world.add_collision_pair('player:coin_object', None, object_create)

        elif object_information[object_load_count][0] == 3:
            object_create = booster_object.BoosterObject(50 + object_information[object_load_count][1] * 50)
            game_world.add_object(object_create, 2)
            game_world.add_collision_pair('player:booster_object', None, object_create)

        elif object_information[object_load_count][0] == 4:
            object_create = magnet_object.MagnetObject(50 + object_information[object_load_count][1] * 50)
            game_world.add_object(object_create, 2)
            game_world.add_collision_pair('player:magnet_object', None, object_create)

        object_load_count = (object_load_count + 1) % object_information_len