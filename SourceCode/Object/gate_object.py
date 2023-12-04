from pico2d import load_image, load_wav

from SourceCode.Etc import game_speed, game_world, global_variable, game_framework
from SourceCode.Mode import game_over_mode
from SourceCode.Object.magnet_object import Magnet_state


class GateObject:
    type = 'Clear'
    sound = None
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if GateObject.image == None:
            GateObject.image = load_image('.//img//Gate//gate.png')
        if GateObject.sound == None:
            GateObject.sound = load_wav('.//Sound//score_mode_sound.ogg')
            GateObject.sound.set_volume(32)

        self.w = GateObject.image.w
        self.h = GateObject.image.h

    def __setstate__(self, state):
        self.__init__(state['x'], state['y'])

    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
        if self.x <= 0 - 30:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_hit_box(self):
        return self.x - self.w / 2 - 550, self.y - self.h / 2 - 500, self.x + self.w / 2, self.y + self.h / 2 + 500

    def handle_collision(self, group, other):
        if group == 'player:gate_object':
            GateObject.sound.play()
            game_speed.speed = 0
            other.BGM.stop()
            global_variable.coin = other.coin
            global_variable.playerCoin = other.coin
            game_framework.change_mode(game_over_mode)
