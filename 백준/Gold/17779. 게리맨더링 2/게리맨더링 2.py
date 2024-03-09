import sys
#1시간 딱 걸림

input = sys.stdin.readline
n = int(input().rstrip())
graph = [[0] * (n + 2)]
for _ in range(n):
    e = list(map(int, input().split()))
    e = [0] + e + [0]
    graph.append(e)
graph.append([0] * (n + 2))
# 이제 시뮬레이션을 돌리면서 인구수가 가장 많은 선거구와
# 가장 적은 선거구의 차이를 구하면 된다
answer = sys.maxsize


def draw(x, y, dx, dy, lx, ly, check):
    while 1:
        check[x][y] = 5

        x += dx
        y += dy
        if x == lx and y == ly:
            check[x][y] = 5
            break


def make(x, y, d1, d2):
    global answer
    check = [[0] * (n + 2) for _ in range(n + 2)]
    temp = [0] * (6)
    # 경계선 칠하기
    # 1
    draw(x, y, 1, -1, x + d1, y - d1, check)

    # 2
    draw(x, y, 1, 1, x + d2, y + d2, check)
    # 3
    draw(x + d1, y - d1, 1, 1, x + d1 + d2, y - d1 + d2, check)
    # 4
    draw(x + d2, y + d2, 1, -1, x + d1 + d2, y - d1 + d2, check)

    # 가장 큰 구역 , 가장 작은 구역 찾기
    # 1번 선거구
    for i in range(1, x + d1):
        for j in range(1, y + 1):
            if check[i][j] == 5:
                break
            check[i][j] = 1
    # 2번 선거구
    for i in range(1, x + d2 + 1):
        for j in range(n, y, -1):
            if check[i][j] != 0:
                break
            check[i][j] = 2
    # 3번 선거구
    for i in range(x + d1, n + 1):
        for j in range(1, y - d1 + d2):
            if check[i][j] != 0:
                break
            check[i][j] = 3
    # 4번 선거구
    for i in range(x + d1, n + 1):
        for j in range(n, y - d1 + d2 - 1, -1):
            if check[i][j] != 0:
                break
            check[i][j] = 4
    # print("그래프")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if 1 <= check[i][j] <= 4:
                temp[check[i][j]] += graph[i][j]
            else:
                temp[5] += graph[i][j]
    mi = sys.maxsize
    ma = -sys.maxsize
    for i in range(1, 6):
        mi = min(mi, temp[i])
        ma = max(ma, temp[i])
    answer = min(answer, ma - mi)


make(4, 3, 1, 1)


def game(x, y):
    # d1,d2 에 따라 달라지는 것을 확인해 보자
    for d1 in range(1, n + 1):
        for d2 in range(1, n + 1):
            if x + d1 + d2 <= n and y + d2 <= n:
                # 이제 탐색 가능한 거임
                make(x, y, d1, d2)


for i in range(1, n + 1):
    for j in range(1, n + 1):
        game(i, j)
print(answer)