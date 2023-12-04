from pico2d import load_image, load_wav

from SourceCode.Etc import game_speed, game_world
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
    type = 'Point'
    sound = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if PointObject.image == None:
            PointObject.image = load_image(point_object_level_image_load())
            PointObject.level = point_object_level

    def __setstate__(self, state):
        self.__init__(state['x'], state['y'])

    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
        if self.x <= 0 - 30:
            game_world.remove_object(self)
        if point_object_level != PointObject.level:
            PointObject.image = load_image(point_object_level_image_load())
            PointObject.level = point_object_level

        if not PointObject.sound:
            PointObject.sound = load_wav('.//Sound//point_sound.ogg')
            PointObject.sound.set_volume(32)

        self.x, self.y = Magnet_state.magnet_checking(self.x, self.y)

    def draw(self):
        self.image.draw(self.x, self.y, 30, 30)

    def get_hit_box(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def handle_collision(self, group, other):
        if group == 'player:point_object':
            PointObject.sound.play()
            game_world.remove_object(self)


class UIPointObject:
    image = None
    level = 0  # point_object_level과 level의 값이 다르면 이미지를 새롭게 로드한다.
    type = 'UI'

    def __init__(self, x, y, size_x = 50, size_y = 50):
        self.x, self.y = x, y
        self.size_x, self.size_y = size_x, size_y

        if UIPointObject.image == None:
            UIPointObject.image = load_image(point_object_level_image_load())
            UIPointObject.level = point_object_level

    def __setstate__(self, state):
        self.__init__(state['x'], state['y'])

    def update(self):
        if point_object_level != UIPointObject.level:
            UIPointObject.image = load_image(point_object_level_image_load())
            UIPointObject.level = point_object_level

    def draw(self):
        self.image.draw(self.x, self.y, self.size_x, self.size_y)

    def get_hit_box(self):
        pass

    def handle_collision(self, group, other):
        pass

