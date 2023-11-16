# 미터당 몇 픽셀인지
import game_framework
import booster_object

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

# 게임 속도
speed = 1.0


class Game_Speed:
    @staticmethod
    def return_spped(PPS):
        return (PPS * game_framework.frame_time) * speed * booster_object.Booster_state.return_booster_speed()
