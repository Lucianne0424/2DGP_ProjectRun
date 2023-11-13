from pico2d import draw_rectangle

import game_framework
import game_world
import object_information

from game_world import canvasSIZE, remove_object
from global_variable import OBJECT_SPEED_PPS, Booster_state
from image_load import image_load




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

    def draw(self):
        self.image.draw(self.x, self.y, 40, 40)
        draw_rectangle(*self.get_hit_box())

    def get_hit_box(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, group, other):
        if group == 'player:booster_object':
            game_world.remove_object(self)
