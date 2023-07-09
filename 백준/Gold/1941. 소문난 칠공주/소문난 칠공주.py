import sys
from collections import deque

input = sys.stdin.readline
graph = []
dasom = []
total = []
for i in range(5):
    e = list(map(str, input().rstrip()))
    for j in range(5):
        total.append((i, j))
        if e[j] == "S":
            dasom.append([i, j])

    graph.append(e)

isselected = [-1] * (7)
to = 0

ans = 0


def game(temp):
    global ans
    visit = [[0] * 5 for _ in range(5)]
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    q = deque()
    q.append((temp[0][0], temp[0][1]))

    while q:
        a1, a2 = q.popleft()
        visit[a1][a2] = 1
        for i in range(4):
            zx = a1 + dx[i]
            zy = a2 + dy[i]
            if 0 <= zx < 5 and 0 <= zy < 5:
                if (zx, zy) in temp and visit[zx][zy] == 0:
                    visit[zx][zy] = 1
                    q.append((zx, zy))

    for a1, a2 in temp:
        if visit[a1][a2] == 0:
            return
    ans += 1


def comb(start, cnt):
    global to
    if cnt == 7:
        temp = []
        cn = 0
        for i in isselected:
            temp.append(total[i])
            if graph[total[i][0]][total[i][1]] == "S":
                cn += 1
        if cn < 4:
            return
        game(temp)

        return
    for i in range(start, 25):
        isselected[cnt] = i
        comb(i + 1, cnt + 1)


comb(0, 0)

print(ans)