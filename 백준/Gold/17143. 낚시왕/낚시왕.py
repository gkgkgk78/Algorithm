import sys
from collections import deque

input = sys.stdin.readline

r, c, m = map(int, input().split())
graph = [[0] * (c + 1) for _ in range(r + 1)]
shark = [[[] for _ in range(c + 1)] for _ in range(r + 1)]

for _ in range(m):
    x, y, speed, dir, size = map(int, input().split())
    shark[x][y].append([speed, dir, size])
    # 1위 2아래 3오른 4왼
ans = 0


def death(z):
    global ans
    for i in range(1, r + 1):
        if len(shark[i][z]) == 1:
            speed, dir, size = shark[i][z][0]
            shark[i][z] = []
            ans += size
            break


def go(x, y, speed, dir):
    # 1위 2아래 3오른 4왼
    dx = [-1, -1, 1, 0, 0]
    dy = [-1, 0, 0, 1, -1]
    if dir == 3 or dir == 4:
        nex = (speed) % ((c - 1) * 2)
        # 이제 남은 만큼 이동 해야함
        zx = x
        zy = y
        while 1:
            tx = zx
            ty = zy
            zx += dx[dir] * nex
            zy += dy[dir] * nex
            if zy <= 0 or zy >= c + 1:
                if dir == 3:
                    dir = 4
                else:
                    dir = 3
                if zy <= 0:
                    nex -= ty
                    zy = 2
                else:
                    nex -= (c - ty + 1)
                    zy = c - 1
                if nex <= 0:
                    break
            else:
                break
    else:
        nex = (speed) % ((r - 1) * 2)
        zx = x
        zy = y
        while 1:
            tx = zx
            ty = zy
            zx += dx[dir] * nex
            zy += dy[dir] * nex
            if zx <= 0 or zx >= r + 1:
                if dir == 1:
                    dir = 2
                else:
                    dir = 1
                if zx <= 0:
                    nex -= tx
                    zx = 2
                else:
                    nex -= (r - tx + 1)
                    zx = r - 1
                if nex <= 0:
                    break
            else:
                break
    return [zx, zy, dir]


temp = [[[] for _ in range(c + 1)] for _ in range(r + 1)]


def move():
    # 이제 하나하나 이동을 하자
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if len(shark[i][j]) == 1:
                speed, dir, size = shark[i][j][0]
                x, y, dd = go(i, j, speed, dir)
                # 이제 이동 하게 됨
                temp[x][y].append([speed, dd, size])
                shark[i][j] = []

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            # 상어 잡아 먹기
            if len(temp[i][j]) > 1:
                ee = temp[i][j]
                ee = sorted(ee, key=lambda x: -x[2])
                shark[i][j] = [ee[0]]
                temp[i][j] = []
            elif len(temp[i][j]) == 1:
                ee = temp[i][j]
                shark[i][j] = [ee[0]]
                temp[i][j] = []


for z in range(1, c + 1):
    # 낚시왕 이동
    # 이제 잡을 거임
    death(z)
    # 상어 이동
    move()
    # for i in shark:
    #     print(i)
    # print()
print(ans)