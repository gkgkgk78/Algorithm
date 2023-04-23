import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, grap, visit):

    if x == n - 1 and y == m - 1:
        return 1
    elif visit[x][y]!=-1:
        return visit[x][y]
    visit[x][y] = 0
    for l in range(4):
        zx = dx[l] + x
        zy = dy[l] + y
        if 0 <= zx < n and 0 <= zy < m:
            if grap[x][y] > grap[zx][zy]:
                e=dfs(zx, zy, grap, visit)
                visit[x][y] += e
    return visit[x][y]

visit = [[-1] * m for _ in range(n)]

dfs(0, 0, graph, visit)

print(visit[0][0])