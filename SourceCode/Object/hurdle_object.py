from pico2d import load_image, load_wav

from SourceCode.Etc import game_speed
from SourceCode.Etc.game_world import remove_object
from SourceCode.Object.booster_object import Booster_state


class HurdleObject:
    Hurdle_names = [('Ghost', 14), ('hurdle_high', 1), ('hurdle_low', 1)]
    image = {}
    type = 'Hurdle'
    sound = []

    def __init__(self, hurdleName, x, y):
        self.x, self.y = x, y
        self.hurdleName = hurdleName

        if not HurdleObject.image:
            for name in HurdleObject.Hurdle_names:
                HurdleObject.image[name[0]] = [load_image('.//img//Hurdle//stage_1//' + name[0] + '//' + name[0] + '_' + str(i) + '.png') for i in range(0, name[1])]

        for name in HurdleObject.Hurdle_names:
            if name[0] == hurdleName:
                self.max_frame = name[1]

        if not HurdleObject.sound:
            HurdleObject.sound.append(load_wav('.//Sound//g_obs2.ogg'))
            HurdleObject.sound[0].set_volume(20)
            HurdleObject.sound.append(load_wav('.//Sound//g_obs1.ogg'))
            HurdleObject.sound[1].set_volume(20)

        self.w = HurdleObject.image[self.hurdleName][0].w
        self.h = HurdleObject.image[self.hurdleName][0].h

        self.flying_toggle = False
        self.acceleration = 10.0
        self.rotate = 0.0
        self.frame = 0.0

    def __setstate__(self, state):
        self.__init__(state['hurdleName'], state['x'], state['y'])

    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
        self.frame = (self.frame + game_speed.Game_Speed.return_frame_speed(game_speed.HURDLE_ACTION_PER_TIME)) % self.max_frame

        if self.x <= 0 - self.w:
            remove_object(self)

        if self.flying_toggle:
            self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS) * 2
            self.y += game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS) * self.acceleration
            deceleration = self.acceleration - game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS) * 0.05
            self.acceleration = max(deceleration, 1.0)

    def draw(self):
        if self.flying_toggle:
            self.image[self.hurdleName][int(self.frame)].rotate_draw(self.rotate, self.x, self.y)
            self.rotate += 1.0
        else:
            self.image[self.hurdleName][int(self.frame)].draw(self.x, self.y)

    def get_hit_box(self):
        return self.x - self.w / 2, self.y - self.h / 2, self.x + self.w / 2, self.y + self.h / 2

    def handle_collision(self, group, other):
        if group == 'player:hurdle_object':
            if Booster_state.return_booster_time():
                HurdleObject.sound[0].play()
                self.flying_toggle = True
            else:
                HurdleObject.sound[1].play()
