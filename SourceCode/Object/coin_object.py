from pico2d import draw_rectangle

from SourceCode.Etc import game_speed
from SourceCode.Etc.game_world import remove_object
from SourceCode.Etc.global_variable import canvasSIZE
from SourceCode.Etc.image_load import image_load
from SourceCode.Object.magnet_object import Magnet_state


class CoinObject:
    image = None

    def __init__(self, y=1):
        self.x = canvasSIZE[0] + 30
        self.y = y
        if CoinObject.image == None:
            CoinObject.image = image_load('.//img//Coin', "Coin.png")

    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
        if self.x <= 0 - 30:
            remove_object(self)
        self.x, self.y = Magnet_state.magnet_checking(self.x, self.y)

    def draw(self):
        self.image.draw(self.x, self.y, 30, 30)
        draw_rectangle(*self.get_hit_box())

    def get_hit_box(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def handle_collision(self, group, other):
        if group == 'player:coin_object':
            remove_object(self)
