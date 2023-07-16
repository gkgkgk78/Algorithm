import sys
from collections import deque

input = sys.stdin.readline

r, c, k = map(int, input().split())
graph = []
hot = []
test = []
wall = [[[] for _ in range(c)] for _ in range(r)]
e = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for i in range(r):
    e = list(map(int, input().split()))
    for j in range(c):
        if e[j] == 5:
            test.append((i, j))
            e[j] = 0
        elif 1 <= e[j] <= 4:
            hot.append((i, j, e[j] - 1))  # 좌표, 방향
            e[j] = 0
    graph.append(e)
z = int(input().rstrip())
for _ in range(z):
    x, y, c1 = map(int, input().split())
    x -= 1
    y -= 1
    x1, y1 = x, y
    if c1 == 0:
        x1 = x - 1
    else:
        y1 = y + 1

    if x == 5 and y == 4:
        x = 5
    wall[x][y].append([x1, y1])
    wall[x1][y1].append([x, y])


# 이제 방향을 주면 세가지 방향에 대해 인덱스를 넘겨주는 작업을 해야함
def go_next(x, y, dir):
    if dir == 0:
        return [[(x, y), (x - 1, y), (x - 1, y + 1)], [(x, y), (x, y + 1)], [(x, y), (x + 1, y), (x + 1, y + 1)]]
    elif dir == 1:
        return [[(x, y), (x - 1, y), (x - 1, y - 1)], [(x, y), (x, y - 1)], [(x, y), (x + 1, y), (x + 1, y - 1)]]
    elif dir == 2:
        return [[(x, y), (x, y - 1), (x - 1, y - 1)], [(x, y), (x - 1, y)], [(x, y), (x, y + 1), (x - 1, y + 1)]]
    elif dir == 3:
        return [[(x, y), (x, y - 1), (x + 1, y - 1)], [(x, y), (x + 1, y)], [(x, y), (x, y + 1), (x + 1, y + 1)]]


choco = 0


def move(x, y, dir, now, visit, temp_graph):
    q = deque()
    x += dx[dir]
    y += dy[dir]
    visit[x][y] = now
    q.append((x, y, 5))
    temp_graph[x][y] += 5
    while q:
        x1, y1, cc = q.popleft()
        if cc == 1:
            continue
        # 이제 나왔으니 움직여 줘야 함
        next = go_next(x1, y1, dir)
        for i in next:  # 이제 가능하면 움직이게 될거임
            lx, ly = i[-1]
            # 우선 한번 거르기 위한 부분
            if (0 <= lx < r and 0 <= ly < c and visit[lx][ly] != now):
                for j in range(len(i) - 1):
                    bx, by = i[j][0], i[j][1]
                    cx, cy = i[j + 1][0], i[j + 1][1]
                    if [cx, cy] not in wall[bx][by] and [bx, by] not in wall[cx][cy]:
                        if j == len(i) - 2:  # 이제 끝에 와버림
                            visit[lx][ly] = now
                            temp_graph[lx][ly] += cc - 1
                            q.append((lx, ly, cc - 1))
                    else:
                        break


def control(graph, temp_graph):
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                for z in range(4):
                    zx = dx[z] + i
                    zy = dy[z] + j
                    if 0 <= zx < r and 0 <= zy < c:
                        if graph[i][j] > graph[zx][zy]:
                            if [zx, zy] not in wall[i][j] and [i, j] not in wall[zx][zy]:
                                ne = (graph[i][j] - graph[zx][zy]) // 4
                                temp_graph[i][j] -= ne
                                temp_graph[zx][zy] += ne


def decrease(graph):
    for i in range(1, c - 1):  # 가로
        if graph[0][i] > 0:
            graph[0][i] -= 1
    for i in range(1, r - 1):  # 왼쪽 세로
        if graph[i][0] > 0:
            graph[i][0] -= 1
    for i in range(1, r - 1):  # 오른쪽 세로
        if graph[i][c - 1] > 0:
            graph[i][c - 1] -= 1
    for i in range(1, c - 1):  # 가로
        if graph[r - 1][i] > 0:
            graph[r - 1][i] -= 1
    tx = [0, 0, r - 1, r - 1]
    ty = [0, c - 1, 0, c - 1]
    for i in range(4):
        if graph[tx[i]][ty[i]] > 0:
            graph[tx[i]][ty[i]] -= 1


def fin(graph):
    for a1, a2 in test:
        if graph[a1][a2] < k:
            return 0
    return 1


while choco <= 100:

    visit = [[0] * (c) for _ in range(r)]
    temp_graph = [[0] * (c) for _ in range(r)]
    for i in range(len(hot)):
        x, y, dir = hot[i]
        move(x, y, dir, i + 1, visit, temp_graph)
    for i in range(r):
        for j in range(c):
            graph[i][j] += temp_graph[i][j]
    temp_graph = [[0] * (c) for _ in range(r)]
    control(graph, temp_graph)
    for i in range(r):
        for j in range(c):
            graph[i][j] += temp_graph[i][j]

    decrease(graph)
    choco += 1

    zz = fin(graph)
    if zz == 1:
        break

if choco > 100:
    print(101)
else:
    print(choco)