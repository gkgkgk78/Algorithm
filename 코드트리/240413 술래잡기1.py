import sys
from collections import deque
#2시간 15분
input = sys.stdin.readline
n, m, h, k = map(int, input().split())
trees = [[0] * (n) for _ in range(n)]
movers_graph = [[[] for _ in range(n)] for _ in range(n)]
# 도망자 먼저 이동, 그다음 술래 이동
movers = []
for a in range(m):
    x, y, dir = map(int, input().split())
    movers.append([x - 1, y - 1, dir])
    movers_graph[x - 1][y - 1].append(a)  # 도망자 몇번이 해당되는 위치에 있는가 나타냄
for a in range(h):
    x, y = map(int, input().split())
    trees[x - 1][y - 1] = 1

# 술래 이동하는거 구현 해보자
atx, aty = n // 2, n // 2
adir = 0
# 1-2, 2-2, 3-2, 4-2, .....
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
move_check = 0  # 0이면 move_first로 해서 이동 하면 됨
move_count = 0  # 2번씩 이동 해야함
move_index = 1  # 얼만큼 이동할지
gtemp = 0
gvisit = [[0] * (n) for _ in range(n)]


def move_first():
    global atx, aty, adir, move_count, move_index, gtemp, gvisit,move_check

    # 우선 이동
    atx += dx[adir]
    aty += dy[adir]
    move_count += 1
    #print(atx,aty)
    if atx == 0 and aty == 0:
        move_check = 1
        move_count = 0
        atx = 0
        aty = 0
        adir = 2
        move_index = 1
        gtemp = 0
        gvisit = [[0] * (n) for _ in range(n)]
        gvisit[0][0] = 1
    if move_count == move_index:
        move_count = 0
        gtemp += 1
        if gtemp == 2:
            move_index += 1
            gtemp = 0
            # 방향 전환
        adir = (adir + 1) % 4


def move_second():
    global atx, aty, adir, move_count, move_index, move_check, gvisit
    # 우선 이동
    atx += dx[adir]
    aty += dy[adir]
    if atx == n // 2 and aty == n // 2:
        move_check = 0
        move_count = 0
        adir = 0
        move_index = 1
    else:
        if not (0 <= atx + dx[adir] < n and 0 <= aty + dy[adir] < n):
            # 방향 전환
            adir -= 1
            if adir == -1:
                adir = 3
        elif gvisit[atx + dx[adir]][aty + dy[adir]] == 1:
            # 방향 전환
            adir -= 1
            if adir == -1:
                adir = 3
        gvisit[atx][aty] = 1


def move_movers():
    # 도망자 이동
    aa = movers

    for i in range(len(movers)):
        if len(movers[i]) > 0:
            x, y, dir = movers[i]
            leng_check = abs(x - atx) + abs(y - aty)
            if leng_check <= 3:
                # 이제 이동 가능
                zx = x + dx[dir]
                zy = y + dy[dir]
                if 0 <= zx < n and 0 <= zy < n:
                    if zx == atx and zy == aty:
                        zx = x
                        zy = y
                    movers[i] = [zx, zy, dir]
                    movers_graph[x][y].remove(i)
                    movers_graph[zx][zy].append(i)
                else:
                    dir = (dir + 2) % 4
                    zx = x + dx[dir]
                    zy = y + dy[dir]
                    if zx == atx and zy == aty:
                        zx, zy = x, y
                    movers[i] = [zx, zy, dir]
                    movers_graph[x][y].remove(i)
                    movers_graph[zx][zy].append(i)

answer = 0
def attack(k1):
    global answer
    x, y, dir = atx, aty, adir
    chch = 0
    for i in range(2):
        x += dx[adir]
        y += dy[adir]
        if 0 <= x < n and 0 <= y < n:
            if trees[x][y] == 1:
                continue
            else:
                # 이제 잡을수 있음
                now = movers_graph[x][y]
                if len(now) > 0:
                    chch += len(now)
                    for a in movers_graph[x][y]:
                        movers[a] = []
                    movers_graph[x][y] = []
        else:
            break
    if len(movers_graph[atx][aty]) > 0 and trees[atx][aty] == 0:
        now = movers_graph[atx][aty]
        chch += len(now)
        for a in now:
            movers[a] = []
        movers_graph[atx][aty] = []

    answer += (k1 * chch)


for l in range(k):
    if l==6:
        l=6
    move_movers()
    if move_check == 0:
        move_first()
    else:
        move_second()
        #("하")

    attack(l + 1)
    #print(atx,aty,adir)
print(answer)
