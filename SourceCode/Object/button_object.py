from pico2d import draw_rectangle, load_image, load_wav, load_font

from SourceCode.Etc import game_speed, game_world, global_variable
from SourceCode.Object.magnet_object import Magnet_state


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
        draw_rectangle(*self.get_hit_box())

    def get_hit_box(self):
        return self.x - self.w / 2, self.y - self.h / 2, self.x + self.w / 2, self.y + self.h / 2

    def handle_collision(self, group, other):
        pass

class SelectUpButtonObject:
    image = []
    type = 'Button'
    sound = None

    def __init__(self, x, y, command, character_num):
        self.x, self.y = x, y
        self.character_num = character_num
        self.command = command
        self.index = global_variable.character_select[character_num]
        self.color = (0, 0, 0)

        if not SelectUpButtonObject.image:
            SelectUpButtonObject.image.append(load_image('.//img//UI//lock_button.png'))
            SelectUpButtonObject.image.append(load_image('.//img//UI//select_2_button.png'))
            SelectUpButtonObject.image.append(load_image('.//img//UI//select_1_button.png'))

        if not SelectUpButtonObject.sound:
            SelectUpButtonObject.sound = load_wav('.//Sound//button_sound.ogg')
            SelectUpButtonObject.sound.set_volume(32)

        self.w = 150
        self.h = 50

    def __setstate__(self, state):
        pass

    def update(self):
        self.index = global_variable.character_select[self.character_num]


    def draw(self):
        SelectUpButtonObject.image[self.index].draw(self.x, self.y, self.w, self.h)
        draw_rectangle(*self.get_hit_box())

    def get_hit_box(self):
        return self.x - self.w / 2, self.y - self.h / 2, self.x + self.w / 2, self.y + self.h / 2

    def handle_collision(self, group, other):
        pass