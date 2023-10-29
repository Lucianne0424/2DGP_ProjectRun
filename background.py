from game_world import canvasSIZE, remove_object, add_object
from image_load import image_load


class BackGround:
    image = None
    def __init__(self, x):
        self.x = x
        if BackGround.image == None:
            BackGround.image = image_load('.//img//BackGround', 'testBG.png')

    def update(self):
        self.x -= 10
        if self.x < -canvasSIZE[0]:
            remove_object(self)
            add_object(BackGround(canvasSIZE[0] + 10),0)


    def draw(self):
        self.image.draw_to_origin(self.x, 0, canvasSIZE[0],canvasSIZE[1])
