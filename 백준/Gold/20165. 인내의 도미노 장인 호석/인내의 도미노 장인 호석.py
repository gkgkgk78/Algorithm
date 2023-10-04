import sys
from collections import deque

input = sys.stdin.readline

ans = 0
n, m, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
temp = [["S"] * (m) for _ in range(n)]


def game(x, y, dir):
    global ans

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dd = ["N", "E", "S", "W"]
    tt = ["1", "2", "3", "4", "5"]
    di = -1
    for i in range(len(dd)):
        if dir == dd[i]:
            di = i
            break
    q = deque()
    q.append((x, y))
    ans += 1
    while q:
        x, y = q.popleft()
        now = (graph[x][y])
        temp[x][y] = "F"

        zx = x
        zy = y
        for _ in range(now - 1):
            zx += dx[di]
            zy += dy[di]
            if 0 <= zx < n and 0 <= zy < m:
                if temp[zx][zy] == "S":
                    ans += 1
                    temp[zx][zy] = "F"
                    q.append((zx, zy))
            else:
                break


for _ in range(r):
    # 무너뜨리고
    a1, a2, a3 = map(str, input().split())
    a1, a2 = (int)(a1), (int)(a2)
    a1 -= 1
    a2 -= 1
    if temp[a1][a2] == "F":
        continue
    else:
        game(a1, a2, a3)
    z1, z2 = map(int, input().split())
    temp[z1 - 1][z2 - 1] = "S"

print(ans)
for i in temp:
    print(*i)