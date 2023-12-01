import tomllib

from SourceCode.Etc import game_speed, game_world
from SourceCode.Etc.game_speed import Game_Speed
from SourceCode.Etc.global_variable import stage, canvasSIZE, depth
from SourceCode.Object import booster_object, point_object, coin_object, magnet_object, healing_object, hurdle_object, \
    tile_object

item_object_information = [] # toml에서 불러온 정보를 저장할 리스트
item_object_information_len = 0 # object_information의 길이

tile_object_information = []
tile_object_information_len = 0

hurdle_object_information = []
hurdle_object_information_len = 0

createLine_x = [0.0, 0.0, 0.0] # 읽어들인 데이터 파일과 좌표값을 비교하여 오브젝트 생성 ( 각각 아이템, 타일, 장애물 오브젝트 )
object_load_count = [0, 0, 0] # 반복해서 생성하기 위한 변수 ( 각각 아이템, 타일, 장애물 오브젝트 )

item_type_dict = {
    'Point': (point_object.PointObject, 'player:point_object'),
    'Coin': (coin_object.CoinObject, 'player:coin_object'),
    'Booster': (booster_object.BoosterObject, 'player:booster_object'),
    'Magnet': (magnet_object.MagnetObject, 'player:magnet_object'),
    'Healing': (healing_object.HealingObject, 'player:healing_object')
}


def setting_stage():
    global item_object_information, item_object_information_len
    global tile_object_information, tile_object_information_len

    with open('.//DataFile//stage' + str(stage) + '_item_object_data.toml', 'rb') as f:
        item_object_information = tomllib.load(f)['item_objects']
        item_object_information_len = len(item_object_information)

    with open('.//DataFile//stage' + str(stage) + '_object_data.toml', 'rb') as f:
        tile_object_information = tomllib.load(f)['tile_objects']
        tile_object_information_len = len(tile_object_information)


def create_item_object(object_type, x):
    ob_type, ob_x, ob_y = object_type['type'], object_type['x'], object_type['y']

    create_pos_x = canvasSIZE[0] + 50
    gap = ob_x - x

    object_create = item_type_dict[ob_type][0](create_pos_x + gap, ob_y)
    game_world.add_object(object_create, depth['Item'])
    game_world.add_collision_pair(item_type_dict[ob_type][1], None, object_create)


def create_tile_object(object_type, x):
    if object_type['type'] == 'None': return
    ob_type, ob_x, ob_y = object_type['type'], object_type['x'], object_type['y']

    create_pos_x = canvasSIZE[0] + 50
    gap = ob_x - x

    object_create = tile_object.TileObject(ob_type, create_pos_x + gap, ob_y)
    game_world.add_object(object_create, depth['Tile'])
    game_world.add_collision_pair('player:tile_object', None, object_create)



def object_create():
    global createLine_x
    global object_load_count

    speed = Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
    for i in range(3):
        createLine_x[i] += speed

    object_type = item_object_information[object_load_count[0]]
    if object_type['x'] <= createLine_x[0]:
        create_item_object(object_type, createLine_x[0])
        object_load_count[0] = (object_load_count[0] + 1) % item_object_information_len
        if object_load_count[0] == 0: createLine_x[0] = 0.0

    object_type = tile_object_information[object_load_count[1]]
    if object_type['x'] <= createLine_x[1]:
        create_tile_object(object_type, createLine_x[1])
        object_load_count[1] = (object_load_count[1] + 1) % tile_object_information_len