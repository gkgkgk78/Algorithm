import sys
from collections import deque
import heapq

input = sys.stdin.readline

graph = [[0] * (501) for _ in range(501)]
visit = [[-1] * (501) for _ in range(501)]

can = int(input().rstrip())
for _ in range(can):
    x1, y1, x2, y2 = map(int, input().split())
    a1, a2, a3, a4 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    for i in range(a1, a3 + 1):
        for j in range(a2, a4 + 1):
            graph[i][j] = -1
death = int(input().rstrip())
for _ in range(death):
    x1, y1, x2, y2 = map(int, input().split())
    a1, a2, a3, a4 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    for i in range(a1, a3 + 1):
        for j in range(a2, a4 + 1):
            graph[i][j] = -2


def bfs():
    q = deque()
    visit[0][0] = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            zx = dx[i] + x
            zy = dy[i] + y
            if 0 <= zx <= 500 and 0 <= zy <= 500:
                if graph[zx][zy] != -2:
                    if graph[zx][zy] == 0:
                        if visit[zx][zy] == -1:
                            visit[zx][zy] = visit[x][y]
                            q.append((zx, zy))
                        else:
                            if visit[zx][zy] > visit[x][y]:
                                visit[zx][zy] = visit[x][y]
                                q.append((zx, zy))
                    else:
                        if visit[zx][zy] == -1:
                            visit[zx][zy] = visit[x][y] + 1
                            q.append((zx, zy))
                        else:
                            if visit[zx][zy] > visit[x][y] + 1:
                                visit[zx][zy] = visit[x][y] + 1
                                q.append((zx, zy))
    return visit[500][500]

answer = bfs()
print(answer)