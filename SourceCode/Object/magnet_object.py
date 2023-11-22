from pico2d import draw_rectangle, get_time, load_image

from SourceCode.Etc import game_speed
from SourceCode.Etc.game_world import remove_object
from SourceCode.Etc.global_variable import canvasSIZE


class Magnet_state:
    magnet_time = False
    magnet_cooldown = 5.0
    magnet_pos = []
    magnet_range_size = 300

    @staticmethod
    def update(x, y):
        if Magnet_state.return_magnet_time() != False:
            Magnet_state.update_magnet_pos(x, y)
            if get_time() - Magnet_state.return_magnet_time() >= Magnet_state.magnet_cooldown:
                Magnet_state.magnet_change(False)


    @staticmethod
    def magnet_change(time):
        Magnet_state.magnet_time = time

    @staticmethod
    def return_magnet_time():
        return Magnet_state.magnet_time

    @staticmethod
    def return_magnet_pos():
        return Magnet_state.magnet_pos

    @staticmethod
    def update_magnet_pos(x, y):
        Magnet_state.magnet_pos = [x, y]

    @staticmethod
    def magnet_draw_in(x, y):
        if Magnet_state.return_magnet_time() == False: return False

        pos1 = Magnet_state.return_magnet_pos()
        if pos1[0] - Magnet_state.magnet_range_size <= x and pos1[0] + Magnet_state.magnet_range_size >= x and pos1[1] - Magnet_state.magnet_range_size <= y and pos1[1] + Magnet_state.magnet_range_size >= y:
            if pos1[0] > x:
                t = 0.1
            else:
                t = 0.01
            x1 = (1 - t) * x + t * pos1[0]
            y1 = (1 - t) * y + t * pos1[1]
            return [x1, y1]
        return [False, False]

    @staticmethod
    def magnet_checking(x, y):
        if Magnet_state.return_magnet_time() != False:
            tx, ty = Magnet_state.magnet_draw_in(x, y)
            if tx != False:
                return tx, ty
            else:
                return x, y
        return x, y


class MagnetObject:
    image = None

    def __init__(self, y=1):
        self.x = canvasSIZE[0] + 30
        self.y = y
        if MagnetObject.image == None:
            MagnetObject.image = load_image('.//img//item//magnet.png')

    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.OBJECT_SPEED_PPS)
        if self.x <= 0 - 30:
            remove_object(self)
        self.x, self.y = Magnet_state.magnet_checking(self.x, self.y)

    def draw(self):
        self.image.draw(self.x, self.y, 40, 40)
        draw_rectangle(*self.get_hit_box())

    def get_hit_box(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, group, other):
        if group == 'player:magnet_object':
            remove_object(self)
