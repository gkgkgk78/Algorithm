#1시간 30분

import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
next_go = k
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 공격한 횟수 측정하는 변수
graph_attack = [[0] * (m) for _ in range(n)]


def who_attack():
    now = []
    now_val = sys.maxsize
    gg = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                continue
            if graph[i][j] > 0:
                gg += 1
            if graph[i][j] < now_val:
                now_val = graph[i][j]
                now = [(i, j, graph_attack[i][j], i + j, j)]  # 행 열 가장 최근 행+열 열
            elif graph[i][j] == now_val:
                now.append((i, j, graph_attack[i][j], i + j, j))

    if len(now) == 1:
        ne = now[0]
        return [ne[0], ne[1], gg]
    else:
        now = sorted(now, key=lambda x: (-x[2], -x[3], -x[4]))
        ne = now[0]
        return [ne[0], ne[1], gg]


def who_get():
    now = []
    now_val = -sys.maxsize
    for i in range(n):
        for j in range(m):

            if graph[i][j] > now_val:
                now_val = graph[i][j]
                now = [(i, j, graph_attack[i][j], i + j, j)]  # 행 열 가장 최근 행+열 열
            elif graph[i][j] == now_val:
                now.append((i, j, graph_attack[i][j], i + j, j))

    if len(now) == 1:
        ne = now[0]
        return [ne[0], ne[1]]
    else:
        now = sorted(now, key=lambda x: (x[2], x[3], x[4]))
        ne = now[0]
        return [ne[0], ne[1]]


def razer(atx, aty, gtx, gty, nownow):
    # 레이저 공격은 공격자의 위치에서 공격 대상 포탑까지 최단 경로로 이동을 해야한다.
    q = deque()
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visit = [[0] * (m) for _ in range(n)]
    back = [[[] for _ in range(m)] for _ in range(n)]
    visit[atx][aty] = 1

    q.append((atx, aty))
    tt = 0
    while q:
        x, y = q.popleft()
        if x == gtx and y == gty:
            tt = 1
            break
        for i in range(4):
            zx = dx[i] + x
            zy = dy[i] + y
            if zx >= n:
                zx = 0
            elif zx < 0:
                zx = n - 1
            if zy >= m:
                zy = 0
            elif zy < 0:
                zy = m - 1
            if graph[zx][zy] == 0:
                continue
            if visit[zx][zy] == 1:
                continue
            visit[zx][zy] = 1
            back[zx][zy] = [x, y]
            q.append((zx, zy))
    if tt == 0:
        return 0
    else:
        # 이제 역추적 하면서 가야 한다.
        attack_val = graph[atx][aty]
        graph[gtx][gty] -= (attack_val)
        zx = gtx
        zy = gty
        gg = graph
        if graph[gtx][gty] <= 0:
            graph[gtx][gty] = 0
        while 1:
            bx = back[zx][zy][0]
            by = back[zx][zy][1]
            if bx == atx and by == aty:
                break
            graph[bx][by] -= attack_val // 2
            if graph[bx][by] <= 0:
                graph[bx][by] = 0
            nownow[bx][by] = 1
            zx = bx
            zy = by


def bomb(atx, aty, gtx, gty, nownow):
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    ne = graph[atx][aty]
    ne1 = graph[atx][aty] // 2
    for i in range(9):
        zx = dx[i] + gtx
        zy = dy[i] + gty
        if zx >= n:
            zx = 0
        elif zx < 0:
            zx = n - 1
        if zy >= m:
            zy = 0
        elif zy < 0:
            zy = m - 1
        if zx == atx and zy == aty:
            continue
        if i != 4:
            graph[zx][zy] -= ne1
        else:
            graph[zx][zy] -= ne
        nownow[zx][zy] = 1
        if graph[zx][zy] <= 0:
            graph[zx][zy] = 0


def up(nownow):
    get = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and nownow[i][j] == 0:
                graph[i][j] += 1
            if graph[i][j] > 0:
                get += 1
    return get


for l in range(next_go):

    # 공격자 선정 해야함
    # 가장 약한 포탑 찾기

    attack = who_attack()
    if attack[2] == 1:
        break

    got = who_get()
    graph[attack[0]][attack[1]] += (n + m)
    graph_attack[attack[0]][attack[1]] = l + 1
    nownow = [[0] * (m) for _ in range(n)]
    nownow[attack[0]][attack[1]] = 1
    nownow[got[0]][got[1]] = 1
    nn = razer(attack[0], attack[1], got[0], got[1], nownow)
    # 이제 공격을 하고자 함
    if nn == 0:
        # 포탄 공격 해야함
        bomb(attack[0], attack[1], got[0], got[1], nownow)

    up(nownow)

ans = -sys.maxsize
for i in range(n):
    for j in range(m):
        ans = max(ans, graph[i][j])
print(ans)