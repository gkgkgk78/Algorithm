import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = []
vister = [[] for _ in range(m)]

visite = [[0] * (n) for _ in range(n)]
exitx = -1
exity = -1
for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(m):
    a1, a2 = map(int, input().split())
    a1 -= 1
    a2 -= 1
    vister[i] = [a1, a2]
    visite[a1][a2] = 1

exitx, exity = map(int, input().split())
exitx -= 1
exity -= 1
graph[exitx][exity] = -1  # 출구를 의미를 함

total_move = 0


def move(x, y):
    global total_move
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    can_move = abs(x - exitx) + abs(y - exity)
    can_next = sys.maxsize
    canx = -1
    cany = -1
    # 최소한 이것 보다는 적어야 한다.
    for i in range(4):
        zx = dx[i] + x
        zy = dy[i] + y
        if 0 <= zx < n and 0 <= zy < n and not (1 <= graph[zx][zy] <= 9):
            # 이동 가능하다면 우선 구해야 한다.
            nex = abs(zx - exitx) + abs(zy - exity)
            if nex < can_move and nex < can_next:
                can_next = min(can_next, nex)
                canx = zx
                cany = zy

    if can_next == sys.maxsize:
        return (x, y)
    else:
        # 움직 일수 있는 칸이 존재 한다는 거임
        if can_next == 0:
            total_move += 1
            return (-1, -1)
        else:
            total_move += 1
            return (canx, cany)


def find():
    global exitx, exity
    tempx = exitx
    tempy = exity
    for i in range(1, n+1):  # 길이를 의미 함
        # 시작점
        for j in range(n):
            for k in range(n):
                zx = j + i
                zy = k + i
                if 0 <= zx < n and 0 <= zy < n:
                    if j <= tempx <= zx and k <= tempy <= zy:
                        # 속하는 범위 안에 존재 한다면
                        for a1 in range(j, zx + 1):
                            for a2 in range(k, zy + 1):
                                if visite[a1][a2] >= 1:
                                    return (i + 1, j, k)


def rotate():
    # 출구와 참가자 최소 1명을 포함한 가장 작은 정사각형을 구해 보도록 하자
    global exitx, exity, vister, visite

    nn, nx, ny = find()

    temp = [[0] * (nn) for _ in range(nn)]
    temp1 = [[0] * (nn) for _ in range(nn)]
    temp2 = [[0] * (nn) for _ in range(nn)]
    temp3 = [[0] * (nn) for _ in range(nn)]
    zx = 0
    zy = 0
    for i in range(nx, nx + nn):
        zy = 0
        for j in range(ny, ny + nn):
            temp[zx][zy] = graph[i][j]
            temp1[zx][zy] = visite[i][j]
            zy += 1
        zx += 1

    for i in range(nn):
        for j in range(nn):
            # 정사각형 움직이는 거니
            t = temp[i][j]
            if 1 <= t <= 9:
                t -= 1
            temp2[j][nn - i - 1] = t
            temp3[j][nn - i - 1] = temp1[i][j]
    zx = 0
    zy = 0
    for i in range(nx, nx + nn):
        zy = 0
        for j in range(ny, ny + nn):
            graph[i][j] = temp2[zx][zy]
            if graph[i][j] == -1:
                exitx = i
                exity = j
            visite[i][j] = temp3[zx][zy]
            zy += 1
        zx += 1
    vister = []

    for i in range(n):
        for j in range(n):
            for k in range(visite[i][j]):
                vister.append((i, j))


for u in range(k):
    # 우선 참가자 이동을 한다
    tt = []

    for j in range(len(vister)):
        a1, a2 = vister[j]
        visite[a1][a2] = 0
        z1, z2 = move(a1, a2)
        if z1 == -1 and z2 == -1:
            continue
        tt.append((z1, z2))
    for a1, a2 in tt:
        visite[a1][a2] += 1
    if len(tt) == 0:
        break
    # 이제 회전을 할 차례 임
    rotate()


print(total_move)
print(exitx + 1, exity + 1)