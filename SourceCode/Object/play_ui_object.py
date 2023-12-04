from pico2d import load_image, load_font

from SourceCode.Etc import global_variable, game_world
from SourceCode.Etc.global_variable import depth
from SourceCode.Mode import play_mode
from SourceCode.Object import point_object


class Play_Ui_Object:
    def __init__(self):
        self.hp_bar = []
        self.hp_bar_w = []
        self.hp_bar_h = []
        self.hp_bar_pos_x, self.hp_bar_pos_y = 200, 680
        for i in range(3):
            self.hp_bar.append(load_image('.//img//UI//hp_bar_' + str(i) + '.png'))
            self.hp_bar_w.append(self.hp_bar[i].w)
            self.hp_bar_h.append(self.hp_bar[i].h)

        self.font = load_font('.//DataFile//KORAIL2007.TTF', 20)
        self.color = (255, 255, 255)

        self.coin_image = load_image('.//img//Coin//coin.png')
        game_world.add_object(point_object.UIPointObject(50, 610, 40, 40), depth['UI'])






    def __setstate__(self, state):
        pass

    def update(self):
        pass

    def draw(self):
        self.hp_bar[0].draw(self.hp_bar_pos_x, self.hp_bar_pos_y, self.hp_bar_w[0] * 2, self.hp_bar_h[0])
        self.hp = (self.hp_bar_w[2] * 2) * (play_mode.player.Hp / play_mode.player.MaxHp)
        self.hp_bar[2].draw_to_origin(self.hp_bar_pos_x- 138, self.hp_bar_pos_y - 17, self.hp , self.hp_bar_h[2])
        self.hp_bar[1].draw(self.hp_bar_pos_x - 153, self.hp_bar_pos_y, self.hp_bar_w[1] * 2, self.hp_bar_h[1])
        self.coin_image.draw(50, 550, 40, 40)

        self.font.draw(80, 610, ': ' + str(global_variable.score),self.color)
        self.font.draw(80, 550, ': ' + str(play_mode.player.coin), self.color)

        if global_variable.mission != False:
            self.font.draw(10, 490,global_variable.missionList[global_variable.stage - 1][0] + ': ' + str(global_variable.mission_result) + ' / ' + str(global_variable.mission), self.color)


    def get_hit_box(self):
        pass

    def handle_collision(self, group, other):
        pass
