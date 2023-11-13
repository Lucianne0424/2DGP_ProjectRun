from pico2d import draw_rectangle

import game_framework
import game_world
from game_world import canvasSIZE, remove_object
from image_load import image_load
from object_information import OBJECT_SPEED_PPS

point_object_level = 1  # 점수 오브젝트 레벨


def point_object_level_image_load():
    name = 'point_item_candy'
    name += str(point_object_level)
    name += '.png'
    return name


class PointObject:
    image = None
    level = 0  # point_object_level과 level의 값이 다르면 이미지를 새롭게 로드한다.

    def __init__(self, y=1):
        self.x = canvasSIZE[0] + 30
        self.y = y
        if PointObject.image == None:
            PointObject.image = image_load('.//img//Point', point_object_level_image_load())
            PointObject.level = point_object_level

    def update(self):
        self.x -= (OBJECT_SPEED_PPS * game_framework.frame_time) * game_world.game_speed
        if self.x <= 0 - 30:
            remove_object(self)
        if point_object_level != PointObject.level:
            PointObject.image = image_load('.//img//Point', point_object_level_image_load())
            PointObject.level = point_object_level

    def draw(self):
        self.image.draw(self.x, self.y, 30, 30)
        draw_rectangle(*self.get_hit_box())

    def get_hit_box(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def handle_collision(self, group, other):
        if group == 'player:point_object':
            game_world.remove_object(self)
