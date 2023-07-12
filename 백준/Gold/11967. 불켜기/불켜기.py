import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(m):
    a1, a2, a3, a4 = map(int, input().split())
    graph[a1][a2].append([a3, a4])

# 1,1에서 시작 가느아
visit = [[0] * (m + 3)  for _ in range(n + 1)]
light = [[0] * (n + 1) for _ in range(n + 1)]


def bfs():
    q = deque()
    visit[1][1] = 1
    light[1][1] = 1
    count = 1
    q.append((1, 1))
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    total=[(1,1)]
    while q:
        a1, a2 = q.popleft()
        for i, j in graph[a1][a2]:
            if light[i][j] == 0:
                light[i][j] = 1
                count += 1
        for z1,z2 in total:
            for k in range(4):
                zx = z1 + dx[k]
                zy = z2 + dy[k]
                if 0 < zx <= n and 0 < zy <= n:
                    if light[zx][zy] == 1 and visit[zx][zy] == 0:
                        visit[zx][zy] = 1
                        q.append((zx, zy))
                        total.append((zx,zy))
    print(count)


bfs()