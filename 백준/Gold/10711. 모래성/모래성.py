import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
time = 0

graph = []
test = deque()
for i in range(n):
    e = list(map(str, input().rstrip()))
    graph.append(e)
    for j in range(m):
        if graph[i][j] == ".":
            graph[i][j] = 0
            test.append((i, j))
        else:
            graph[i][j] = (int)(graph[i][j])


while 1:
    cnt = 0
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    temp = deque()
    nex = deque()
    while test:
        i, j = test.popleft()
        for a in range(8):
            zx = dx[a] + i
            zy = dy[a] + j
            if 0 <= zx < n and 0 <= zy < m:
                if graph[zx][zy] !=0:
                    graph[zx][zy] -= 1
                    if graph[zx][zy] == 0:
                        nex.append((zx, zy))
                        cnt += 1
    if cnt == 0:
        break
    time += 1
    test = nex

print(time)