import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(str, input().rstrip())))
total = dict()
check = 0
last = []
first=dict()
for i in range(k):
    ee = str(input().rstrip())
    check = max(check, len(ee))
    last.append(ee)
    if ee[0]not in first:
        first[ee[0]]=1
    if ee not in total:
        total[ee] = 0


def dfs(x, y, now):
    global  check
    if now in total:
        total[now] += 1
    if len(now) > check:
        return

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    zx = x
    zy = y
    for i in range(len(dx)):
        zx = x + dx[i]
        zy = y + dy[i]

        if 0 <= zx < n and 0 <= zy < m:
            tt = now + graph[zx][zy]

            dfs(zx, zy, tt)
        else:
            if zx == -1:
                zx = n - 1
            if zx == n:
                zx = 0
            if zy == -1:
                zy = m - 1
            if zy == m:
                zy = 0
            tt = now + graph[zx][zy]
            dfs(zx, zy, tt)


for i in range(n):
    for j in range(m):
        if graph[i][j]in first:
            dfs(i, j, ""+graph[i][j])

for i in last:
    print(total[i])