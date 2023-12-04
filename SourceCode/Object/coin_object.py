from pico2d import load_image, load_wav

from SourceCode.Etc import game_speed
from SourceCode.Etc.game_world import remove_object
from SourceCode.Object.magnet_object import Magnet_state


class CoinObject:
    image = None
    type = 'Coin'
    sound = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if CoinObject.image == None:
            CoinObject.image = load_image('.//img//Coin//Coin.png')

        if not CoinObject.sound:
            CoinObject.sound = load_wav('.//Sound//coin_sound.ogg')
            CoinObject.sound.set_volume(32)

    def __setstate__(self, state):
        self.__init__(state['x'], state['y'])

    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
        if self.x <= 0 - 30:
            remove_object(self)
        self.x, self.y = Magnet_state.magnet_checking(self.x, self.y)

    def draw(self):
        self.image.draw(self.x, self.y, 30, 30)

    def get_hit_box(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def handle_collision(self, group, other):
        if group == 'player:coin_object':
            CoinObject.sound.play()
            remove_object(self)
