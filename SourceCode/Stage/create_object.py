import tomllib

from SourceCode.Etc import game_speed, game_world
from SourceCode.Etc.game_speed import Game_Speed
from SourceCode.Etc.global_variable import stage, canvasSIZE
from SourceCode.Object import booster_object, point_object, coin_object, magnet_object, healing_object


object_information = [] # toml에서 불러온 정보를 저장할 리스트
object_information_len = 0 # object_information의 길이
createLine_x = 0.0 # 읽어들인 데이터 파일과 좌표값을 비교하여 오브젝트 생성
object_load_count = 0 # 반복해서 생성하기 위한 변수

item_type_dict = {
    'Point': (point_object.PointObject, 'player:point_object'),
    'Coin': (coin_object.CoinObject, 'player:coin_object'),
    'Booster': (booster_object.BoosterObject, 'player:booster_object'),
    'Magnet': (magnet_object.MagnetObject, 'player:magnet_object'),
    'Healing': (healing_object.HealingObject, 'player:healing_object')
}

def setting_stage():
    global object_information, object_information_len
    with open('.//DataFile//stage' + str(stage) + '_object_data.toml', 'rb') as f:
        object_information = tomllib.load(f)['objects']
        object_information_len = len(object_information)

def create_item_object(object_type, x):
    ob_type, ob_x, ob_y = object_type['type'], object_type['x'], object_type['y']

    create_pos_x = canvasSIZE[0] + 50
    gap = ob_x - x

    object_create = item_type_dict[ob_type][0](create_pos_x + gap, ob_y)
    game_world.add_object(object_create, 4)
    game_world.add_collision_pair(item_type_dict[ob_type][1], None, object_create)



def object_create():
    global createLine_x
    global object_load_count

    createLine_x += Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)

    object_type = object_information[object_load_count]
    print(object_type['x'], createLine_x)
    if object_type['x'] <= createLine_x:
        create_item_object(object_type, createLine_x)
        object_load_count = (object_load_count + 1) % object_information_len
        if object_load_count == 0: createLine_x = 0.0

