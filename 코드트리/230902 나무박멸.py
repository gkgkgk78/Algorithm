#한 40분정도 걸렸으려나?..
import sys

input = sys.stdin.readline
import heapq

graph = []
ans = 0

n, m, k, c = map(int, input().split())
poison = [[0] * (n) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(n):
    graph.append(list(map(int, input().split())))


def check(x, y):
    cc = 0
    for i in range(4):
        zx = x + dx[i]
        zy = y + dy[i]
        if 0 <= zx < n and 0 <= zy < n and graph[zx][zy] > 0:
            cc += 1
    return cc


def growth():
    temp = [[0] * (n) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                temp[i][j] += check(i, j)
    for i in range(n):
        for j in range(n):
            graph[i][j] += temp[i][j]


def check1(x, y, temp):
    cc = 0
    tt = []
    for i in range(4):
        zx = x + dx[i]
        zy = y + dy[i]
        if 0 <= zx < n and 0 <= zy < n and graph[zx][zy] == 0 and poison[zx][zy] == 0:
            tt.append((zx, zy))
    if len(tt) > 0:
        ne = graph[x][y] // len(tt)
        for a1, a2 in tt:
            temp[a1][a2] += ne


def go():
    temp = [[0] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                check1(i, j, temp)

    for i in range(n):
        for j in range(n):
            graph[i][j] += temp[i][j]


def ups(x, y):
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    tt = graph[x][y]
    for i in range(4):
        zx = x
        zy = y
        for j in range(k):
            zx += dx[i]
            zy += dy[i]
            if (0 <= zx < n and 0 <= zy < n):
                if graph[zx][zy] == -1 or graph[zx][zy] == 0:
                    break
                else:
                    tt += graph[zx][zy]
            else:
                break

    return tt


def last(x, y):
    global ans
    # 이제 움직이면서 정리를 해주면 된다.
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]
    ans += graph[x][y]
    graph[x][y] = 0
    poison[x][y] = c + 1

    for i in range(4):
        zx = x
        zy = y
        for j in range(k):
            zx += dx[i]
            zy += dy[i]
            if (0 <= zx < n and 0 <= zy < n):
                if graph[zx][zy] == -1 or graph[zx][zy] == 0:
                    poison[zx][zy] = c + 1
                    break
                else:
                    ans += graph[zx][zy]
                    graph[zx][zy] = 0
                    poison[zx][zy] = c + 1
            else:
                break


def last1():
    # 이제 움직이면서 정리를 해주면 된다.

    for i in range(n):
        for j in range(n):
            if poison[i][j] > 0:
                poison[i][j] -= 1


def death():
    q = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                a1 = ups(i, j)
                heapq.heappush(q, (-a1, i, j))

    # 이제 하나 뽑아서 진행 하면 된다
    if q:
        _, x, y = heapq.heappop(q)
        last(x, y)


for _ in range(m):

    growth()
    go()

    death()
    last1()

print(ans)