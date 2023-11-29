from pico2d import draw_rectangle, load_image

from SourceCode.Etc import game_speed, game_world
from SourceCode.Etc.global_variable import canvasSIZE
from SourceCode.Object.magnet_object import Magnet_state



class HealingObject:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if HealingObject.image == None:
            HealingObject.image = load_image('.//img//item//Healing.png')

    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
        if self.x <= 0 - 30:
            game_world.remove_object(self)
        self.x, self.y = Magnet_state.magnet_checking(self.x, self.y)

    def draw(self):
        self.image.draw(self.x, self.y, 40, 40)
        draw_rectangle(*self.get_hit_box())

    def get_hit_box(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, group, other):
        if group == 'player:healing_object':
            game_world.remove_object(self)
