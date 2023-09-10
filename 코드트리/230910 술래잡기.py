#2시간 40분 걸림, 그냥 범위 안큰 경우에는 그냥 따로 관리 하지 말고 다 돌려서 확인 하고
#그리고 문제를 제대로 읽으면 시간이 줄어들듯 하다...
import sys
from collections import deque

n, m, h, k = map(int, input().split())
first = [[0] * (n) for _ in range(n)]
tree = [[0] * (n) for _ in range(n)]

run_graph = [[[] for _ in range(n)] for _ in range(n)]


def move():
    x, y = n // 2, n // 2
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    total = 1
    dir = 0
    now = 1
    count = 0
    count_idx = 0  # 현재 주어진 count안에서 몇번 이동 했는지를 파악하기 위한 부분임
    while 1:
        if x == 0 and y == 0:
            first[x][y] = total
            break
        first[x][y] = total
        total += 1
        x += dx[dir]
        y += dy[dir]
        count_idx += 1
        if count_idx == now:
            count_idx = 0
            count += 1
            dir = (dir + 1) % 4
        if count == 2:
            now += 1
            count = 0


for i in range(m):
    x, y, di = map(int, input().split())
    run_graph[x - 1][y - 1].append([x - 1, y - 1, di, 1])

for _ in range(h):
    a1, a2 = map(int, input().split())
    tree[a1 - 1][a2 - 1] = 1

move()
nowx, nowy = n // 2, n // 2
now_dir = -1


def runs():
    global run_graph
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    temp = []

    for i in range(n):
        for j in range(n):
            if len(run_graph[i][j]) > 0:
                for x, y, dir, live in run_graph[i][j]:
                    co = abs(x - nowx) + abs(y - nowy)
                    if live == 1 and co <= 3:
                        zx = x + dx[dir]
                        zy = y + dy[dir]
                        if 0 <= zx < n and 0 <= zy < n:
                            if not (zx == nowx and zy == nowy):
                                temp.append([zx, zy, dir, live])
                            else:
                                temp.append([x, y, dir, live])
                        else:
                            if dir == 0:
                                dir = 1
                            elif dir == 1:
                                dir = 0
                            elif dir == 2:
                                dir = 3
                            else:
                                dir = 2
                            zx = x + dx[dir]
                            zy = y + dy[dir]
                            if 0 <= zx < n and 0 <= zy < n:
                                if not (zx == nowx and zy == nowy):
                                    temp.append([zx, zy, dir, live])
                                else:
                                    temp.append([x, y, dir, live])
                    else:
                        temp.append([x, y, dir, live])
                run_graph[i][j] = []

    for zx, zy, dir, live in temp:
        run_graph[zx][zy].append([zx, zy, dir, live])


ins = 1


def move_center():
    global nowx, nowy, now_dir, ins
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    nn = first[nowx][nowy]
    if ins == 1:
        nn += 1
    else:
        nn -= 1
    for i in range(4):
        zx = dx[i] + nowx
        zy = dy[i] + nowy
        if 0 <= zx < n and 0 <= zy < n:
            if first[zx][zy] == nn:
                nowx = zx
                nowy = zy
                now_dir = i
                break
    if nowx == 0 and nowy == 0:
        ins = 0
        nn = first[nowx][nowy]
        nn -= 1
        # 방향만 바꿔 주자
        for i in range(4):
            zx = dx[i] + nowx
            zy = dy[i] + nowy
            if 0 <= zx < n and 0 <= zy < n:
                if first[zx][zy] == nn:
                    now_dir = i
                    break
    elif nowx == n // 2 and nowy == n // 2:
        ins = 1
        nn = first[nowx][nowy]
        nn += 1
        # 방향만 바꿔 주자
        for i in range(4):
            zx = dx[i] + nowx
            zy = dy[i] + nowy
            if 0 <= zx < n and 0 <= zy < n:
                if first[zx][zy] == nn:
                    now_dir = i
                    break
    else:
        nn = first[nowx][nowy]
        if ins == 1:
            nn += 1
        else:
            nn -= 1
        for i in range(4):
            zx = dx[i] + nowx
            zy = dy[i] + nowy
            if 0 <= zx < n and 0 <= zy < n:
                if first[zx][zy] == nn:
                    now_dir = i
                    break


ans = 0


def delete(ii):
    global ans
    zx = nowx
    zy = nowy
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    tt = 0
    if tree[zx][zy] == 0 and len(run_graph[zx][zy]) > 0:
        tt += len(run_graph[zx][zy])
        run_graph[zx][zy] = []

    for i in range(2):
        zx += dx[now_dir]
        zy += dy[now_dir]
        if 0 <= zx < n and 0 <= zy < n:
            if tree[zx][zy] == 1:
                continue
            if len(run_graph[zx][zy]) > 0:
                tt += len(run_graph[zx][zy])
                run_graph[zx][zy] = []
        else:
            break

    ans += (ii * tt)


for i in range(1, k + 1):
    # 이제 도망자들이 움직 여야 한다

    runs()
    move_center()
    delete(i)

print(ans)
