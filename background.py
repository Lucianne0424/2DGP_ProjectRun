import game_framework
import game_world
from game_world import canvasSIZE, remove_object, add_object
from global_variable import BACKGROUND_SPEED_PPS, Booster_state
from image_load import image_load






class BackGround:
    image = None
    def __init__(self, x):
        self.x = x
        if BackGround.image == None:
            BackGround.image = image_load('.//img//BackGround', 'testBG.png')

    def update(self):
        self.x -= (BACKGROUND_SPEED_PPS * game_framework.frame_time) * game_world.game_speed * Booster_state.return_booster_speed()
        if self.x <= -canvasSIZE[0]:
            remove_object(self)
            background = BackGround(canvasSIZE[0])
            add_object(background, 0)


    def draw(self):
        self.image.draw_to_origin(self.x, 0, canvasSIZE[0],canvasSIZE[1])
