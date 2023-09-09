import sys
from collections import deque
from itertools import combinations

n, m, g, r = map(int, input().split())
graph = []
position = []
for i in range(n):
    e = list(map(int, input().split()))
    for j in range(m):
        if e[j] == 2:
            position.append((i, j))
            e[j] = 1
    graph.append(e)

nex = list(combinations(position, g + r))

# 이제 nex에서 구하면 된다
ans = -sys.maxsize


def bfs(green, red):
    global ans
    q = deque()
    visit = [[0] * (m) for _ in range(n)]
    who = [[-1] * (m) for _ in range(n)]
    gr = [[]]
    total = []
    flower = 0
    time = 2
    for a1, a2 in green:
        visit[a1][a2] = 1
        q.append((a1, a2, 0))
        who[a1][a2] = 0
    for a1, a2 in red:
        visit[a1][a2] = 1
        q.append((a1, a2, 1))
        who[a1][a2] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    zz = graph
    while 1:
        if len(q) == 0:
            break
        temp = deque()
        while q:
            a1, a2, color = q.popleft()
            total.append((a1, a2))
            if graph[a1][a2] == 3:
                continue
            for i in range(4):
                zx = a1 + dx[i]
                zy = a2 + dy[i]
                if 0 <= zx < n and 0 <= zy < m:
                    if visit[zx][zy] == 0 and graph[zx][zy] == 1:
                        visit[zx][zy] = time
                        temp.append((zx, zy, color))
                        who[zx][zy] = color
                    elif visit[zx][zy] == time and who[zx][zy] != -1 and who[zx][zy] != color:

                        graph[zx][zy] = 3
        q = temp
        time += 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 3:
                flower += 1
    for a1, a2 in total:
        graph[a1][a2] = 1
    ans = max(ans, flower)


for i in nex:
    a1 = list(combinations(i, g))

    for j in a1:
        a1 = set(j)
        a2 = set(i) - a1
        # 초록이는 3 빨강이는 4로 해서 진행을 해보도록 하자
        for i1, i2 in a1:
            graph[i1][i2] = 0
        for i1, i2 in a2:
            graph[i1][i2] = 0

        bfs(a1, a2)
        for i1, i2 in a1:
            graph[i1][i2] = 1
        for i1, i2 in a2:
            graph[i1][i2] = 1
print(ans)