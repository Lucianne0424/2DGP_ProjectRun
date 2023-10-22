import os

from pico2d import load_image
from sdl2 import SDL_KEYDOWN, SDLK_SPACE

os.chdir("./img")

bottom = 100


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def end_action(e):
    return e[0] == 'END_ACTION'


class Landing:
    @staticmethod
    def entrance(player, event):
        player.action = 6
        player.frame = 0

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 4

        if player.frame == 3:
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 110, player.action * 150, 110, 150, player.x, player.y)


class DoubleJumpFall:
    @staticmethod
    def entrance(player, event):
        player.action = 9
        player.frame = 0

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 4

        player.y = player.startY + player.G_force()
        if player.y <= bottom:
            player.y = bottom
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 86, player.action * 150, 86, 150, player.x, player.y)


class DoubleJumpStart:
    @staticmethod
    def entrance(player, event):
        player.action = 7
        player.frame = 0
        player.count = 0
        player.jumpTime = 0.0
        player.startY = player.y

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        if player.frame < 6:
            player.frame = (player.frame + 1)
        player.y = player.startY + player.G_force()
        player.count += 1

        if player.count == 10:
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 102, player.action * 150, 102, 150, player.x, player.y)


class JumpFall:
    @staticmethod
    def entrance(player, event):
        player.action = 5
        player.frame = 0

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1)
        if player.frame > 5:
            player.frame = 5
        player.y = bottom + player.G_force()
        if player.y <= bottom:
            player.y = bottom
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 109, player.action * 150, 109, 150, player.x, player.y)


class JumpUp:
    @staticmethod
    def entrance(player, event):
        player.action = 4
        player.frame = 0
        player.count = 0

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.count += 1
        player.y = bottom + player.G_force()
        if player.count == 2:
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 80, player.action * 150, 80, 150, player.x, player.y)


class JumpStart:
    @staticmethod
    def entrance(player, event):
        player.action = 3
        player.frame = 0
        player.jumpTime = 0.0

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 4
        player.y = bottom + player.G_force()
        if player.frame == 3:
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 108, player.action * 150, 108, 150, player.x, player.y)


class Run:
    @staticmethod
    def entrance(player, event):
        player.action = 0
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
            Run: {space_down: JumpStart},
            JumpStart: {end_action: JumpUp, space_down: DoubleJumpStart},
            JumpUp: {end_action: JumpFall, space_down: DoubleJumpStart},
            JumpFall: {end_action: Landing, space_down: DoubleJumpStart},
            DoubleJumpStart: {end_action: DoubleJumpFall},
            DoubleJumpFall: {end_action: Landing},
            Landing: {end_action: Run}
        }

    def start(self):
        self.cur_state.entrance(self.player, ('NONE', 0))

    def handle_event(self, event):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(event):
                self.cur_state.exit(self.player, event)
                self.cur_state = next_state
                self.cur_state.entrance(self.player, event)
                return True
        return False

    def update(self):
        self.cur_state.do(self.player)

    def draw(self):
        self.cur_state.draw(self.player)


class Player:
    def __init__(self):
        self.x, self.y = 100, bottom
        self.frame = 0
        self.action = 0
        self.count = 0

        self.Graity = 9.8
        self.jumpPower = 50.0
        self.jumpTime = 0.0

        self.image = load_image('Girl_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()

    def G_force(self):
        h = (self.jumpTime * self.jumpTime * (-self.Graity) / 2) + (self.jumpTime * self.jumpPower)
        self.jumpTime += 1.0
        return h
