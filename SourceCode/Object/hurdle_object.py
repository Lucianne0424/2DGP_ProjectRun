from pico2d import draw_rectangle, get_time, load_image

from SourceCode.Etc import game_speed
from SourceCode.Etc.game_world import remove_object
from SourceCode.Etc.global_variable import canvasSIZE
from SourceCode.Object.magnet_object import Magnet_state


class HurdleObject:
    Hurdle_names = [('Ghost', 14)]
    image = {}
    def __init__(self, hurdleName, y=100):
        self.x = canvasSIZE[0] + 30
        self.y = y
        self.hurdleName = hurdleName

        if not HurdleObject.image:
            for name in HurdleObject.Hurdle_names:
                HurdleObject.image[name[0]] = [load_image('.//img//Hurdle//stage_1//' + name[0] + '//' + name[0] + '_' + str(i) + '.png') for i in range(0, name[1])]

        self.w = HurdleObject.image[self.hurdleName][0].w
        self.h = HurdleObject.image[self.hurdleName][0].h


    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
        if self.x <= 0 - self.w:
            remove_object(self)

    def draw(self):
        self.image[self.hurdleName][0].draw(self.x, self.y)
        draw_rectangle(*self.get_hit_box())

    def get_hit_box(self):
        return self.x - self.w/2, self.y - self.h/2, self.x + self.w/2, self.y + self.h/2

    def handle_collision(self, group, other):
        if group == 'player:hurdle_object':
            pass
