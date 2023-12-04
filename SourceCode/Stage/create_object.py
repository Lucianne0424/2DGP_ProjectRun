from SourceCode.Etc import game_speed, game_world, global_variable
from SourceCode.Etc.game_speed import Game_Speed
from SourceCode.Etc.global_variable import canvasSIZE, depth
from SourceCode.Object import booster_object, point_object, coin_object, magnet_object, healing_object, hurdle_object, \
    tile_object

object_information = []  # .pickle에서 불러온 정보를 저장할 리스트
object_len = {'Tile': 0, 'Hurdle': 0, 'Item': 0}  # object_information의 길이

list = ['Tile', 'Hurdle', 'Item'] # 반복문 돌리기 위한 리스트
createLine_x = {'Tile': 0, 'Hurdle': 0, 'Item': 0}  # 읽어들인 데이터 파일과 좌표값을 비교하여 오브젝트 생성
object_load_count = {'Tile': 0, 'Hurdle': 0, 'Item': 0}  # 반복해서 생성하기 위한 변수

item_type_dict = {
    'Point': (point_object.PointObject, 'player:point_object'),
    'Coin': (coin_object.CoinObject, 'player:coin_object'),
    'Booster': (booster_object.BoosterObject, 'player:booster_object'),
    'Magnet': (magnet_object.MagnetObject, 'player:magnet_object'),
    'Healing': (healing_object.HealingObject, 'player:healing_object')
}


def setting_stage():
    global object_information
    global object_len


    object_information = game_world.load_world(".//DataFile//editor_mode_object_data.pickle")
    object_len['Item'] = len(object_information[depth['Item']])
    object_len['Tile'] = len(object_information[depth['Tile']])
    object_len['Hurdle'] = len(object_information[depth['Hurdle']])

    for i in list:
        createLine_x[i] = 0
        object_load_count[i] = 0

    if global_variable.stage != 0:
        global_variable.mission = global_variable.missionList[global_variable.stage - 1][1]
        global_variable.mission_result = 0
    else:
        global_variable.mission = 0


def create_item_object(object, x):
    ob_type, ob_x, ob_y = object.type, object.x, object.y

    create_pos_x = canvasSIZE[0] + 50
    gap = ob_x - x

    object_create = item_type_dict[ob_type][0](create_pos_x + gap, ob_y)
    game_world.add_object(object_create, depth['Item'])
    game_world.add_collision_pair(item_type_dict[ob_type][1], None, object_create)


def create_tile_object(object, x):
    ob_type, ob_x, ob_y = object.index, object.x, object.y

    create_pos_x = canvasSIZE[0] + 50
    gap = ob_x - x

    object_create = tile_object.TileObject(ob_type, create_pos_x + gap, ob_y)
    game_world.add_object(object_create, depth['Tile'])
    game_world.add_collision_pair('player:tile_object', None, object_create)


def create_hurdle_object(object, x):
    ob_type, ob_x, ob_y = object.hurdleName, object.x, object.y

    create_pos_x = canvasSIZE[0] + 50
    gap = ob_x - x

    object_create = hurdle_object.HurdleObject(ob_type, create_pos_x + gap, ob_y)
    game_world.add_object(object_create, depth['Hurdle'])
    game_world.add_collision_pair('player:hurdle_object', None, object_create)


fnc = {'Tile': create_tile_object, 'Hurdle': create_hurdle_object, 'Item': create_item_object}


def object_create():
    global createLine_x
    global object_load_count

    speed = Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
    for i in list:
        createLine_x[i] += speed

        if object_len[i] == 0 or object_load_count[i] == object_len[i]: continue

        object_type = object_information[depth[i]][object_load_count[i]]
        if object_type.x <= createLine_x[i]:
            fnc[i](object_type, createLine_x[i])
            object_load_count[i] += 1
