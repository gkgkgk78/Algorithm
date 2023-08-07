import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
wall = []
for i in range(n):
    e = list(map(int, input().split()))
    for j in range(m):
        if e[j] == 1:
            wall.append((i, j))

h, w, sr, sc, fr, fc = map(int, input().split())
sr -= 1
sc -= 1
fr -= 1
fc -= 1


def bfs():
    visit = [[0] * (m) for _ in range(n)]
    visit[sr][sc] = 1
    q = deque()
    q.append((sr, sc, 0))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        a1, a2, a3 = q.popleft()
        if a1 == fr and a2 == fc:
            return a3
        for i in range(4):
            zx = a1 + dx[i]
            zy = a2 + dy[i]
            if 0 <= zx < n and 0 <= zy < m and visit[zx][zy] == 0 and zx + h <= n and zy + w <= m:
                # 벽이 있는지 없는지 판단 해아함

                cc = 0
                for z1, z2 in wall:
                    if zx <= z1 < zx + h and zy <= z2 < zy + w:
                        cc = 1
                        break
                if cc == 0:
                    visit[zx][zy] = 1
                    q.append((zx, zy, a3 + 1))
    return -1

zz = bfs()
if zz != -1:
    print(zz)
else:
    print(-1)