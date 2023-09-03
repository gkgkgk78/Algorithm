#1시간 30분
import sys
from collections import deque

input = sys.stdin.readline

ans = 0

n, m, k = map(int, input().split())
head_tail = [[(-1, -1), (-1, -1)] for _ in range(m)]

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visit = [[0] * (n) for _ in range(n)]
team = [[-1] * n for _ in range(n)]
team_ver = []


def make_team(x, y, co):
    visit[x][y] = 1
    q = deque()
    q.append((x, y))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    head = []
    tail = []
    total = []
    while q:
        a1, a2 = q.popleft()
        total.append((a1, a2))
        if graph[a1][a2] == 1:
            head = [a1, a2]
        elif graph[a1][a2] == 3:
            tail = [a1, a2]
        for i in range(4):
            zx = dx[i] + a1
            zy = dy[i] + a2
            if 0 <= zx < n and 0 <= zy < n:
                if visit[zx][zy] == 0 and graph[zx][zy] != 0:
                    q.append((zx, zy))
                    visit[zx][zy] = 1
    head_tail[co][0] = head
    head_tail[co][1] = tail
    for a1, a2 in total:
        team[a1][a2] = co


co = 0
# 이제 돌기 시작하면서 찾아 보도록 하자
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and visit[i][j] == 0:
            make_team(i, j, co)
            co += 1


def get_team(x, y):
    visit = [[0] * (n) for _ in range(n)]
    visit[x][y] = 1
    q = deque()
    q.append((x, y))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    total = []
    tt = team[x][y]
    while q:
        a1, a2 = q.popleft()
        total.append((a1, a2))
        for i in range(4):
            zx = dx[i] + a1
            zy = dy[i] + a2
            if 0 <= zx < n and 0 <= zy < n:
                if visit[zx][zy] == 0 and team[zx][zy] == tt and 1 <= graph[zx][zy] <= 2:
                    q.append((zx, zy))
                    visit[zx][zy] = 1
    total.append((head_tail[tt][1][0], head_tail[tt][1][1]))
    return total


def move(he, ta, p):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    x = -1
    y = -1
    zx = he[0]
    zy = he[1]
    total = get_team(zx, zy)
    lx, ly = total[-1]
    for i in range(4):
        tx = zx + dx[i]
        ty = zy + dy[i]
        if 0 <= tx < n and 0 <= ty < n and (graph[tx][ty] == 4 or graph[tx][ty]==3):
            x = tx
            y = ty
            break
    ea = graph
    # 이제 이동시킬 하나를 찾았음
    for i in range(len(total)):
        nx = -1
        ny = -1
        zx, zy = total[i]
        if i + 1 < len(total):
            nx, ny = total[i + 1]
        graph[x][y] = graph[zx][zy]
        if [zx,zy]!=head_tail[p][0]:
            graph[zx][zy] = 4
        if i == 0:
            head_tail[p][0] = [x, y]
        if i == len(total) - 1:
            head_tail[p][1] = [x, y]
            graph[x][y]=3
        x = zx
        y = zy


def get_point(x, y, dir):
    global ans
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    # 이제 움직이면서 확인 하면 된다.
    zx = x
    zy = y
    cc = 0
    yy = graph
    while 0 <= zx < n and 0 <= zy < n:
        if 1 <= graph[zx][zy] <= 3:
            cc = 1
            break
        zx += dx[dir]
        zy += dy[dir]

    if cc == 1:
        h1, t1 = head_tail[team[zx][zy]]
        if h1==[-1,-1]:
            tt=1
        # 이제 찾은 얘에서 몇번째 얘인지 확인한후 점수 더하고
        total = get_team(h1[0], h1[1])
        ee = total.index((zx, zy)) + 1
        ans += ee * ee
        graph[t1[0]][t1[1]] = 1
        graph[h1[0]][h1[1]] = 3
        # 머리와 꼬리를 바꾸면 된다
        head_tail[team[zx][zy]] = [t1, h1]


lx, ly = 0, 0
dir = 0
w = 1
for _ in range(1, k + 1):
    # 이제 이동을 시작 하면 된다
    p = 0
    for i in head_tail:
        he, ta = i
        # 이제 이동을 하게 될거다
        move(he, ta, p)
        p += 1

    # 이제 공을 던지자

    if w ==(4 * n)+1:
        w = 1
    if w == 1:
        lx, ly = 0, 0
        dir = 0
    elif w == n + 1:
        lx, ly = n - 1, 0
        dir = 1
    elif w == 2 * n + 1:
        lx, ly = n - 1, n - 1
        dir = 2
    elif w == 3 * n + 1:
        lx, ly = 0, n - 1
        dir = 3
    elif 2 <= w <= n:
        lx += 1
    elif n + 2 <= w <= 2 * n:
        ly += 1
    elif 2 * n + 2 <= w <= 3 * n:
        lx -= 1
    elif 3 * n + 2 <= w <= 4 * n:
        ly -= 1

    get_point(lx, ly, dir)

    w += 1
print(ans)