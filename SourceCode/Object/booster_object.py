from pico2d import get_time, load_image, load_wav

from SourceCode.Etc import game_speed
from SourceCode.Etc.game_world import remove_object
from SourceCode.Object.magnet_object import Magnet_state


class Booster_state:
    booster_time = False
    booster_cooldown = 5.0
    booster_speed = 0.0

    @staticmethod
    def update(speed):
        if get_time() - Booster_state.return_booster_time() >= Booster_state.booster_cooldown and Booster_state.return_booster_time() != False:
            Booster_state.booster_change(False, speed)

    @staticmethod
    def booster_change(time, speed):
        Booster_state.booster_time = time
        Booster_state.booster_speed = speed

    @staticmethod
    def return_booster_time():
        return Booster_state.booster_time

    @staticmethod
    def return_booster_speed():
        return Booster_state.booster_speed

    @staticmethod
    def reset():
        Booster_state.booster_time = False
        Booster_state.booster_cooldown = 5.0
        Booster_state.booster_speed = 0.0



class BoosterObject:
    image = None
    type = 'Booster'
    sound = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if BoosterObject.image == None:
            BoosterObject.image = load_image('.//img//item//Booster.png')

        if not BoosterObject.sound:
            BoosterObject.sound = load_wav('.//Sound//item_sound.ogg')
            BoosterObject.sound.set_volume(32)

    def __setstate__(self, state):
        self.__init__(state['x'], state['y'])

    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
        if self.x <= 0 - 30:
            remove_object(self)
        self.x, self.y = Magnet_state.magnet_checking(self.x, self.y)

    def draw(self):
        self.image.draw(self.x, self.y, 40, 40)

    def get_hit_box(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, group, other):
        if group == 'player:booster_object':
            BoosterObject.sound.play()
            remove_object(self)
