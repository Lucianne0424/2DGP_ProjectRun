from pico2d import get_events, clear_canvas, update_canvas, load_image
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDLK_a, SDLK_d, \
    SDL_BUTTON_LEFT, SDLK_s, SDLK_l, SDLK_LEFT, SDLK_RIGHT, SDLK_UP, SDLK_DOWN

from SourceCode.Etc import game_framework, game_world, mouse_event
from SourceCode.Etc.global_variable import canvasSIZE, depth
from SourceCode.Mode import title_mode
from SourceCode.Object import tile_object, hurdle_object, point_object, coin_object, booster_object, magnet_object, \
    healing_object, gate_object

MousePos_x, MousePos_y = 0, 0  # 마우스 위치
Print_display_x = -canvasSIZE[0] - 200  # 초기 위치에서 얼만큼 움직였는지 ( 나중에 세이브를 위해 필요 )
display_speed = 50  # a, d키를 눌렀을 때, 화면이 움직이는 속도

image = None  # 마우스 이미지

object_type = 0  # 오브젝트 타입
object_num = 0  # 타일이나 허들의 종류

hurdleType = ['Ghost', 'hurdle_high', 'hurdle_low']
hurdleType_and_tile_len = [8, len(hurdleType)]

object_type_list = [
    tile_object.TileObject,
    hurdle_object.HurdleObject,
    point_object.PointObject,
    coin_object.CoinObject,
    booster_object.BoosterObject,
    magnet_object.MagnetObject,
    healing_object.HealingObject,
    gate_object.GateObject
]
object_type_len = len(object_type_list)
tile_size = [100, 40]


def clamp(min, num, max):
    return min <= num and num <= max


class mouse_img_load:
    @staticmethod
    def tile_load(num):
        global image
        if clamp(0, num, 3):
            image = load_image('.//img//Tile//stage_1//Stage_1_bottom_tile_' + str(num) + '.png')

        elif clamp(4, num, 7):
            image = load_image('.//img//Tile//stage_1//Stage_1_top_tile_' + str(num % 4) + '.png')

    @staticmethod
    def hurdle_load(num):
        global image
        image = load_image('.//img//Hurdle//stage_1//' + hurdleType[num] + '//' + hurdleType[num] + '_0' + '.png')

    @staticmethod
    def point_load():
        global image
        image = load_image('.//img//Point//point_item_candy1.png')

    @staticmethod
    def coin_load():
        global image
        image = load_image('.//img//Coin//Coin.png')

    @staticmethod
    def booster_load():
        global image
        image = load_image('.//img//item//Booster.png')

    @staticmethod
    def magnet_load():
        global image
        image = load_image('.//img//item//magnet.png')

    @staticmethod
    def healing_load():
        global image
        image = load_image('.//img//item//Healing.png')

    @staticmethod
    def gate_object():
        global image
        image = load_image('.//img//Gate//gate.png')

    @staticmethod
    def object_type(type, num):
        match (type):
            case 0:
                mouse_img_load.tile_load(num)
            case 1:
                mouse_img_load.hurdle_load(num)
            case 2:
                mouse_img_load.point_load()
            case 3:
                mouse_img_load.coin_load()
            case 4:
                mouse_img_load.booster_load()
            case 5:
                mouse_img_load.magnet_load()
            case 6:
                mouse_img_load.healing_load()
            case 7:
                mouse_img_load.gate_object()


def create_object(type, num, x, y):
    match (type):
        case 0:
            t = object_type_list[type](num, x, y)
            game_world.add_object(t, depth['Tile'])
        case 1:
            t = object_type_list[type](hurdleType[num], x, y)
            game_world.add_object(t, depth['Hurdle'])
        case 2 | 3 | 4 | 5 | 6:
            t = object_type_list[type](x, y)
            game_world.add_object(t, depth['Item'])
        case 7:
            t = object_type_list[type](x, y)
            game_world.add_object(t, depth['Gate'])


def move_display(speed):
    for layer in game_world.objects:
        for o in layer:
            o.x += speed


def init():
    global object_type, object_num
    global MousePos_x, MousePos_y

    mouse_img_load.object_type(object_type, object_num)

    i = 0
    while i < canvasSIZE[0]:
        create_object(0, 2, i,0)
        i += 100


def finish():
    game_world.clear()


def handle_events():
    global MousePos_x, MousePos_y
    global Print_display_x
    global object_type, object_num

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)

        elif event.type == SDL_MOUSEMOTION:
            MousePos_x, MousePos_y = mouse_event.Mouse_event.return_mouse_pos(event)

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                create_object(object_type, object_num, MousePos_x, MousePos_y)

            else:
                for t in game_world.objects:
                    for i in t:
                        if mouse_event.Mouse_event.mounse_collide(i, MousePos_x, MousePos_y):
                            game_world.remove_object(i)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            Print_display_x -= display_speed
            move_display(display_speed)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            Print_display_x += display_speed
            move_display(-display_speed)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            print("저장 중 입니다.")
            move_display(Print_display_x)
            game_world.save_world(".//DataFile//editor_mode_object_data.pickle")
            move_display(-Print_display_x)
            print("저장 완료")

        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            print("불러오기 중 입니다.")
            game_world.objects = game_world.load_world(".//DataFile//editor_mode_object_data.pickle")
            move_display(-Print_display_x)
            print("불러오기 완료")


        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            if object_type == 0 or object_type == 1:
                object_num = (object_num - 1) % hurdleType_and_tile_len[object_type]
                mouse_img_load.object_type(object_type, object_num)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            if object_type == 0 or object_type == 1:
                object_num = (object_num + 1) % hurdleType_and_tile_len[object_type]
                mouse_img_load.object_type(object_type, object_num)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            object_type = (object_type + 1) % object_type_len
            object_num = 0
            mouse_img_load.object_type(object_type, object_num)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            object_type = (object_type - 1) % object_type_len
            object_num = 0
            mouse_img_load.object_type(object_type, object_num)


def update():
    pass


def draw():
    clear_canvas()
    match (object_type):
        case 0:
            image.draw(MousePos_x, MousePos_y, tile_size[object_num % 2], image.h)
        case 1 | 7:
            image.draw(MousePos_x, MousePos_y)
        case 2 | 3:
            image.draw(MousePos_x, MousePos_y, 30, 30)
        case _:
            image.draw(MousePos_x, MousePos_y, 40, 40)

    game_world.render()
    game_world.render_hit_box()
    update_canvas()


def pause(): pass


def resume(): pass
