# 게임 월드 모듈

canvasSIZE = (1280, 720)

world = [[], [], []]  # 레이어 구별


# 게임 월드에 객체 담기

def add_object(o, depth=0):
    world[depth].append(o)


# 게임 월드 객체들을 모두 업데이트
def updata():
    for layer in world:
        for o in layer:
            o.update()


# 게임 월드 객체들을 모두 그리기
def render():
    for layer in world:
        for o in layer:
            o.draw()


# 객체 삭제
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    raise ValueError('Remove Error')