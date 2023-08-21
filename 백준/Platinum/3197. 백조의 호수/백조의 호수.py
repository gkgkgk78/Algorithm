import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

visit = [[0] * (m) for _ in range(n)]
graph = []
last = deque()
water = deque()
for i in range(n):
    e = list(map(str, input().rstrip()))
    graph.append(e)
    for j in range(m):
        if e[j] == "L":
            last = deque()
            last.append((i, j))
            water.append((i, j))
        elif e[j] == ".":
            water.append((i, j))

nex = deque()


# 처음은 그냥 해야함
def bfs_water(now):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while now:
        a1, a2 = now.popleft()

        visit[a1][a2] = 1
        for i in range(4):
            zx = a1 + dx[i]
            zy = a2 + dy[i]
            if 0 <= zx < n and 0 <= zy < m:
                if visit[zx][zy] == 0 and graph[zx][zy] == "X":
                    visit[zx][zy] = 1
                    nex.append((zx, zy))
                    graph[zx][zy] = "."


visit1 = [[0] * (m) for _ in range(n)]

count = 0
def bfs_last():
    global last,count
    q = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    tt=graph
    while last:
        q.append(last.popleft())
    while q:
        n1, n2 = q.popleft()
        visit1[n1][n2] = 1
        if graph[n1][n2] == "L":
            count += 1
        if graph[n1][n2] == "L" and count == 2:
            return 1
        for i in range(4):
            zx = n1 + dx[i]
            zy = n2 + dy[i]
            if 0 <= zx < n and 0 <= zy < m:
                if visit1[zx][zy] == 0 and graph[zx][zy] != "X":
                    visit1[zx][zy] = 1
                    q.append((zx, zy))
                    last.append((zx,zy))


    return 0


def bfs_x():
    global nex
    q = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while nex:
        a1, a2 = nex.popleft()

        visit[a1][a2] = 1
        graph[a1][a2] = "."
        for i in range(4):
            zx = a1 + dx[i]
            zy = a2 + dy[i]
            if 0 <= zx < n and 0 <= zy < m:
                if visit[zx][zy] == 0 and graph[zx][zy] == "X":
                    visit[zx][zy] = 1
                    q.append((zx, zy))
                    graph[zx][zy] = "."
    nex = q


today = 1


bfs_water(water)
ee = bfs_last()

if ee == 1:
    print(1)
    sys.exit()

while 1:
    bfs_x()
    # for i in graph:
    #     print(i)
    # print()
    ee = bfs_last()
    today += 1
    if ee == 1:
        print(today)
        break