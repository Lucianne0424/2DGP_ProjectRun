import os

from pico2d import load_image
from sdl2 import SDL_KEYDOWN, SDLK_SPACE

os.chdir("./img")

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


class Run:
    @staticmethod
    def entrance(player, event):
        player.frame = 0

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 10

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 98, player.action * 150, 98, 150, player.x, player.y)

class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Run
        self.transitions = {
        }

    def start(self):
        self.cur_state.entrance(self.player, ('NONE', 0))

    def handle_event(self, event):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(event):
                self.cur_state.exit(self.player, event)
                self.cur_state = next_state
                self.cur_state.enter(self.player, event)
                return True

    def update(self):
        self.cur_state.do(self.player)

    def draw(self):
        self.cur_state.draw(self.player)


class Player:
    def __init__(self):
        self.x, self.y = 100, 100
        self.frame = 0
        self.action = 0
        self.image = load_image('Girl_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
