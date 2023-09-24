import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())

e = []
for _ in range(2):
    temp = []
    for _ in range(2):
        a1, a2 = map(int, input().split())
        temp.append([a1, a2])
    e.append(temp)

e = list(permutations(e, 2))

# 이제 필요한 전선 길이의 최솟값을 출력 하고자 한다
ans = sys.maxsize


def bfs(x, y, lx, ly, visit):
    q = deque()

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q.append((x, y))
    visit1 = [[0] * (m + 1) for _ in range(n + 1)]
    visit1[x][y] = 1
    before = [[[] for _ in range(m + 1)] for _ in range(n + 1)]
    check = 0

    while q:
        a1, a2 = q.popleft()

        if a1 == lx and a2 == ly:
            check = 1
            break
        for i in range(4):
            zx = a1 + dx[i]
            zy = a2 + dy[i]
            if 0 <= zx <= n and 0 <= zy <= m:
                if visit[zx][zy] == 0 and visit1[zx][zy] == 0:
                    visit1[zx][zy] = 1
                    before[zx][zy] = [a1, a2]
                    q.append((zx, zy))

    if check == 0:
        return -1
    co = 0
    while 1:

        visit[lx][ly] = 1
        if lx == x and ly == y:
            break
        lx, ly = before[lx][ly]
        co += 1

    return co


for i in e:
    visit = [[0] * (m + 1) for _ in range(n + 1)]
    check = 0
    cou = 0

    for x, y in i:
        a1, a2 = x
        a3, a4 = y
        visit[a1][a2]=1
        visit[a3][a4]=1

    for x, y in i:
        a1, a2 = x
        a3, a4 = y
        visit[a3][a4] = 0
        ee = bfs(a1, a2, a3, a4, visit)
        if ee == -1:
            check = 1
            break
        else:
            cou += ee

    if check == 0:
        ans = min(cou, ans)

if ans == sys.maxsize:
    print("IMPOSSIBLE")
else:
    print(ans)