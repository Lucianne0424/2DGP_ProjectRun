from pico2d import get_events, clear_canvas, update_canvas, load_image
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDLK_a, SDLK_d, \
    SDL_BUTTON_LEFT

from SourceCode.Etc import game_framework, game_world
from SourceCode.Etc.global_variable import canvasSIZE
from SourceCode.Mode import title_mode
from SourceCode.Object import tile_object

MousePos_x, MousePos_y = 0, 0
image = None
choiceObject = None
ObjectNum = None
Print_display_x = 0
diplay_speed = 50

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
    image = load_image('.//img//Tile//stage_1//Stage_1_top_tile_' + str(0) + '.png')
    choiceObject = 'Tile'
    ObjectNum = 4



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
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                x = (MousePos_x // 100 * 100)
                y = (MousePos_y // 100 * 100)
                c = choiceList['Tile'](ObjectNum, x, y)
                game_world.add_object(c, 1)
            else:
                for i in game_world.objects[1]:
                    if game_world.mounse_collide(i, MousePos_x, MousePos_y):
                        game_world.remove_object(i)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            Print_display_x -= diplay_speed
            move_display(diplay_speed)

            print(Print_display_x)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            Print_display_x += diplay_speed
            move_display(-diplay_speed)

            print(Print_display_x)






def update():
    pass


def draw():
    clear_canvas()
    image.draw(MousePos_x, MousePos_y, 100, image.h)
    game_world.render()
    update_canvas()


def pause(): pass


def resume(): pass
