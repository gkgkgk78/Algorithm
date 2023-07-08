import sys
from collections import deque

input = sys.stdin.readline
graph = []
n, m = map(int, input().split())

sx, sy = map(int, input().split())
fx, fy = map(int, input().split())
sx -= 1
sy -= 1
fx -= 1
fy -= 1
ans = sys.maxsize
last = []
for i in range(n):
    e = list(map(int, input().split()))
    for j in range(m):
        if e[j] == 1:
            last.append((i, j))
    graph.append(e)


def bfs():
    global ans
    q = deque()
    visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    q.append((sx, sy, 0))
    visit[sx][sy][0] = 0
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    while q:
        x, y,  ff = q.popleft()
        if x == fx and y == fy:
            ans = min(ans, visit[x][y][ff])
            return

        for i in range(4):
            zx = x + dx[i]
            zy = y + dy[i]
            if 0 <= zx < n and 0 <= zy < m:
                if graph[zx][zy] == 0 and visit[zx][zy][ff]==0:
                    q.append((zx, zy,ff))
                    visit[zx][zy][ff] = visit[x][y][ff]+1
                else:
                    if ff == 0 and visit[zx][zy][ff]==0:
                        q.append((zx, zy, 1))
                        visit[zx][zy][1] = visit[x][y][0] + 1


bfs()

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)