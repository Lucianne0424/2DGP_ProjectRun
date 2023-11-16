from pico2d import draw_rectangle

from SourceCode.Etc import game_speed
from SourceCode.Etc.game_world import remove_object
from SourceCode.Etc.global_variable import canvasSIZE
from SourceCode.Etc.image_load import image_load
from SourceCode.Object.magnet_object import Magnet_state

booster_time = False
booster_speed = 0.0


class Booster_state:
    @staticmethod
    def booster_change(time, speed):
        global booster_time
        global booster_speed
        booster_time = time
        booster_speed = speed

    @staticmethod
    def return_booster_time():
        return booster_time

    @staticmethod
    def return_booster_speed():
        return booster_speed


class BoosterObject:
    image = None

    def __init__(self, y=1):
        self.x = canvasSIZE[0] + 30
        self.y = y
        if BoosterObject.image == None:
            BoosterObject.image = image_load('.//img//item', "Booster.png")

    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
        if self.x <= 0 - 30:
            remove_object(self)
        self.x, self.y = Magnet_state.magnet_checking(self.x, self.y)

    def draw(self):
        self.image.draw(self.x, self.y, 40, 40)
        draw_rectangle(*self.get_hit_box())

    def get_hit_box(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, group, other):
        if group == 'player:booster_object':
            remove_object(self)
