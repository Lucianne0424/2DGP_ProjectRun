import os

from pico2d import load_image


def image_load(path, file_name):
    os.chdir(path)
    image = load_image(file_name)
    os.chdir("..//..")  # 원래 경로로 돌아오기
    return image
