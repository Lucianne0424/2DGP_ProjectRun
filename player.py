from pico2d import draw_rectangle, get_time
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_1, SDLK_s

import game_framework
import game_world
from booster_object import Booster_state

from image_load import image_load
from magnet_object import Magnet_state
from point_object import point_object_level

bottom = 100


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def Key_down_1(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_1


def end_action(e):
    return e[0] == 'END_ACTION'


def game_over(e):
    return e[0] == 'GameOver' and e[1] <= 0.0


PIXEL_PER_METER = (10.0 / 0.3)
PLAYER_SPEED_KMPH = 1.5
PLAYER_SPEED_MPM = (PLAYER_SPEED_KMPH * 1000.0 / 60.0)
PLAYER_SPEED_MPS = (PLAYER_SPEED_MPM / 60.0)
PLAYER_SPEED_PPS = (PLAYER_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION


class Damage:
    @staticmethod
    def entrance(player, event):
        player.action = 1
        player.frame = 0
        player.Hp -= 10

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 7 * ACTION_PER_TIME * game_framework.frame_time) % 7
        if player.frame >= 6:
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(int(player.frame) * 120 - 40, player.action * 150, 120, 150, player.x, player.y)


class GameOver:
    @staticmethod
    def entrance(player, event):
        player.action = 2
        player.frame = 0

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 11 * ACTION_PER_TIME * game_framework.frame_time) % 11

    @staticmethod
    def draw(player):
        player.image.clip_draw((int(player.frame) * 175) + int(player.frame) * 5, player.action * 150, 175, 150,player.x, player.y)


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
        player.frame = (player.frame + 4 * ACTION_PER_TIME * game_framework.frame_time * Booster_state.return_booster_speed()) % 4

        if player.frame >= 3:
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(int(player.frame) * 110, player.action * 150, 110, 150, player.x, player.y)


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
        player.frame = (player.frame + 4 * ACTION_PER_TIME * game_framework.frame_time * Booster_state.return_booster_speed()) % 4

        player.y = player.startY + player.G_force()
        if player.y <= bottom:
            player.y = bottom
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(int(player.frame) * 86, player.action * 150, 86, 150, player.x, player.y)


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
        player.frame = (player.frame + 8 * ACTION_PER_TIME * game_framework.frame_time * Booster_state.return_booster_speed()) % 8
        player.y = player.startY + player.G_force()

        if player.frame >= 7:
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(int(player.frame) * 102, player.action * 150, 102, 150, player.x, player.y)


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
        player.frame = min((player.frame + 5 * ACTION_PER_TIME * game_framework.frame_time * Booster_state.return_booster_speed()), 5)
        player.y = bottom + player.G_force()
        if player.y <= bottom:
            player.y = bottom
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(int(player.frame) * 108, player.action * 150, 108, 150, player.x, player.y)


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
        player.frame = (player.frame + 2 * ACTION_PER_TIME * game_framework.frame_time * Booster_state.return_booster_speed()) % 2
        player.y = bottom + player.G_force()
        if player.frame >= 1:
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(int(player.frame) * 87, player.action * 150, 87, 150, player.x, player.y)


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
        player.frame = (player.frame + 4 * ACTION_PER_TIME * game_framework.frame_time * Booster_state.return_booster_speed()) % 4
        player.y = bottom + player.G_force()
        if player.frame >= 3:
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.image.clip_draw(int(player.frame) * 108, player.action * 150, 108, 150, player.x, player.y)


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
        player.frame = (player.frame + 10 * ACTION_PER_TIME * game_framework.frame_time * Booster_state.return_booster_speed()) % 10
        player.state_machine.handle_event(('GameOver', player.Hp))

    @staticmethod
    def draw(player):
        player.image.clip_draw(int(player.frame) * 98, player.action * 150, 98, 150, player.x, player.y)


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Run
        self.transitions = {
            Run: {space_down: JumpStart, game_over: GameOver, Key_down_1: Damage},
            JumpStart: {end_action: JumpUp, space_down: DoubleJumpStart},
            JumpUp: {end_action: JumpFall, space_down: DoubleJumpStart},
            JumpFall: {end_action: Landing, space_down: DoubleJumpStart},
            DoubleJumpStart: {end_action: DoubleJumpFall},
            DoubleJumpFall: {end_action: Landing},
            Landing: {end_action: Run, space_down: JumpStart},
            GameOver: {game_over: GameOver},
            Damage: {end_action: Run}
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
        self.x, self.y = 300, bottom
        self.Hp = 100.0
        self.frame = 0
        self.action = 0
        self.count = 0

        self.Graity = 9.8
        self.jumpPower = 50.0
        self.jumpTime = 0.0

        self.score = 0
        self.coin = 0

        self.image = image_load('.//img//Character', 'Girl_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

        self.skill_time = False

    def update(self):
        if game_world.game_speed <= 0.0: return
        self.Hp = self.Hp - 1.0 * game_framework.frame_time
        self.state_machine.update()
        if get_time() - Booster_state.return_booster_time() >= 5 and Booster_state.return_booster_time() != False:
            Booster_state.booster_change(False, 1.0)

        if Magnet_state.return_magnet_time() != False:
            Magnet_state.update_magnet_pos(self.x, self.y)
            if get_time() - Magnet_state.return_magnet_time() >= 5:
                Magnet_state.magnet_change(False)
        if self.skill_time != False and get_time() - self.skill_time >= 10:
            self.skill_time = False

    def handle_event(self, event):
        if game_world.game_speed <= 0.0: return
        if self.skill_time == False and event.key == SDLK_s:
            Booster_state.booster_change(get_time(), 5.0)
            self.skill_time = get_time()
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_hit_box())
        if Magnet_state.return_magnet_time() != False:
            draw_rectangle(*self.get_magnet_hit_box())

    def G_force(self):
        if game_world.game_speed <= 0.0: return
        h = (self.jumpTime * self.jumpTime * (-self.Graity) / 2) + (self.jumpTime * self.jumpPower)
        self.jumpTime = self.jumpTime + PLAYER_SPEED_PPS * game_framework.frame_time * max(1.0,Booster_state.return_booster_speed() / 2)
        return h

    def get_hit_box(self):
        return self.x - 35, self.y - 60, self.x + 35, self.y + 45

    def get_magnet_hit_box(self):
        pos = Magnet_state.return_magnet_pos()
        draw_in_size = 300
        return pos[0] - draw_in_size, pos[1] - draw_in_size, pos[0] + draw_in_size, pos[1] + draw_in_size

    def handle_collision(self, group, other):
        if group == 'player:point_object':
            self.score += 10 * point_object_level
            print("score : ", self.score)
        if group == 'player:coin_object':
            self.coin += 10
            print("coin : ", self.coin)

        if group == 'player:booster_object':
            if Booster_state.return_booster_time() == False:
                Booster_state.booster_change(get_time(), 3.0)

        if group == 'player:magnet_object':
            Magnet_state.magnet_change(get_time())
            Magnet_state.update_magnet_pos(self.x, self.y)
