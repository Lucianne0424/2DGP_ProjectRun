import pickle
import sys

from pico2d import get_events, clear_canvas, update_canvas, load_image
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDLK_a, SDLK_d, \
    SDL_BUTTON_LEFT, SDLK_s, SDLK_l

from SourceCode.Etc import game_framework, game_world
from SourceCode.Etc.global_variable import canvasSIZE
from SourceCode.Mode import title_mode
from SourceCode.Object import tile_object

MousePos_x, MousePos_y = 0, 0
image = None
choiceObject = None
ObjectNum = None

Print_display_x = 0 # 초기 위치에서 얼만큼 움직였는지 ( 나중에 세이브를 위해 필요 )
display_speed = 50 # a, d키를 눌렀을 때, 화면이 움직이는 속도

choiceList = {
    'Tile': tile_object.TileObject
}


def move_display(speed):
    for layer in game_world.objects:
        for o in layer:
            o.x += speed



def init():
    global image
    global choiceObject
    global ObjectNum
    image = load_image('.//img//Tile//stage_1//Stage_1_bottom_tile_' + str(2) + '.png')
    choiceObject = 'Tile'
    ObjectNum = 2



def finish():
    pass


def handle_events():
    global MousePos_x, MousePos_y
    global Print_display_x

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_MOUSEMOTION:
            MousePos_x, MousePos_y = event.x, (canvasSIZE[1] - 1 - event.y)
            MousePos_x = MousePos_x // 10 * 10
            MousePos_y = MousePos_y // 10 * 10

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                c = choiceList['Tile'](ObjectNum, MousePos_x, MousePos_y)
                game_world.add_object(c, 1)
            else:
                for i in game_world.objects[1]:
                    if game_world.mounse_collide(i, MousePos_x, MousePos_y):
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
            print("불러오기 완료")







def update():
    pass


def draw():
    clear_canvas()
    image.draw(MousePos_x, MousePos_y, 100, image.h)
    game_world.render()
    update_canvas()


def pause(): pass


def resume(): pass
