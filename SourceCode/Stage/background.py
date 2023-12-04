from pico2d import load_image

from SourceCode.Etc import game_world, game_speed, global_variable
from SourceCode.Etc.global_variable import depth


def add_back_ground():
    if game_world.objects[depth['BackGround']][0].x <= -1280:
        game_world.remove_object(game_world.objects[depth['BackGround']][0])
        background = BackGround(game_world.objects[depth['BackGround']][0].x + 1280)
        game_world.add_object(background, depth['BackGround'])


class BackGround:
    image = None

    def __init__(self, x):
        self.x = x
        if BackGround.image == None:
            BackGround.image = load_image('.//img//BackGround//testBG.png')

    def update(self):
        self.x -= game_speed.Game_Speed.return_spped(game_speed.BACKGROUND_SPEED_PPS)
        add_back_ground()

    def draw(self):
        self.image.draw_to_origin(self.x, 0, global_variable.canvasSIZE[0], global_variable.canvasSIZE[1])
