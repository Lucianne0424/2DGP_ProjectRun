from pico2d import load_image, load_wav, load_font

from SourceCode.Etc import global_variable
from SourceCode.Object import point_object


class ButtonObject:
    image = None
    type = 'Button'
    sound = None
    font = None

    def __init__(self, x, y, command, message, pos):
        self.x, self.y = x, y
        self.message = message
        self.pos = pos
        self.color = (0,0,0)
        self.command = command

        if ButtonObject.font == None:
            ButtonObject.font = load_font('.//DataFile//KORAIL2007.ttf', 30)

        if ButtonObject.image == None:
            ButtonObject.image = load_image('.//img//UI//button1.png')

        if not ButtonObject.sound:
            ButtonObject.sound = load_wav('.//Sound//button_sound.ogg')
            ButtonObject.sound.set_volume(32)

        self.w = 200
        self.h = ButtonObject.image.h

    def __setstate__(self, state):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, self.w, self.h)
        self.font.draw(self.x - self.pos, self.y, self.message, self.color)

    def get_hit_box(self):
        return self.x - self.w / 2, self.y - self.h / 2, self.x + self.w / 2, self.y + self.h / 2

    def handle_collision(self, group, other):
        pass

class SelectButtonObject:
    image = []
    type = 'Button'
    sound = None

    def __init__(self, x, y, command, character_num):
        self.x, self.y = x, y
        self.character_num = character_num
        self.command = command
        self.index = global_variable.character_select[character_num]
        self.color = (0, 0, 0)

        if not SelectButtonObject.image:
            SelectButtonObject.image.append(load_image('.//img//UI//lock_button.png'))
            SelectButtonObject.image.append(load_image('.//img//UI//select_2_button.png'))
            SelectButtonObject.image.append(load_image('.//img//UI//select_1_button.png'))

        if not SelectButtonObject.sound:
            SelectButtonObject.sound = load_wav('.//Sound//button_sound.ogg')
            SelectButtonObject.sound.set_volume(32)

        self.w = 150
        self.h = 50

    def __setstate__(self, state):
        pass

    def update(self):
        self.index = global_variable.character_select[self.character_num]


    def draw(self):
        SelectButtonObject.image[self.index].draw(self.x, self.y, self.w, self.h)

    def get_hit_box(self):
        return self.x - self.w / 2, self.y - self.h / 2, self.x + self.w / 2, self.y + self.h / 2

    def handle_collision(self, group, other):
        pass


class LevelUpButtonObject:
        image = []
        type = 'Button'
        sound = None

        def __init__(self, x, y, command, level_type):
            self.x, self.y = x, y
            self.level_type = level_type
            self.command = command
            self.index = 1

            self.color = (0, 0, 0)

            if not LevelUpButtonObject.image:
                LevelUpButtonObject.image.append(load_image('.//img//UI//store_button_max.png'))
                LevelUpButtonObject.image.append(load_image('.//img//UI//store_button_level_up_off.png'))
                LevelUpButtonObject.image.append(load_image('.//img//UI//store_button_level_up_on.png'))

            if not LevelUpButtonObject.sound:
                LevelUpButtonObject.sound = load_wav('.//Sound//button_sound.ogg')
                LevelUpButtonObject.sound.set_volume(32)

            self.w = 150
            self.h = 50

        def __setstate__(self, state):
            pass

        def update(self):
            if self.level_type == 'Point_level':
                if point_object.point_object_level >= global_variable.levelMax[self.level_type] - 1:
                    self.index = 0
                elif global_variable.price[self.level_type][point_object.point_object_level] <= global_variable.coin:
                    self.index = 2
                else:
                    self.index = 1

            elif self.level_type == 'Hp_level':
                if global_variable.hpLevel >= global_variable.levelMax[self.level_type] - 1:
                    self.index = 0
                elif global_variable.price[self.level_type][global_variable.hpLevel] <= global_variable.coin:
                    self.index = 2
                else:
                    self.index = 1


        def draw(self):
            LevelUpButtonObject.image[self.index].draw(self.x, self.y, self.w, self.h)

        def get_hit_box(self):
            return self.x - self.w / 2, self.y - self.h / 2, self.x + self.w / 2, self.y + self.h / 2

        def handle_collision(self, group, other):
            pass