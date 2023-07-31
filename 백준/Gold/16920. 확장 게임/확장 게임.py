import sys
from collections import deque

input = sys.stdin.readline

n, m, p = map(int, input().split())
can_go = [0] + list(map(int, input().split()))
player = [[] for _ in range(p + 1)]

graph = []
for i in range(n):
    e = list(map(str, input().rstrip()))
    for j in range(m):
        if e[j] == "." or e[j] == "#":
            continue
        if 1 <= (int)(e[j]) <= 9:
            player[(int)(e[j])].append((i, j))
    graph.append(e)
visit = [[0] * (m) for _ in range(n)]


def bfs(i):
    q = deque()
    temp = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    tt = 0
    for a1, a2 in player[i]:
        visit[a1][a2] = 1
        q.append((a1, a2))
    for l in range(can_go[i]):
        ttt = deque()
        if len(q)==0:
            break
        while q:
            a1, a2 = q.popleft()
            g1 = graph
            for k in range(4):
                zx = a1
                zy = a2
                zx += dx[k]
                zy += dy[k]
                if 0 <= zx < n and 0 <= zy < m:
                    if graph[zx][zy] == "." and visit[zx][zy] == 0:
                        visit[zx][zy] = 1
                        graph[zx][zy] = str(i)
                        temp.append((zx, zy))
                        ttt.append((zx, zy))
                        tt = 1
        q = ttt
    player[i] = temp
    return tt

while 1:
    cc = 0
    for i in range(1, p + 1):
        cc += bfs(i)
    if cc == 0:
        break

pp = [0] * (p + 1)
for i in range(n):
    for j in range(m):
        if graph[i][j] == "." or graph[i][j] == "#":
            continue
        ee = graph[i][j]

        pp[(int)(graph[i][j])] += 1
for i in range(1, p + 1):
    print(pp[i], end=" ")