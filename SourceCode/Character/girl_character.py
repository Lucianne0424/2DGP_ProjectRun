from pico2d import get_time, load_image, load_wav, load_music
from sdl2 import SDLK_s

from SourceCode.Character import state_machine
from SourceCode.Etc import game_speed, game_framework, global_variable
from SourceCode.Etc.global_variable import stage
from SourceCode.Object.booster_object import Booster_state
from SourceCode.Object.magnet_object import Magnet_state
from SourceCode.Object.point_object import point_object_level


class Girl_Character:
    name_list = ['Run', 'Jump_Start', 'Jump_Fall', 'Landing', 'Double_Jump_Start', 'GameOver', 'Damage']

    animation_names = {'Run': 10, 'Jump_Start': 6, 'Jump_Fall': 6, 'Landing': 3,
                       'Double_Jump_Start': 7, 'GameOver': 11, 'Damage': 7}

    jump_sound = None
    BGM = None
    game_over_sound = None

    def __init__(self):
        self.x, self.y, self.max_y = 300, 150, 150
        self.MaxHp = 50.0 + (global_variable.hpLevel * 10)
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
        for name in Girl_Character.name_list:
            self.images[name] = [
                load_image('.//img//Character//Girl//' + name + '//' + name + '_' + str(i) + '.png') for i in range(0, Girl_Character.animation_names[name])]

        self.state_machine = state_machine.StateMachine(self)
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
        if self.skill_time != False and get_time() - self.skill_time >= 30:
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

    def G_force(self):
        y = game_speed.Game_Speed.return_spped(game_speed.PLAYER_SPEED_PPS) * self.jumpAcceleration * state_machine.jumpPower
        self.jumpAcceleration -= self.Graity * game_speed.Game_Speed.return_spped(game_speed.PLAYER_SPEED_PPS)

        if y > 0:
            self.fall_tile_collision = True
            self.max_y = self.y - 30
        else:
            self.fall_tile_collision = False

        return y

    def get_hit_box(self):
        return self.x - 10, self.y - 60, self.x + 15, self.y + 45

    def get_magnet_hit_box(self):
        pos = Magnet_state.return_magnet_pos()
        draw_in_size = Magnet_state.magnet_range_size
        return pos[0] - draw_in_size, pos[1] - draw_in_size, pos[0] + draw_in_size, pos[1] + draw_in_size

    def handle_collision(self, group, other):
        if group == 'player:point_object':
            global_variable.score += 10 * point_object_level

        if group == 'player:coin_object':
            self.coin += 10
            global_variable.score += 15 * point_object_level

        if group == 'player:booster_object':
            Booster_state.booster_change(get_time(), 2.0)

        if group == 'player:magnet_object':
            Magnet_state.magnet_change(get_time())
            Magnet_state.update_magnet_pos(self.x, self.y)

        if group == 'player:tile_object':
            if not self.fall_tile_collision and self.max_y >= (other.y + other.h):
                self.y = (other.y + other.h) + 3
                self.max_y = (other.y + other.h) + 3
                self.jumpAcceleration = -1.0
                if self.state_machine.cur_state == state_machine.JumpFall or self.state_machine.cur_state == state_machine.DoubleJumpFall:
                    self.state_machine.handle_event(('END_ACTION', 0))

        if group == 'player:hurdle_object':
            if self.invincible_time == False and not Booster_state.return_booster_time():
                self.invincible_time = get_time()
                self.state_machine.handle_event(('Damage', 0))
            elif Booster_state.return_booster_time():
                global_variable.score += 30 * point_object_level


        if group == 'player:healing_object':
            self.Hp = min(self.MaxHp, self.Hp + 10)



