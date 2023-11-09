from pico2d import draw_rectangle

import game_framework
import game_world
from game_world import canvasSIZE, remove_object, add_object
from image_load import image_load
from object_information import setting_stage

point_object_level = 1 # 점수 오브젝트 레벨
PO_gap_count = 0 # 점수 오브젝트 일정 간격마다 출력하기 위한 변수
point_object_load_count = 0 # 점수 오브젝트의 배치 정보를 저장한 리스트의 인덱스 값

point_object_information = setting_stage()
point_object_information_len = len(point_object_information)


PIXEL_PER_METER = (10.0 / 0.3)
P_O_SPEED_KMPH = 30.0
P_O_SPEED_MPM = (P_O_SPEED_KMPH * 1000.0 / 60.0)
P_O_SPEED_MPS = (P_O_SPEED_MPM / 60.0)
P_O_SPEED_PPS = (P_O_SPEED_MPS * PIXEL_PER_METER)


def add_point_object(): # 일정 간격으로 점수 오브젝트 출력
    global PO_gap_count
    global point_object_load_count
    PO_gap_count = (PO_gap_count + 1.0 * game_framework.frame_time)
    if PO_gap_count >= 0.2: # 1초에 점수 오브젝트 5개 생성
        PO_gap_count = 0
        object_create = PointObject(50 + point_object_information[point_object_load_count] * 50)
        add_object(object_create, 2)
        point_object_load_count = (point_object_load_count + 1) % point_object_information_len
        game_world.add_collision_pair('player:object', None, object_create)


def point_object_level_image_load():
    name = 'point_item_candy'
    name += str(point_object_level)
    name += '.png'
    return name

class PointObject:
    image = None
    def __init__(self, y = 1):
        self.x = canvasSIZE[0] + 30
        self.y = y
        if PointObject.image == None:
            PointObject.image = image_load('.//img//Point', point_object_level_image_load())

    def update(self):
        self.x -= P_O_SPEED_PPS * game_framework.frame_time
        if self.x <= 0 - 30:
            remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y, 30, 30)
        draw_rectangle(*self.get_hit_box())

    def get_hit_box(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def handle_collision(self, group, other):
        if group == 'player:object':
            game_world.remove_object(self)