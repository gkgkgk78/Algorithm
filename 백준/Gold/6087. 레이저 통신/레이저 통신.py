import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())

graph = []
start = []
for i in range(n):
    e = list(map(str, input().rstrip()))
    for j in range(m):
        if e[j].lower() == "c":
            start.append((i, j))
    graph.append(e)
visit = [[[sys.maxsize] * 4 for _ in range(m)] for _ in range(n)]  # 들어 올때 빛의 방향을 의미를 함

# 아무 한점에서 시작을 해서 진행을 해보도록 하자

startx = start[0][0]
starty = start[0][1]
lastx = start[1][0]
lasty = start[1][1]


def check_dir(dir):
    if dir == 0 or dir == 2:
        return [3, 1]
    else:
        return [2, 0]


def bfs(x, y):
    q = deque()
    for i in range(4):
        q.append((0, x, y, i))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while (len(q) > 0):
        count, x1, y1, dir = q.popleft()
        zx = x1 + dx[dir]
        zy = y1 + dy[dir]

        if 0 <= zx < n and 0 <= zy < m:
            if graph[zx][zy] == "*":
                continue
            if visit[zx][zy][dir] <= count:  # 그전에 방문했다면 넘어감
                continue
            visit[zx][zy][dir] = count
            # 여기에선 세가지 방향으로 갈수 있을 것이다
            # 거울을 사용하지 않고 그냥 가는 경우
            q.appendleft((count, zx, zy, dir))
            # 거울을 사용하는 경우
            temp = check_dir(dir)
            for a1 in temp:
                if visit[zx][zy][a1] <= count + 1:
                    continue
                visit[zx][zy][a1] = count + 1
                q.appendleft((count + 1, zx, zy, a1))
            if graph[zx][zy] == "C":
                visit[zx][zy][dir] = min(visit[zx][zy][dir], count + 1)


bfs(startx, starty)
print(min(visit[lastx][lasty]))
