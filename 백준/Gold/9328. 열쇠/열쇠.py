import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())


def bfs(graph, key, n, m):
    q = deque()
    visit = [[0] * (m + 2) for _ in range(n + 2)]
    keys = [[0] * (m + 2) for _ in range(n + 2)]
    visit[0][0] = 1
    q.append((0, 0))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    ans = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            zx = x + dx[i]
            zy = y + dy[i]
            if 0 <= zx < n + 2 and 0 <= zy < m + 2 and graph[zx][zy] != "*" and visit[zx][zy] == 0:
                if "A" <= graph[zx][zy] <= "Z":
                    te = graph[zx][zy].lower()
                    if te not in key:
                        continue
                elif "a" <= graph[zx][zy] <= "z":

                    if graph[zx][zy] not in key:
                        visit = [[0] * (m + 2) for _ in range(n + 2)]
                        key[graph[zx][zy]] = 1
                elif graph[zx][zy] == "$" and keys[zx][zy] == 0:
                    ans += 1
                    keys[zx][zy] = 1

                visit[zx][zy] = 1
                q.append((zx, zy))

    return ans


for _ in range(t):
    n, m = map(int, input().split())
    graph = [["."] * (m + 2) for _ in range(n + 2)]
    temp = []
    key = dict()
    for _ in range(n):
        temp.append(list(map(str, input().rstrip())))
    la = list(map(str, input().rstrip()))

    for i in la:
        if i != "0":
            key[i] = 1

    x = 1
    y = 1
    for i in range(n):
        for j in range(m):
            graph[x][y] = temp[i][j]
            y += 1
        x += 1
        y = 1

    print(bfs(graph, key, n, m))