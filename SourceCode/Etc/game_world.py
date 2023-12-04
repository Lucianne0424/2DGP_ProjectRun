# 게임 월드 모듈
import pickle

from pico2d import draw_rectangle

objects = [[] for _ in range(8)]  # 레이어 구별
# 충돌 그룹 정보를 dict로 표현
collision_pairs = {}


# 충돌처리를 위한 객채들 그룹화
def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'New group {group} added...')
        collision_pairs[group] = [[], []]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


# 그훕화 한 객체 삭제
def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


# 게임 월드에 객체 담기
def add_object(o, depth=0):
    objects[depth].append(o)


def add_objects(ol, depth=0):
    objects[depth] += ol


# 게임 월드 객체들을 모두 업데이트
def updata():
    for layer in objects:
        for o in layer:
            o.update()


# 게임 월드 객체들을 모두 그리기
def render():
    for layer in objects:
        for o in layer:
            o.draw()

def render_hit_box():
    for layer in objects:
        for o in layer:
            draw_rectangle(*o.get_hit_box())


# 객체 삭제
def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return

    raise ValueError('Remove Error')


# 객체 모두 삭제
def clear():
    for layer in objects:
        layer.clear()

    collision_pairs.clear()


# 충돌처리
def collide(a, b):
    la, ba, ra, ta = a.get_hit_box()
    lb, bb, rb, tb = b.get_hit_box()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True


def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)


def save_world(path):
    with open(path, "wb") as f:
        pickle.dump(objects, f)


def load_world(path):
    with open(path, "rb") as f:
        data = pickle.load(f)

    for i in data:
        i.sort(key=lambda c: c.x)

    return data
