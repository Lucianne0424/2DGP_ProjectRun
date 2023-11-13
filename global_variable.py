PIXEL_PER_METER = (10.0 / 0.3)

OBJECT_SPEED_KMPH = 30.0
OBJECT_SPEED_PPS = ((OBJECT_SPEED_KMPH * 1000.0 / 60.0) / 60.0) * PIXEL_PER_METER

BACKGROUND_SPEED_KMPH = 20.0
BACKGROUND_SPEED_PPS = ((BACKGROUND_SPEED_KMPH * 1000.0 / 60.0) / 60.0) * PIXEL_PER_METER

coin = 0
stage = 1

booster_time = False
booster_speed = 1.0


class Booster_state:
    @staticmethod
    def booster_change(time, speed):
        global booster_time
        global booster_speed
        booster_time = time
        booster_speed = speed

    @staticmethod
    def return_booster_time():
        return booster_time

    @staticmethod
    def return_booster_speed():
        return booster_speed


magnet_time = False
magnet_pos = []


class Magnet_state:
    @staticmethod
    def magnet_change(time):
        global magnet_time
        magnet_time = time

    @staticmethod
    def return_magnet_time():
        return magnet_time

    @staticmethod
    def return_magnet_pos():
        return magnet_pos

    @staticmethod
    def update_magnet_pos(x, y):
        global magnet_pos
        magnet_pos = [x, y]

    @staticmethod
    def magnet_draw_in(x, y):
        if Magnet_state.return_magnet_time() == False: return False

        pos1 = Magnet_state.return_magnet_pos()
        draw_in_size = 300
        if pos1[0] - draw_in_size <= x and pos1[0] + draw_in_size >= x and pos1[1] - draw_in_size <= y and pos1[1] + draw_in_size >= y:
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