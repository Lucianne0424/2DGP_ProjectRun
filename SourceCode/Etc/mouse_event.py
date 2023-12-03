from SourceCode.Etc import game_world
from SourceCode.Etc.global_variable import canvasSIZE, depth

MousePos_x = 0
MousePos_y = 0

class Mouse_event:
    @staticmethod
    def mounse_collide(a, x, y):
        la, ba, ra, ta = a.get_hit_box()
        lb, bb, rb, tb = x - 5, y - 5, x + 5, y + 5

        if la > rb: return False
        if ra < lb: return False
        if ta < bb: return False
        if ba > tb: return False

        return True

    @staticmethod
    def return_mouse_pos(event):
        x, y = event.x, (canvasSIZE[1] - 1 - event.y)
        x = x // 10 * 10
        y = y // 10 * 10
        return x, y

    @staticmethod
    def collision_Ui_object():
        global MousePos_x, MousePos_y
        for i in game_world.objects[depth['Button']]:
            if Mouse_event.mounse_collide(i, MousePos_x, MousePos_y):
                return i

        return False
