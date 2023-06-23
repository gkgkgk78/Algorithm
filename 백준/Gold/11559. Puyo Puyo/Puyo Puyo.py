import sys
from collections import deque

input = sys.stdin.readline

graph = []

ans = 0

for _ in range(12):
    e = list(map(str, input().rstrip()))
    graph.append(e)


def down():
    for l in range(6):
        # 거꾸로 해서 내려 가도록 하자
        for i in range(10, -1, -1):
            if graph[i][l] != "." and graph[i + 1][l] == ".":  # 이렇게 된다면 이제 움직 여야 함

                temp = graph[i][l]
                zx = i
                while zx < 12:
                    zx += 1
                    if zx == 12:
                        zx -= 1
                        break
                    if graph[zx][l] != ".":
                        zx -= 1
                        break
                graph[zx][l] = temp
                graph[i][l] = "."


def bfs(color, x, y, visit):
    q = deque()
    visit[x][y] = 1
    q.append((x, y))
    temp = []

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y = q.popleft()
        temp.append((x, y))
        for l in range(4):
            zx = x + dx[l]
            zy = y + dy[l]
            if 0 <= zx < 12 and 0 <= zy < 6:
                if visit[zx][zy] == 0 and graph[zx][zy] == color:
                    q.append((zx, zy))
                    visit[zx][zy] = 1
    if len(temp) < 4:
        temp = []
    return temp


while 1:

    visit = [[0] * (6) for _ in range(12)]
    total = []

    for i in range(12):
        for j in range(6):
            if graph[i][j] != "." and visit[i][j] == 0:
                total += bfs(graph[i][j], i, j, visit)
    if len(total) == 0:
        break
    for a1, a2 in total:
        graph[a1][a2] = "."

    down()


    ans += 1

print(ans)