canvasSIZE = (1280, 720)

coin = 500000
score = 0
stage = 1
hpLevel = 1
playerCoin = 0

mission = 0
mission_result = 0

character_select = {'Girl': 2, 'temp1': 0, 'temp2': 0} # 0이면 사용 불가 상태, 1이면 사용 가능 상태, 2이면 선택된 상태

levelMax = {
    'Point_level': 17 + 1,
    'Hp_level': 20 + 1
}
price = {
    'Point_level': [i * 100 for i in range(levelMax['Point_level'])],
    'Hp_level': [i * 100 for i in range(levelMax['Hp_level'])]
}
depth = {'BackGround': 0, 'Tile': 1, 'Hurdle': 2, 'Player': 3, 'Item': 4, 'UI': 5, 'Button': 6}
