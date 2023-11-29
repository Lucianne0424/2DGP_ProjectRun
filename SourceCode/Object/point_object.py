from pico2d import draw_rectangle, load_image

from SourceCode.Etc import game_speed, game_world
from SourceCode.Etc.global_variable import canvasSIZE
from SourceCode.Object.magnet_object import Magnet_state

point_object_level = 1  # 점수 오브젝트 레벨


def point_object_level_image_load():
    name = './/img//Point//'
    name += 'point_item_candy'
    name += str(point_object_level)
    name += '.png'
    return name


class PointObject:
    image = None
    level = 0  # point_object_level과 level의 값이 다르면 이미지를 새롭게 로드한다.

    def __init__(self, x, y):
        self.x, self.y = x, y

        if PointObject.image == None:
            PointObject.image = load_image(point_object_level_image_load())
            PointObject.level = point_object_level

    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
        if self.x <= 0 - 30:
            game_world.remove_object(self)
        if point_object_level != PointObject.level:
            PointObject.image = load_image(point_object_level_image_load())
            PointObject.level = point_object_level
        self.x, self.y = Magnet_state.magnet_checking(self.x, self.y)

    def draw(self):
        self.image.draw(self.x, self.y, 30, 30)
        draw_rectangle(*self.get_hit_box())

    def get_hit_box(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def handle_collision(self, group, other):
        if group == 'player:point_object':
            game_world.remove_object(self)
