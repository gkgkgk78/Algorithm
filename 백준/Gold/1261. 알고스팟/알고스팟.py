import sys
from collections import deque
import heapq

input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
for _ in range(n):
    e = list(map(int, input().rstrip()))
    graph.append(e)
visit = [[sys.maxsize] * (m) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append((0, 0))
visit[0][0] = 0

while q:
    a1, a2 = q.popleft()
    if a1 == n - 1 and a2 == m - 1:
        continue
    for i in range(4):
        zx = dx[i] + a1
        zy = dy[i] + a2
        if 0 <= zx < n and 0 <= zy < m:
            if graph[zx][zy] == 0:
                if visit[a1][a2] < visit[zx][zy]:
                    visit[zx][zy] = visit[a1][a2]
                    q.appendleft((zx, zy))
            else:
                if visit[a1][a2] + 1 < visit[zx][zy]:
                    visit[zx][zy] = visit[a1][a2] + 1
                    q.append((zx, zy))

print(visit[n - 1][m - 1])