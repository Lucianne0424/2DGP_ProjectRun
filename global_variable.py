PIXEL_PER_METER = (10.0 / 0.3)

OBJECT_SPEED_KMPH = 30.0
OBJECT_SPEED_PPS = ((OBJECT_SPEED_KMPH * 1000.0 / 60.0) / 60.0) * PIXEL_PER_METER

BACKGROUND_SPEED_KMPH = 20.0
BACKGROUND_SPEED_PPS = ((BACKGROUND_SPEED_KMPH * 1000.0 / 60.0) / 60.0) * PIXEL_PER_METER


booster_time = False
booster_speed = 1.0

coin = 0
stage = 1


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