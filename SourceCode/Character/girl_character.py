from pico2d import draw_rectangle, get_time, load_image
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_1, SDLK_s

from SourceCode.Etc import game_speed, game_framework
from SourceCode.Etc.global_variable import hpLevel
from SourceCode.Object.booster_object import Booster_state
from SourceCode.Object.magnet_object import Magnet_state
from SourceCode.Object.point_object import point_object_level

jumpPower = 2.0

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def Key_down_1(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_1


def end_action(e):
    return e[0] == 'END_ACTION'


def game_over(e):
    return e[0] == 'GameOver' and e[1] <= 0.0

def damage(e):
    return e[0] == 'Damage'


class Damage:
    @staticmethod
    def entrance(player, event):
        player.action = 'Damage'
        player.frame = 0
        player.Hp -= 10

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 7 * game_speed.ACTION_PER_TIME * game_framework.frame_time) % 7
        player.y += player.G_force()
        if player.frame >= 6:
            player.state_machine.handle_event(('END_ACTION', 0))


    @staticmethod
    def draw(player):
        player.images[player.action][int(player.frame)].draw(player.x, player.y)


class GameOver:
    @staticmethod
    def entrance(player, event):
        player.action = 'GameOver'
        player.frame = 0

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = min((player.frame + 10 * game_speed.ACTION_PER_TIME * game_framework.frame_time), 10)

    @staticmethod
    def draw(player):
        player.images[player.action][int(player.frame)].draw(player.x, player.y)


class Landing:
    @staticmethod
    def entrance(player, event):
        player.action = 'Landing'
        player.frame = 0

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 4 * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)) % 4
        player.y += player.G_force()
        if player.frame >= 3:
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.images[player.action][int(player.frame)].draw(player.x, player.y)


class DoubleJumpFall:
    @staticmethod
    def entrance(player, event):
        player.action = 'Jump_Fall'
        player.frame = 0

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = min((player.frame + 5 * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)), 5)
        player.y += player.G_force()

    @staticmethod
    def draw(player):
        player.images[player.action][int(player.frame)].draw(player.x, player.y)


class DoubleJumpStart:
    @staticmethod
    def entrance(player, event):
        player.action = 'Double_Jump_Start'
        player.frame = 2
        player.count = 0
        player.jumpPower = jumpPower


    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 8 * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)) % 8
        player.y += player.G_force()

        if player.frame >= 7:
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.images[player.action][int(player.frame)].draw(player.x, player.y)


class JumpFall:
    @staticmethod
    def entrance(player, event):
        player.action = 'Jump_Fall'
        player.frame = 0

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = min((player.frame + 5 * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)), 5)
        player.y += player.G_force()

    @staticmethod
    def draw(player):
        player.images[player.action][int(player.frame)].draw(player.x, player.y)


class JumpStart:
    @staticmethod
    def entrance(player, event):
        player.action = 'Jump_Start'
        player.frame = 0
        player.jumpPower = jumpPower


    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 7 * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)) % 7
        player.y += player.G_force()
        if player.frame >= 6:
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.images[player.action][int(player.frame)].draw(player.x, player.y)


class Run:
    @staticmethod
    def entrance(player, event):
        player.action = 'Run'
        player.frame = 0

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 10 * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)) % 10
        player.y += player.G_force()
        player.state_machine.handle_event(('GameOver', player.Hp))

    @staticmethod
    def draw(player):
        player.images[player.action][int(player.frame)].draw(player.x, player.y)


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.cur_state = Run
        self.transitions = {
            Run: {space_down: JumpStart, game_over: GameOver, Key_down_1: Damage, damage: Damage},
            JumpStart: {end_action: JumpFall, space_down: DoubleJumpStart, damage: Damage},
            JumpFall: {end_action: Landing, space_down: DoubleJumpStart, damage: Damage},
            DoubleJumpStart: {end_action: DoubleJumpFall, damage: Damage},
            DoubleJumpFall: {end_action: Landing, damage: Damage},
            Landing: {end_action: Run, space_down: JumpStart, damage: Damage},

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


class Girl_Character:
    animation_names = [('Run', 10), ('Jump_Start', 6), ('Jump_Fall', 6), ('Landing', 3),
                       ('Double_Jump_Start', 7), ('GameOver', 11), ('Damage', 7)]

    def __init__(self):
        self.x, self.y = 300, 100
        self.MaxHp = 100.0 + (hpLevel * 20)
        self.Hp = self.MaxHp
        self.frame = 0

        self.Graity = 0.398
        self.jumpPower = -1.0
        self.jumpTime = 1.0

        self.score = 0
        self.coin = 0

        self.images = {}
        for name in Girl_Character.animation_names:
            self.images[name[0]] = [
                load_image('.//img//Character//Girl//' + name[0] + '//' + name[0] + '_' + str(i) + '.png') for i in range(0, name[1])]

        self.state_machine = StateMachine(self)
        self.state_machine.start()

        self.invincible_time = False
        self.skill_time = False

    def update(self):
        self.Hp = self.Hp - 1.0 * game_framework.frame_time
        print('Hp : ', self.Hp)
        self.state_machine.update()
        Booster_state.update(0.0)
        Magnet_state.update(self.x, self.y)
        if self.skill_time != False and get_time() - self.skill_time >= 10:
            self.skill_time = False
        if self.invincible_time != False and get_time() - self.invincible_time >= 2:
            self.invincible_time = False

    def handle_event(self, event):
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
        mul_speed = max(1.0, Booster_state.return_booster_speed() / 2)
        y = self.jumpPower * mul_speed
        self.jumpPower -= self.Graity * (game_speed.PLAYER_SPEED_PPS * game_framework.frame_time) * mul_speed

        return y

    def get_hit_box(self):
        return self.x - 35, self.y - 60, self.x + 35, self.y + 45

    def get_magnet_hit_box(self):
        pos = Magnet_state.return_magnet_pos()
        draw_in_size = 300
        return pos[0] - draw_in_size, pos[1] - draw_in_size, pos[0] + draw_in_size, pos[1] + draw_in_size

    def handle_collision(self, group, other):
        if group == 'player:point_object':
            self.score += 10 * point_object_level

        if group == 'player:coin_object':
            self.coin += 10

        if group == 'player:booster_object':
            if self.skill_time == False:
                Booster_state.booster_change(get_time(), 3.0)

        if group == 'player:magnet_object':
            Magnet_state.magnet_change(get_time())
            Magnet_state.update_magnet_pos(self.x, self.y)

        if group == 'player:tile_object':
            self.y = + 60 + other.y + other.h
            self.jumpPower = -1.0
            if self.state_machine.cur_state == JumpFall or self.state_machine.cur_state == DoubleJumpFall:
                self.state_machine.handle_event(('END_ACTION', 0))

        if group == 'player:hurdle_object':
            if self.invincible_time == False and not Booster_state.return_booster_time():
                self.invincible_time = get_time()
                self.state_machine.handle_event(('Damage', 0))

        if group == 'player:healing_object':
            self.Hp = min(self.MaxHp, self.Hp + 10)



