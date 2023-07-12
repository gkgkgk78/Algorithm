import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())

visit = [[[0] * (2) for _ in range(n)] for _ in range(n)]
start = []
finish = []
graph = []
for i in range(n):
    e = list(map(str, input().rstrip()))
    for j in range(n):
        if e[j] == "B":
            start.append((i, j))
            e[j] = "0"
        elif e[j] == "E":
            finish.append((i, j))
            e[j] = "0"
    graph.append(e)

sx, sy, sdir = start[1][0], start[1][1], -1
fx, fy, fdir = finish[1][0], finish[1][1], -1

if start[0][0] == start[1][0]:
    sdir = 0  # 평행
else:
    sdir = 1
if finish[0][0] == finish[1][0]:
    fdir = 0  # 평행
else:
    fdir = 1


def possible(x, y, go, dir):
    if go == "U":
        x -= 1
    elif go == "D":
        x += 1
    elif go == "L":
        y -= 1
    elif go == "R":
        y += 1

    if go == "T":
        dir1 = (dir + 1) % 2
        if visit[x][y][dir1] == 1 or graph[x][y] == "1":
            return 0
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        zx = x
        zy = y
        for i in range(8):
            zx = x + dx[i]
            zy = y + dy[i]
            if 0 <= zx < n and 0 <= zy < n and graph[zx][zy] == "0":
                continue
            else:
                return 0

        return 1

    else:
        # 가로인지 세로인지 에 따라 다르게 해야 한다
        if dir == 0:
            dz = [-1, 1]
            for i in range(2):
                zy = y + dz[i]
                if 0 <= x < n and 0 <= zy < n and graph[x][zy] == "0":
                    continue
                else:
                    return 0
        else:
            dz = [-1, 1]
            for i in range(2):
                zx = x + dz[i]
                if 0 <= zx < n and 0 <= y < n and graph[zx][y] == "0":
                    continue
                else:
                    return 0
        if visit[x][y][dir] == 1 or graph[x][y] == "1":
            return 0
        return 1


def che(x, y, go):
    if go == "U":
        x -= 1
    elif go == "D":
        x += 1
    elif go == "L":
        y -= 1
    elif go == "R":
        y += 1
    return x, y


def bfs():
    visit[sx][sy][sdir] = 1
    q = deque()
    q.append((sx, sy, sdir, 0))
    next = ["U", "D", "L", "R", "T"]
    aa = visit
    while q:

        x, y, dir, count = q.popleft()
        if x == fx and y == fy and dir == fdir:
            return count
        for i in next:
            g = possible(x, y, i, dir)
            if g == 1:
                if i != "T":
                    zx, zy = che(x, y, i)
                    visit[zx][zy][dir] = 1
                    q.append((zx, zy, dir, count + 1))
                else:
                    dir1 = (dir + 1) % 2
                    visit[x][y][dir1] = 1
                    q.append((x, y, dir1, count + 1))
    return 0

aa = bfs()
print(aa)