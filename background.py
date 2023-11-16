import game_framework
import game_world
from booster_object import Booster_state
from game_world import canvasSIZE, remove_object, add_object
from global_variable import BACKGROUND_SPEED_PPS
from image_load import image_load

def add_back_ground():
    if game_world.objects[0][0].x <= -1280:
        game_world.remove_object(game_world.objects[0][0])
        background = BackGround(game_world.objects[0][0].x + 1280)
        game_world.add_object(background, 0)

class BackGround:
    image = None

    def __init__(self, x):
        self.x = x
        if BackGround.image == None:
            BackGround.image = image_load('.//img//BackGround', 'testBG.png')

    def update(self):
        self.x -= (BACKGROUND_SPEED_PPS * game_framework.frame_time) * game_world.game_speed * Booster_state.return_booster_speed()
        add_back_ground()

    def draw(self):
        self.image.draw_to_origin(self.x, 0, canvasSIZE[0], canvasSIZE[1])
