from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_1
from SourceCode.Etc import game_speed, game_framework, global_variable
from SourceCode.Mode import game_over_mode

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
        player.max_frame = player.animation_names[player.action] - 1

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + player.max_frame * game_speed.ACTION_PER_TIME * game_framework.frame_time) % player.max_frame
        player.y += player.G_force()
        if player.frame >= player.max_frame - 1:
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
        player.max_frame = player.animation_names[player.action] - 1


    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = min(player.max_frame, (player.frame + player.max_frame * game_speed.ACTION_PER_TIME * game_framework.frame_time))

        if player.frame == player.max_frame:
            game_speed.speed = 0
            player.BGM.stop()
            global_variable.coin += player.coin
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
        player.max_frame = player.animation_names[player.action]

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + player.max_frame * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)) % player.max_frame
        player.y += player.G_force()
        if player.frame >= player.max_frame - 1:
            player.state_machine.handle_event(('END_ACTION', 0))

    @staticmethod
    def draw(player):
        player.images[player.action][int(player.frame)].draw(player.x, player.y)


class DoubleJumpFall:
    @staticmethod
    def entrance(player, event):
        player.action = 'Jump_Fall'
        player.frame = 0
        player.max_frame = player.animation_names[player.action] - 1

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = min(player.max_frame, (player.frame + player.max_frame * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)))
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
        player.jump_sound.play()
        player.max_frame = player.animation_names[player.action] - 1


    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = min(player.max_frame, (player.frame + player.max_frame * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)))

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
        player.max_frame = player.animation_names[player.action] - 1

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = min(player.max_frame, (player.frame + player.max_frame * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)))
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
        player.jump_sound.play()
        player.max_frame = player.animation_names[player.action] - 1


    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = min(player.max_frame, (player.frame + player.max_frame * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)))
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
        player.max_frame = player.animation_names[player.action]

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + player.max_frame * game_speed.Game_Speed.return_spped(game_speed.ACTION_PER_TIME)) % player.max_frame
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

