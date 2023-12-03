from pico2d import draw_rectangle, get_time, load_image, load_wav, load_music
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_1, SDLK_s

from SourceCode.Etc import game_speed, game_framework, global_variable
from SourceCode.Etc.global_variable import hpLevel, stage
from SourceCode.Mode import game_over_mode
from SourceCode.Object.booster_object import Booster_state
from SourceCode.Object.magnet_object import Magnet_state
from SourceCode.Object.point_object import point_object_level

jumpAcceleration = 2.0
jumpPower = 30

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
        player.state_machine.handle_event(('GameOver', player.Hp))

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
        player.game_over_sound.play()


    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = min((player.frame + 10 * game_speed.ACTION_PER_TIME * game_framework.frame_time), 10)

        if player.frame == 10:
            game_speed.speed = 0
            player.BGM.stop()
            global_variable.coin = player.coin
            global_variable.playerCoin = player.coin
            game_framework.change_mode(game_over_mode)

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
        player.frame = 0
        player.count = 0
        player.jumpAcceleration = jumpAcceleration
        Girl_Character.jump_sound.play()


    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = min(6, (player.frame + 6 * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)))

        force = player.G_force()
        if force <= 0:
            player.state_machine.handle_event(('END_ACTION', 0))
        else:
            player.y += force

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
        player.jumpAcceleration = jumpAcceleration
        Girl_Character.jump_sound.play()


    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = min(5, (player.frame + 5 * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)))
        force = player.G_force()

        if force <= 0:
            player.state_machine.handle_event(('END_ACTION', 0))
        else:
            player.y += force

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
            Run: {end_action: Run, space_down: JumpStart, game_over: GameOver, Key_down_1: Damage, damage: Damage},
            JumpStart: {end_action: JumpFall, space_down: DoubleJumpStart, damage: Damage, game_over: GameOver},
            JumpFall: {end_action: Landing, space_down: DoubleJumpStart, damage: Damage, game_over: GameOver},
            DoubleJumpStart: {end_action: DoubleJumpFall, damage: Damage, game_over: GameOver},
            DoubleJumpFall: {end_action: Landing, damage: Damage, game_over: GameOver},
            Landing: {end_action: Run, space_down: JumpStart, damage: Damage, game_over: GameOver},

            GameOver: {game_over: GameOver},
            Damage: {end_action: Run, game_over: GameOver}
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
    jump_sound = None
    BGM = None
    game_over_sound = None

    def __init__(self):
        self.x, self.y, self.max_y = 300, 150, 150
        self.MaxHp = 100.0 + (hpLevel * 20)
        self.Hp = self.MaxHp
        self.frame = 0

        self.Graity = 0.398
        self.jumpAcceleration = -1.0
        self.game_over_toggle = False

        if not Girl_Character.jump_sound:
            Girl_Character.jump_sound = load_wav('.//Sound//jump_sound.ogg')
            Girl_Character.jump_sound.set_volume(32)

        if not Girl_Character.game_over_sound:
            Girl_Character.game_over_sound = load_wav('.//Sound//game_over_sound.ogg')
            Girl_Character.game_over_sound.set_volume(32)


        if not Girl_Character.BGM:
            Girl_Character.BGM = load_music('.//Sound//bgm_main'+ str(stage) + '.ogg')
            Girl_Character.BGM.set_volume(50)
        Girl_Character.BGM.repeat_play()



        self.coin = 0

        self.images = {}
        for name in Girl_Character.animation_names:
            self.images[name[0]] = [
                load_image('.//img//Character//Girl//' + name[0] + '//' + name[0] + '_' + str(i) + '.png') for i in range(0, name[1])]

        self.state_machine = StateMachine(self)
        self.state_machine.start()

        self.invincible_time = False
        self.skill_time = False
        self.fall_tile_collision = False


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
        if self.y <= -200 and self.game_over_toggle == False:
            self.Hp = 0.0
            self.game_over_toggle = True
            self.state_machine.handle_event(('GameOver', self.Hp))

    def handle_event(self, event):
        if self.skill_time == False and event.key == SDLK_s:
            Booster_state.booster_change(get_time(), 3.0)
            self.skill_time = get_time()
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_hit_box())
        if Magnet_state.return_magnet_time() != False:
            draw_rectangle(*self.get_magnet_hit_box())

    def G_force(self):
        y = game_speed.Game_Speed.return_spped(game_speed.PLAYER_SPEED_PPS) * self.jumpAcceleration * jumpPower
        self.jumpAcceleration -= self.Graity * game_speed.Game_Speed.return_spped(game_speed.PLAYER_SPEED_PPS)

        if y > 0:
            self.fall_tile_collision = True
            self.max_y = self.y - 30
            print(self.max_y)
        else:
            self.fall_tile_collision = False

        return y

    def get_hit_box(self):
        return self.x - 10, self.y - 60, self.x + 15, self.y + 45

    def get_magnet_hit_box(self):
        pos = Magnet_state.return_magnet_pos()
        draw_in_size = 300
        return pos[0] - draw_in_size, pos[1] - draw_in_size, pos[0] + draw_in_size, pos[1] + draw_in_size

    def handle_collision(self, group, other):
        if group == 'player:point_object':
            global_variable.score += 10 * point_object_level

        if group == 'player:coin_object':
            self.coin += 10
            global_variable.score += 15 * point_object_level

        if group == 'player:booster_object':
            if self.skill_time == False or not Booster_state.return_booster_time():
                Booster_state.booster_change(get_time(), 2.0)

        if group == 'player:magnet_object':
            Magnet_state.magnet_change(get_time())
            Magnet_state.update_magnet_pos(self.x, self.y)

        if group == 'player:tile_object':
            if not self.fall_tile_collision and self.max_y >= (other.y + other.h):
                self.y = (other.y + other.h) + 3
                self.max_y = (other.y + other.h) + 3
                self.jumpAcceleration = -1.0
                if self.state_machine.cur_state == JumpFall or self.state_machine.cur_state == DoubleJumpFall:
                    self.state_machine.handle_event(('END_ACTION', 0))

        if group == 'player:hurdle_object':
            if self.invincible_time == False and not Booster_state.return_booster_time():
                self.invincible_time = get_time()
                self.state_machine.handle_event(('Damage', 0))
            elif Booster_state.return_booster_time():
                global_variable.score += 30 * point_object_level


        if group == 'player:healing_object':
            self.Hp = min(self.MaxHp, self.Hp + 10)



