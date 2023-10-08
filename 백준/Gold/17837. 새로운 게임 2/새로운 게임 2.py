#50분
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
horse = [[]]
total = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(1, k + 1):
    a1, a2, a3 = map(int, input().split())
    horse.append([a1 - 1, a2 - 1, a3 - 1])  # 이렇게 이동을 함
    total[a1 - 1][a2 - 1].append(i)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def chch(dir):
    if dir == 0:
        return 1
    elif dir == 1:
        return 0
    elif dir == 2:
        return 3
    else:
        return 2


def last(x, y, temp):
    g = total
    for i in temp:
        total[x][y].append(i)
        horse[i][0] = x
        horse[i][1] = y


def mo(x, y, dir, now, temp):  # now는 순서를 의미한다
    zx = x + dx[dir]
    zy = y + dy[dir]
    if not (0 <= zx < n and 0 <= zy < n):
        # 파
        di = chch(dir)
        zx = x + dx[di]
        zy = y + dy[di]
        if not (0 <= zx < n and 0 <= zy < n) or graph[zx][zy] == 2:
            zx = x
            zy = y
            last(zx, zy, temp)
        else:
            if graph[zx][zy] == 1:
                temp.reverse()
            last(zx, zy, temp)
        horse[now] = [zx, zy, di]
    else:
        if graph[zx][zy] == 0:
            # 흰
            horse[now] = [zx, zy, dir]
            last(zx, zy, temp)
        elif graph[zx][zy] == 1:
            # 빨
            horse[now] = [zx, zy, dir]
            temp.reverse()
            last(zx, zy, temp)

        else:
            # 파
            di = chch(dir)
            zx = x + dx[di]
            zy = y + dy[di]
            if not (0 <= zx < n and 0 <= zy < n) or graph[zx][zy] == 2:
                zx = x
                zy = y
                last(zx, zy, temp)
            else:
                if graph[zx][zy] == 1:
                    temp.reverse()
                last(zx, zy, temp)
            horse[now] = [zx, zy, di]
    if len(total[zx][zy]) >= 4:
        return 1
    else:
        return 0


def game(x, y, move, now):
    # 이제 움직 이면 된다
    temp = []
    aa = total[x][y].index(now)
    temp = total[x][y][aa:]
    total[x][y] = total[x][y][:aa]
    # 이제 이동을 해야 한다
    aa = mo(x, y, move, now, temp)
    if aa == 1:
        return 1
    else:
        return 0


time = 1
while time < 1000:
    for i in range(1, k + 1):
        a1, a2, a3 = horse[i]

        aa = game(a1, a2, a3, i)

        if aa == 1:
            print(time)
            sys.exit(0)

    time += 1
print(-1)