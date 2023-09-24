import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
ans = 0


def bfs(x, y, c, visit):
    global ans
    q = deque()
    visit[x][y] = 1
    co = 0
    q.append((x, y))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    flag = 0
    while q:
        a1, a2 = q.popleft()
        co += 1
        for i in range(4):
            zx = a1 + dx[i]
            zy = a2 + dy[i]
            if zx == -1 or zx == n or zy == -1 or zy == m:
                flag = 1
            if 0 <= zx < n and 0 <= zy < m and visit[zx][zy] == 0 and graph[zx][zy] <= c:
                visit[zx][zy] = 1
                q.append((zx, zy))
    if flag == 0:
        ans += co


for i in range(1, 9):
    visit = [[0] * (m) for _ in range(n)]
    for j in range(n):
        for k in range(m):
            if visit[j][k] == 0 and graph[j][k] <= i:
                bfs(j, k, i, visit)

print(ans)