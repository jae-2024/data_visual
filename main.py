import matplotlib.pyplot as plt
import numpy as np
import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

points = [(x,y) for x in range(401) for y in range(401)]

select = np.random.choice(len(points), 200, replace=False)
selected_points = np.array([points[i] for i in select])

x = selected_points[:, 0]
y = selected_points[:, 1]

color = ['red']*100 + ['blue']*100
np.random.shuffle(color)

red_spot = []
blue_spot = []
for i in range(len(color)):
    if color[i] == 'red':
        red_spot.append(i)
    else:
        blue_spot.append(i)

for _ in range(100):
    #100개의 빨간색, 파란색 점을 리스트에 저장
    red_points = selected_points[red_spot]
    blue_points = selected_points[blue_spot]

    avg_redx = np.mean(red_points[:, 0])
    avg_redy = np.mean(red_points[:, 1])

    avg_bluex = np.mean(blue_points[:, 0])
    avg_bluey = np.mean(blue_points[:, 1])

    #어느 평균값의 점에 더 가까운지 계산 (색이 지정된걸로하면 색을 다시 바꿔야 하니 기존에 처음 색이 지정되기 전의 점의 리스트로 하기)
    # 1.처음 선택된 점들의 리스트를 불러와 하나씩 평균값과 비교
    # 2.더 가까운 평균값의 색으로 변경
    new_red_spot = []
    new_blue_spot = []
    new_color = []
    for i in range(len(selected_points)):
        point = selected_points[i]
        a = calculate_distance(point[0], point[1], avg_redx, avg_redy)
        b = calculate_distance(point[0], point[1], avg_bluex, avg_bluey)
        if a < b:
            new_color.append('red')
            new_red_spot.append(i)
        else:
            new_color.append('blue')
            new_blue_spot.append(i)
    if color == new_color:
        break
    color = new_color
    red_spot = np.array(new_red_spot)
    blue_spot = np.array(new_blue_spot)
    # 평균값을 점으로 찍음(확인차 짠 코드)
    plt.scatter(avg_redx, avg_redy, c='black')
    plt.scatter(avg_bluex, avg_bluey, c='yellow')
    plt.scatter(x, y, c=new_color)
    plt.show()

plt.xlim(0, 400)
plt.ylim(0, 400)





# 1. 2차원 좌표값을 200개 생성 x,y : 0~400사이의 정수 (좌표값은 중복x) ok
# 2. 임의로 100개씩 두그룹 빨강/파랑으로 지정 ok
# 3. 평균값을 2개 구하기 ok
# 4. 한 점이 두개의 평균값 중 더 가까운 것의 색으로 바뀜 ok
# 5. 2번과정을 전 평균값과 같을시에 종료되게 짜기 => 기존의 색 배열이 바뀐 색 배열과 같을 때 종료하는걸로 바꿈