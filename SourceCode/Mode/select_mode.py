from pico2d import get_events, clear_canvas, update_canvas, load_image, load_font
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, \
    SDL_BUTTON_LEFT

from SourceCode.Etc import game_framework, game_world, mouse_event, global_variable
from SourceCode.Etc.global_variable import canvasSIZE, depth
from SourceCode.Mode import play_mode, title_mode, help_mode
from SourceCode.Object import button_object, point_object


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


        self.font = load_font('.//DataFile//KORAIL2007.TTF', 20)
        self.color = (0, 0, 0)


    def draw(self):
        self.image.draw(self.x, self.y, self.w, self.h)
        if self.type == 'store':
            self.font.draw(self.x - 155, self.y + 88, '점수 업글', self.color)
            self.font.draw(self.x - 140, self.y + 50, 'Lv : '+ str(point_object.point_object_level), self.color)

            self.font.draw(self.x + 75, self.y + 88, 'Hp 업글', self.color)
            self.font.draw(self.x + 80, self.y + 50, 'Lv : ' + str(global_variable.hpLevel), self.color)

            self.font.draw(self.x - 220, self.y + 220, '코인 : ' + str(global_variable.coin), self.color)

        elif self.type == 'character':
            self.font.draw(self.x - 265, self.y + 88, '기본 캐릭터', self.color)
            self.font.draw(self.x - 20, self.y + 88, '카우', self.color)
            self.font.draw(self.x + 182, self.y + 88, '매지션', self.color)

    def update(self):
        pass


def init():
    global image, hp_image, character_image

    image = load_image('img/UI//BGI.png')
    hp_image = load_image('img/Item//Healing.png')
    character_image = [load_image('img/Character//Girl//STAY.png'), load_image('img/Character//Cow//STAY.png'), load_image('img/Character//Magician//STAY.png')]

    game_world.add_object(UI('store'), depth['UI'])
    game_world.add_object(UI('character'), depth['UI'])

    game_world.add_object(button_object.ButtonObject(1150, 180, 'help', '도움말', 45), depth['Button'])
    game_world.add_object(button_object.ButtonObject(1150, 80, 'previous', '이   전', 45), depth['Button'])

    game_world.add_object(button_object.SelectButtonObject(170, 320, 'girl_character_choice','Girl'), depth['Button'])
    game_world.add_object(button_object.SelectButtonObject(380, 320, 'cow_character_choice','Cow'), depth['Button'])
    game_world.add_object(button_object.SelectButtonObject(590, 320, 'magician_character_choice','Magician'), depth['Button'])
    game_world.add_object(button_object.LevelUpButtonObject(885, 320, 'Point_level','Point_level'), depth['Button'])
    game_world.add_object(button_object.LevelUpButtonObject(1115, 320, 'Hp_level','Hp_level'), depth['Button'])

    game_world.add_object(button_object.ButtonObject(300, 180, 'stage_1', '스테이지 1 플레이', 125, 300), depth['Button'])
    game_world.add_object(button_object.ButtonObject(300, 80, 'stage_2', '스테이지 2 플레이', 125, 300), depth['Button'])
    game_world.add_object(button_object.ButtonObject(700, 180, 'stage_3', '스테이지 3 플레이', 125, 300), depth['Button'])
    game_world.add_object(button_object.ButtonObject(700, 80, 'editor', '에디터 맵 플레이', 115, 300), depth['Button'])


    game_world.add_object(point_object.UIPointObject(885, 430), depth['UI'])



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
                    elif t.command == 'help':
                        t.sound.play()
                        game_framework.push_mode(help_mode)
                    elif t.command == 'stage_1':
                        t.sound.play()
                        global_variable.stage = 1
                        game_framework.change_mode(play_mode)
                    elif t.command == 'stage_2':
                        t.sound.play()
                        global_variable.stage = 2
                        game_framework.change_mode(play_mode)
                    elif t.command == 'stage_3':
                        t.sound.play()
                        global_variable.stage = 3
                        game_framework.change_mode(play_mode)
                    elif t.command == 'editor':
                        t.sound.play()
                        global_variable.stage = 0
                        game_framework.change_mode(play_mode)
                    elif t.command == 'girl_character_choice':
                        t.sound.play()
                        if resetButton('Girl'):
                            global_variable.character_select['Girl'] = 2

                    elif t.command == 'cow_character_choice':
                        t.sound.play()
                        if resetButton('Cow'):
                            global_variable.character_select['Cow'] = 2

                    elif t.command == 'magician_character_choice':
                        t.sound.play()
                        if resetButton('Magician'):
                            global_variable.character_select['Magician'] = 2

                    elif t.command == 'Point_level':
                        temp = 'Point_level'
                        t.sound.play()
                        if global_variable.levelMax[temp] - 1 > point_object.point_object_level:
                            print(global_variable.coin)
                            if global_variable.price[temp][point_object.point_object_level] <= global_variable.coin:
                                global_variable.coin -= global_variable.price[temp][point_object.point_object_level]
                                point_object.point_object_level += 1



                    elif t.command == 'Hp_level':
                        temp = 'Hp_level'
                        t.sound.play()
                        if global_variable.levelMax[temp] - 1 > global_variable.hpLevel:
                            if global_variable.price[temp][global_variable.hpLevel] <= global_variable.coin:
                                global_variable.coin -= global_variable.price[temp][global_variable.hpLevel]
                                global_variable.hpLevel += 1





def update():
    game_world.updata()


def draw():
    clear_canvas()
    image.draw_to_origin(0, 0, canvasSIZE[0], canvasSIZE[1])
    game_world.render()
    hp_image.draw(1115, 430, 80, 80)

    character_image[0].draw(165, 440)
    character_image[1].draw(380, 420)
    character_image[2].draw(590, 420)

    update_canvas()


def pause(): pass


def resume(): pass
