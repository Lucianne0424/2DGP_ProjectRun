from pico2d import draw_rectangle, load_image

from SourceCode.Etc import game_speed, global_variable
from SourceCode.Etc.game_world import remove_object


class TileObject:
    image = []
    draw_size = [ 100, 35 ]
    def __init__(self, index, x, y = -50):
        self.index, self.x, self.y = index, x, y

        if not TileObject.image:
            for i in range(4):
                TileObject.image.append(load_image('.//img//Tile//stage_1//Stage_1_bottom_tile_' + str(i) + '.png'))
            for i in range(4):
                TileObject.image.append(load_image('.//img//Tile//stage_1//Stage_1_top_tile_' + str(i) + '.png'))

        self.w = TileObject.draw_size[self.index % 2]
        self.h = TileObject.image[self.index].h


    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
        if self.x <= -300:
            remove_object(self)



    def draw(self):
        TileObject.image[self.index].draw(self.x, self.y, self.w, self.h)
        draw_rectangle(*self.get_hit_box())

    def get_hit_box(self):
        return self.x - self.w / 2, self.y - self.h / 2, self.x + self.w / 2, self.y + self.h / 2

    def handle_collision(self, group, other):
        pass
