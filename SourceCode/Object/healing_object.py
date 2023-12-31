from pico2d import load_image, load_wav

from SourceCode.Etc import game_speed, game_world
from SourceCode.Object.magnet_object import Magnet_state


class HealingObject:
    image = None
    type = 'Healing'
    sound = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if HealingObject.image == None:
            HealingObject.image = load_image('.//img//item//Healing.png')

        if not HealingObject.sound:
            HealingObject.sound = load_wav('.//Sound//item_sound.ogg')
            HealingObject.sound.set_volume(32)

    def __setstate__(self, state):
        self.__init__(state['x'], state['y'])

    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
        if self.x <= 0 - 30:
            game_world.remove_object(self)
        self.x, self.y = Magnet_state.magnet_checking(self.x, self.y)

    def draw(self):
        self.image.draw(self.x, self.y, 40, 40)

    def get_hit_box(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, group, other):
        if group == 'player:healing_object':
            HealingObject.sound.play()
            game_world.remove_object(self)
