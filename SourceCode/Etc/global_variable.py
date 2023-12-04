canvasSIZE = (1280, 720)

coin = 0
score = 0
stage = 0
hpLevel = 1
playerCoin = 0

missionList = [
    # 1스테이지
    ('장애물 파괴 하기', 50),
    # 2스테이지
    ('코인 획득 하기', 1800),
    # 3스테이지
    ('포인트 오브젝트 먹기', 240)
]

mission = 0 # 미션 내용
mission_result = 0 # 미션 결과

character_select = {'Girl': 2, 'Cow': 0, 'Magician': 0} # 0이면 사용 불가 상태, 1이면 사용 가능 상태, 2이면 선택된 상태

levelMax = {
    'Point_level': 17 + 1,
    'Hp_level': 20 + 1
}
price = {
    'Point_level': [i * 100 for i in range(levelMax['Point_level'])],
    'Hp_level': [i * 100 for i in range(levelMax['Hp_level'])]
}
depth = {'BackGround': 0, 'Tile': 1, 'Gate': 2, 'Hurdle': 3, 'Player': 4, 'Item': 5, 'UI': 6, 'Button': 7}
