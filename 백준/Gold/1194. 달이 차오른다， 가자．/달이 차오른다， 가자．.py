import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
sx = -1
sy = -1
for i in range(n):
    e = list(map(str, input().rstrip()))
    for j in range(m):
        if e[j] == "0":
            sx = i
            sy = j
            e[j] = "."
    graph.append(e)

ans = sys.maxsize
visit = [[[0] * (1 << 6) for _ in range(m)] for _ in range(n)]


def bfs():
    global ans
    q = deque()
    q.append((sx, sy, 0, 0))
    visit[sx][sy][0] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y, count, value = q.popleft()
        
        if graph[x][y] == "1":
            ans = min(ans, count)
            return
        for i in range(4):
            zx = x + dx[i]
            zy = y + dy[i]
            if 0 <= zx < n and 0 <= zy < m and visit[zx][zy][value] == 0:
                if graph[zx][zy] == "#":
                    continue
                if "a" <= graph[zx][zy] <= "f":
                    nex = value | (1 << (ord(graph[zx][zy]) - ord('a')))
                    visit[zx][zy][nex] = 1
                    q.append((zx, zy, count + 1, nex))
                elif "A" <= graph[zx][zy] <= "F":
                    now = (1 << (ord(graph[zx][zy].lower()) - ord('a')))
                    if (value & (1 << (ord(graph[zx][zy].lower()) - ord('a')))) != 0:
                        visit[zx][zy][value] = 1
                        q.append((zx, zy, count + 1, value))
                else:
                    visit[zx][zy][value] = 1
                    q.append((zx, zy, count + 1, value))


bfs()
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)