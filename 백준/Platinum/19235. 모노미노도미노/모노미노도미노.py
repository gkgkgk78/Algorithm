import sys
from collections import deque

green = [[0] * (4) for _ in range(10)]
blue = [[0] * (10) for _ in range(4)]

n = int(input().rstrip())

ans = 0


def move_first1(graph, temp, count):
    # 이제 그룹 모두가 내려 갈 일만 남음
    t1 = []
    next = []

    for a1, a2 in temp:
        t1.append((a1, a2))
        graph[a1][a2] = 0
    while 1:
        nt = 0
        next = []
        for a1, a2 in t1:
            if 0 <= a1 < 4 and 0 <= a2 < 9 and graph[a1][a2+1] == 0:
                next.append((a1, a2+1))
            else:
                nt = 1
                break
        if nt == 1:
            break
        else:
            t1 = next
    for a1, a2 in t1:
        graph[a1][a2] = count

def move_first(graph, temp, count):
    # 이제 그룹 모두가 내려 갈 일만 남음
    t1 = []
    next = []

    for a1, a2 in temp:
        t1.append((a1, a2))
        graph[a1][a2] = 0
    while 1:
        nt = 0
        next = []
        for a1, a2 in t1:
            if 0 <= a1 < 9 and 0 <= a2 < 4 and graph[a1 + 1][a2] == 0:
                next.append((a1 + 1, a2))
            else:
                nt = 1
                break
        if nt == 1:
            break
        else:
            t1 = next
    for a1, a2 in t1:
        graph[a1][a2] = count

def move_tile(a1, a2, a3, count):
    # 이제 초록색 파란색 움직여야 함
    temp = [(a2, a3)]
    if a1 == 2:
        temp.append((a2, a3 + 1))
    elif a1 == 3:
        temp.append((a2 + 1, a3))
    move_first(green, temp, count)
    move_first1(blue, temp, count)


def move_down(graph, i, j):
    # 이제 같은 얘들 찾아 보도록 하자
    # 통째로 옮겨야 한다
    q = deque()
    visit = [[0] * (4) for _ in range(10)]
    visit[i][j] = 1
    color = graph[i][j]
    q.append((i, j))
    temp = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        a1, a2 = q.popleft()
        temp.append((a1, a2))
        for i in range(4):
            zx = dx[i] + a1
            zy = dy[i] + a2
            if 0 <= zx < 10 and 0 <= zy < 4 and visit[zx][zy] == 0 and graph[zx][zy] == color:
                visit[zx][zy] = 1
                q.append((zx, zy))

    # 이제 같은 집합 모두 찾음
    move_first(graph, temp, color)

def move_down1(graph, i, j):
    # 이제 같은 얘들 찾아 보도록 하자
    # 통째로 옮겨야 한다
    q = deque()
    visit = [[0] * (10) for _ in range(4)]
    visit[i][j] = 1
    color = graph[i][j]
    q.append((i, j))
    temp = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        a1, a2 = q.popleft()
        temp.append((a1, a2))
        for i in range(4):
            zx = dx[i] + a1
            zy = dy[i] + a2
            if 0 <= zx < 4 and 0 <= zy < 10 and visit[zx][zy] == 0 and graph[zx][zy] == color:
                visit[zx][zy] = 1
                q.append((zx, zy))

    # 이제 같은 집합 모두 찾음
    move_first1(graph, temp, color)

def down(graph, row):
    # 이제 행을 거슬러 올라 가면서 내리면 된다

    for i in range(row, 3, -1):
        for j in range(4):
            if graph[i][j] != 0:
                move_down(graph, i, j)


def move_total(graph, ne):
    for i in range(8, 3, -1):
        # 이제 행마다 움직 여야함
        # 어차피 통째로 움직 일거라 상관이 없음
        for j in range(4):
            if graph[i][j] != 0:
                graph[i+ne][j]=graph[i][j]
                graph[i][j]=0

def move_total1(graph, ne):
    for i in range(8, 3, -1):
        # 이제 행마다 움직 여야함
        # 어차피 통째로 움직 일거라 상관이 없음
        for j in range(4):
            if graph[j][i] != 0:
                graph[j][i+ne] = graph[j][i]
                graph[j][i] = 0


def check_row(graph):
    # 행 가득 차있다면 제거 후 내려 줘야 함
    global ans
    while 1:
        cou = 0
        fin = 0
        for i in range(9, 3, -1):
            cou = 0
            for j in range(4):
                if graph[i][j] != 0:
                    cou += 1
            if cou == 4:
                for j in range(4):
                    graph[i][j] = 0
                fin += 1
                ans += 1
        if fin != 0:
            down(graph,8)

        if fin == 0:
            break
    # 이제 연한색 부분에 있는거 제거 하면 됨
    ne = 0
    for i in range(4, 6):
        for j in range(4):
            if graph[i][j] != 0:
                ne += 1
                break
    x = 9
    for i in range(ne):
        for j in range(4):
            graph[x][j] = 0
        x -= 1

    # 이제 모두 제거를 하였으니 움직 이도록 하자.
    if ne != 0:
        move_total(graph, ne)

def down1(graph, col):
    # 이제 열을 거슬러 올라 가면서 내리면 된다
    for i in range(col, 3, -1):
        for j in range(4):
            if graph[j][i] != 0:
                move_down1(graph, j, i)

def check_row1(graph):
    # 행 가득 차있다면 제거 후 내려 줘야 함
    global ans
    while 1:
        cou = 0
        fin = 0
        for i in range(9, 3, -1):
            cou = 0
            for j in range(4):
                if graph[j][i] != 0:
                    cou += 1
            if cou == 4:
                for j in range(4):
                    graph[j][i] = 0
                fin += 1
                ans += 1
        if fin != 0:
            down1(graph, 8)

        if fin == 0:
            break
    # 이제 연한색 부분에 있는거 제거 하면 됨
    ne = 0
    for i in range(4, 6):
        for j in range(4):
            if graph[j][i] != 0:
                ne += 1
                break
    x = 9
    for i in range(ne):
        for j in range(4):
            graph[j][x] = 0
        x -= 1

    # 이제 모두 제거를 하였으니 움직 이도록 하자.
    if ne != 0:
        move_total1(graph, ne)

for l in range(1, n + 1):
    a1, a2, a3 = map(int, input().split())
    # 다른 블록 만나기 전까지 블록 이동
    if l == 5:
        l = 5
    move_tile(a1, a2, a3, l)

    # 이제 행 또는 열이 가득 찼다면 해당 행 제거 후 이동을 계속 함
    check_row(green)
    check_row1(blue)

print(ans)
gr = 0
bl = 0
for i in range(4, 10):
    for j in range(4):
        if green[i][j] != 0:
            gr += 1
for i in range(4):
    for j in range(10):
        if blue[i][j] != 0:
            bl += 1
print(gr + bl)