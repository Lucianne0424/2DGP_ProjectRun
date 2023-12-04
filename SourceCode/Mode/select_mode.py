from pico2d import get_events, clear_canvas, update_canvas, load_image, load_font
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, \
    SDL_BUTTON_LEFT

from SourceCode.Etc import game_framework, game_world, game_speed, mouse_event, global_variable
from SourceCode.Etc.global_variable import canvasSIZE, depth
from SourceCode.Mode import test_play_mode, editor_mode, title_mode
from SourceCode.Object import booster_object, magnet_object, button_object


class UI:
    def __init__(self, type):


        self.type = type
        if type == 'store':
            self.image = load_image('img/UI//store_window.png')
            self.x, self.y = 1000, 450
            self.w, self.h = 500, 400

        elif type == 'character':
            self.image = load_image('img/UI//character_choice_window.png')
            self.x, self.y = 380, 450
            self.w, self.h = 700, 400


        self.font = load_font('.//DataFile//KORAIL2007.TTF', 30)
        self.color = (0, 0, 0)


    def draw(self):
        self.image.draw(self.x, self.y, self.w, self.h)

    def update(self):
        pass


def init():
    global image
    image = load_image('img/UI//BGI.png')
    game_world.add_object(UI('store'), depth['UI'])
    game_world.add_object(UI('character'), depth['UI'])

    game_world.add_object(button_object.ButtonObject(1150, 170, 'play', '플레이', 45), depth['Button'])
    game_world.add_object(button_object.ButtonObject(1150, 70, 'previous', '이 전', 34), depth['Button'])
    game_world.add_object(button_object.SelectUpButtonObject(170, 320, 'girl_character_choice','Girl'), depth['Button'])
    game_world.add_object(button_object.SelectUpButtonObject(380, 320, 'temp1_character_choice','temp1'), depth['Button'])
    game_world.add_object(button_object.SelectUpButtonObject(590, 320, 'temp2_character_choice','temp2'), depth['Button'])



def finish():
    game_world.clear()


def resetButton(t):
    if global_variable.character_select[t] == 0: return False
    for i in global_variable.character_select:
        if global_variable.character_select[i] == 0: continue
        global_variable.character_select[i] = 1
    return True

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouse_event.MousePos_x, mouse_event.MousePos_y = mouse_event.Mouse_event.return_mouse_pos(event)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                t = mouse_event.Mouse_event.collision_Ui_object()
                if t != False:
                    if t.command == 'previous':
                        t.sound.play()
                        game_framework.change_mode(title_mode)
                    elif t.command == 'play':
                        t.sound.play()
                        game_framework.change_mode(test_play_mode)
                    elif t.command == 'girl_character_choice':
                        t.sound.play()
                        if resetButton('Girl'):
                            global_variable.character_select['Girl'] = 2

                    elif t.command == 'temp1_character_choice':
                        t.sound.play()
                        if resetButton('temp1'):
                            global_variable.character_select['temp1'] = 2

                    elif t.command == 'temp2_character_choice':
                        t.sound.play()
                        if resetButton('temp2'):
                            global_variable.character_select['temp2'] = 2





def update():
    game_world.updata()


def draw():
    clear_canvas()
    image.draw_to_origin(0, 0, canvasSIZE[0], canvasSIZE[1])
    game_world.render()
    update_canvas()


def pause(): pass


def resume(): pass
