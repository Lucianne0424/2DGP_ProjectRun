from pico2d import draw_rectangle, load_image

from SourceCode.Etc import game_speed, global_variable
from SourceCode.Etc.game_world import remove_object


class TileObject:
    image = []
    test = None
    def __init__(self, index, x, y = -50):
        self.x = x
        self.y = y
        self.index = index
        if not TileObject.image:
            for i in range(4):
                TileObject.image.append(load_image('.//img//Tile//stage_1//Stage_1_bottom_tile_' + str(i) + '.png'))
        self.w = TileObject.image[self.index].w
        self.h = TileObject.image[self.index].h

    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)


    def draw(self):
        if self.x > 0 - self.w and self.x <= global_variable.canvasSIZE[0]:
            TileObject.image[self.index].draw_to_origin(self.x, self.y)
            draw_rectangle(*self.get_hit_box())

    def get_hit_box(self):
        return self.x, self.y, self.x + self.w, self.y + self.h

    def handle_collision(self, group, other):
        pass
