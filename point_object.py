from game_world import canvasSIZE, remove_object, add_object
from image_load import image_load


point_object_level = 1 # 점수 오브젝트 레벨
PO_gap_count = 0 # 점수 오브젝트 일정 간격마다 출력하기 위한 변수

def add_point_object(): # 일정 간격으로 점수 오브젝트 출력
    global PO_gap_count
    PO_gap_count = (PO_gap_count + 1) % 10
    if PO_gap_count == 10 - 1:
        add_object(PointObject(), 2)


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
        self.x -= 10
        if self.x <= 0 - 30:
            remove_object(self)

    def draw(self):
        self.image.draw(self.x, 50 + self.y * 50, 30, 30)
