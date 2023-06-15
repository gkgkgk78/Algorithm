import sys
from collections import deque

input = sys.stdin.readline


def bfs(l, r, c, sz, sx, sy, graph):
    q = deque()
    visit = [[[0] * (c) for _ in range(r)] for _ in range(l)]
    t = visit[0]
    visit[sz][sx][sy] = 1
    q.append((sz, sx, sy, 0))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    dz = [-1, 1]

    while q:
        tz, tx, ty, value = q.popleft()

        for i in range(4):
            zx = dx[i] + tx
            zy = dy[i] + ty
            if 0 <= zx < r and 0 <= zy < c and visit[tz][zx][zy] == 0:
                if graph[tz][zx][zy] == "#":
                    continue
                if graph[tz][zx][zy] == "E":
                    return value + 1
                visit[tz][zx][zy] = 1
                q.append((tz, zx, zy, value + 1))

        for j in range(2):
            zz = dz[j] + tz
            if 0 <= zz < l and visit[zz][tx][ty] == 0:
                if graph[zz][tx][ty] == "#":
                    continue
                if graph[zz][tx][ty] == "E":
                    return value + 1
                visit[zz][tx][ty] = 1
                q.append((zz, tx, ty, value + 1))

    return -1


while 1:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break

    graph = []
    sz = -1
    sx = -1
    sy = -1
    i = 0
    for l1 in range(l):
        temp = []
        for i in range(r):
            e = list(map(str, input().rstrip()))
            for j in range(c):
                if e[j] == "S":
                    sz = l1
                    sx = i
                    sy = j
            temp.append(e)
        graph.append(temp)
        input().split()

    ti = bfs(l, r, c, sz, sx, sy, graph)
    if ti == -1:
        print("Trapped!")
    else:
        print("Escaped in " + str(ti) + " minute(s).")