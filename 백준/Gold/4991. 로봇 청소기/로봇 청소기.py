import sys
from collections import deque


def bfs(x, y, graph, dirty, n, m):
    visit = [[[0] * (1 << 10) for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((x, y, 0))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x1, y1, count = q.popleft()

        if count == (1 << len(dirty)) - 1:
            return visit[x1][y1][count]
        for i in range(4):
            zx = x1 + dx[i]
            zy = y1 + dy[i]
            if 0 <= zx < n and 0 <= zy < m:
                if graph[zx][zy] != "x":
                    if graph[zx][zy] == "*" :
                        nex = count | (1 << dirty.index((zx, zy)))
                        if visit[zx][zy][nex]==0:
                            visit[zx][zy][nex] = visit[x1][y1][count] + 1
                            q.append((zx, zy, nex))

                    else:
                        if visit[zx][zy][count] == 0:
                            visit[zx][zy][count] = visit[x1][y1][count] + 1
                            q.append((zx, zy, count))
    return -1


while 1:
    a2, a1 = map(int, input().split())
    if a1 == 0 and a2 == 0:
        break
    graph = []
    dirty = []
    sx = -1
    sy = -1
    for i in range(a1):
        e = list(map(str, input().rstrip()))
        graph.append(e)
        for j in range(a2):
            if e[j] == "*":
                dirty.append((i, j))
            elif e[j] == "o":
                sx = i
                sy = j

    t = bfs(sx, sy, graph, dirty, a1, a2)

    if t != -1:
        print(t)
    else:
        print(-1)