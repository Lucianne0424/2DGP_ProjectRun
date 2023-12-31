# 미터당 몇 픽셀인지
from pico2d import get_time

from SourceCode.Etc import game_framework
from SourceCode.Object import booster_object, magnet_object

# 픽셀당 미터 계산
PIXEL_PER_METER = (10.0 / 0.3)

# 오브젝트 속도
OBJECT_SPEED_KMPH = 30.0
OBJECT_SPEED_PPS = ((OBJECT_SPEED_KMPH * 1000.0 / 60.0) / 60.0) * PIXEL_PER_METER

# 배경 오브젝트 속도
BACKGROUND_SPEED_KMPH = 20.0
BACKGROUND_SPEED_PPS = ((BACKGROUND_SPEED_KMPH * 1000.0 / 60.0) / 60.0) * PIXEL_PER_METER

# 플레이어 오브젝트 점프 속도
PLAYER_SPEED_KMPH = 1.5
PLAYER_SPEED_PPS = ((PLAYER_SPEED_KMPH * 1000.0 / 60.0) / 60.0) * PIXEL_PER_METER

# 플레이어 애니메이션 속도
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

# 장애물 속도
HURDLE_TIME_PER_ACTION = 0.05
HURDLE_ACTION_PER_TIME = 1.0 / HURDLE_TIME_PER_ACTION

# 게임 속도
speed = 1.0
pauseTime = False

class Game_Speed:
    @staticmethod
    def return_spped(PPS):
        return (PPS * game_framework.frame_time) * (speed + booster_object.Booster_state.return_booster_speed())

    @staticmethod
    def return_frame_speed(PPS):
        return (PPS * game_framework.frame_time)

    @staticmethod
    def pauseGame():
        if speed <= 0.0:
            global pauseTime
            if pauseTime == False:
                pauseTime = get_time()
                print(pauseTime)
            return False
        else:
            if pauseTime != False:
                Game_Speed.sustainment_time_update(Game_Speed.get_pause_time())
                pauseTime = False
            return True

    @staticmethod
    def get_pause_time():
        return get_time() - pauseTime

    @staticmethod
    def sustainment_time_update(add_time):
        if booster_object.Booster_state.booster_time != False:
            booster_object.Booster_state.booster_time += add_time
        if magnet_object.Magnet_state.magnet_time != False:
            magnet_object.Magnet_state.magnet_time += add_time