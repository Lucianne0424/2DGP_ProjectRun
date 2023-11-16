from pico2d import draw_rectangle

import game_framework
import game_world

from game_world import canvasSIZE, remove_object
from global_variable import OBJECT_SPEED_PPS
from image_load import image_load
from magnet_object import Magnet_state

booster_time = False
booster_speed = 1.0


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
        self.x -= (OBJECT_SPEED_PPS * game_framework.frame_time) * game_world.game_speed * Booster_state.return_booster_speed()
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
            game_world.remove_object(self)
