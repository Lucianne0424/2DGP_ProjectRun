from pico2d import get_events, clear_canvas, update_canvas, load_image, load_font
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, \
    SDL_BUTTON_LEFT

from SourceCode.Etc import game_framework, game_world, game_speed, mouse_event, global_variable
from SourceCode.Etc.global_variable import canvasSIZE, depth
from SourceCode.Mode import play_mode, title_mode
from SourceCode.Object import booster_object, magnet_object, button_object


class UI:
    def __init__(self):
        self.image = load_image('img/UI//score_screen.png')
        self.font = load_font('.//DataFile//KORAIL2007.TTF', 30)
        self.x, self.y = canvasSIZE[0] / 2, canvasSIZE[1] / 2
        self.color = (0, 0, 0)


    def draw(self):
        self.image.draw(self.x, self.y, 800, 600)
        self.font.draw(self.x - 65, self.y + 245, '게임 결과', self.color)
        self.font.draw(self.x - 250, self.y + 100, '점       수 : ' + str(global_variable.score), self.color)
        self.font.draw(self.x - 250, self.y + 20, '획득 코인 : ' + str(global_variable.playerCoin), self.color)

        if global_variable.mission != False:
            self.font.draw(self.x - 250, self.y - 60, '미       션 : ' + str(global_variable.mission_result) + ' / ' + str(global_variable.mission), self.color)

    def update(self):
        pass


def init():
    game_world.add_object(UI(), depth['UI'])
    size_x, size_y = canvasSIZE[0] / 2, canvasSIZE[1] / 2
    game_world.add_object(button_object.ButtonObject(size_x + 150, size_y - 200, 'next', '확 인', 34), depth['Button'])
    game_world.add_object(button_object.ButtonObject(size_x - 150, size_y - 200, 'replay', '다시하기', 58), depth['Button'])


def finish():
    game_world.clear()

    # 초기화
    game_speed.speed = 1.0
    game_speed.pauseTime = False
    booster_object.Booster_state.reset()
    magnet_object.Magnet_state.reset()


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
                    if t.command == 'next':
                        t.sound.play()
                        game_framework.change_mode(title_mode)
                    elif t.command == 'replay':
                        t.sound.play()
                        game_framework.change_mode(play_mode)




def update():
    pass


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause(): pass


def resume(): pass
