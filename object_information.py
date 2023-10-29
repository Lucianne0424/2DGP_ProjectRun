stage = 1

stage1_point_object_pos_y = [1, 1, 1, 1, 1, 2, 3, 2, 1, 1, 2, 3, 4, 3, 2, 1] # 점수 오브젝트가 생성될 높이를 순서대로 저장한 배열

def setting_stage():
    if stage == 1:
        point_object_information = stage1_point_object_pos_y

    return point_object_information