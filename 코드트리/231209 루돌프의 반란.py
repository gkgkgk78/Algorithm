#3시간 걸림
import sys
input = sys.stdin.readline

n, m, p, C, D = map(int, input().split())
graph = [[-1] * (n) for _ in range(n)]  # 0은 루돌프, 1부터는 산타들을 의믜
scores = [0] * (p + 1)
santa_alive = [0] * (p + 1)  # -1이면 죽은거 0이면 가능한거 아니면 하나씩 감소
roux, rouy = map(int, input().split())
roux -= 1
rouy -= 1
roupower = C

santa = [[] for _ in range(p + 1)]
for i in range(p):
    x, y, d = map(int, input().split())
    graph[y - 1][d - 1] = x
    santa[x] = [y - 1, d - 1]  # 좌표 임


def move_roudol():
    # 탈락하지 않은 산타중 가장 가까운 산타 향해 1칸 돌진한다
    check = sys.maxsize
    lx, ly = -1, -1
    total = []
    for i in range(1, p + 1):
        if santa_alive[i] != -1:
            # 거리 계산
            tx, ty = santa[i]
            temp = (tx - roux) ** 2 + (ty - rouy) ** 2
            total.append((temp, tx, ty))
    total = sorted(total, key=lambda x: (x[0], -x[1], -x[2]))
    lx, ly = total[0][1], total[0][2]
    # 이제 찾았으니 8방향중 가장 가까워 지는 방향을 찾으면 된다
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    temp = []
    # 가장 가까워 지는 칸을 찾아보자
    for i in range(len(dx)):
        zx = dx[i] + roux
        zy = dy[i] + rouy
        if 0 <= zx < n and 0 <= zy < n:
            tt = (lx - zx) ** 2 + (ly - zy) ** 2
            temp.append((tt, zx, zy, i))
    temp = sorted(temp, key=lambda x: x[0])
    nx, ny = temp[0][1], temp[0][2]
    return [nx, ny, temp[0][3]]


def move_each(x, y, dirx, diry, before):
    # 현재꺼 확인
    now = graph[x][y]
    # 우선 그전꺼 세팅
    graph[x][y] = before
    santa[before] = [x, y]
    # 이제 지금꺼 한방향 이동 해야 한다
    zx = x + dirx
    zy = y + diry
    if not (0 <= zx < n and 0 <= zy < n):
        # 밖에 벗어났으면 죽어야하고
        santa_alive[now] = -1
    else:
        if graph[zx][zy] == -1:  # 움직였는데 빈공간 인경우
            santa[now] = [zx, zy]
            graph[zx][zy] = now
        elif graph[zx][zy] >= 1:
            # 이제 이동을 했는데 그렇게 산타와 겹친다면 상호 작용이 발생 하는 거임\
            move_each(zx, zy, dirx,diry,now)


def collision_rou_to_santa(nx, ny, dir):
    # 루돌프가 움직여서 온거임

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    now = graph[nx][ny]
    lx, ly = santa[now]
    scores[now] += C  # 산타는 c만큼의 점수를 얻게된다
    # 이제 산타 움직이면 된다
    zx = lx + dx[dir] * C
    zy = ly + dy[dir] * C
    gg=graph
    graph[lx][ly] = -1  # 빈공간으로 초기화
    if not (0 <= zx < n and 0 <= zy < n):
        # 밖에 벗어났으면 죽어야하고
        santa_alive[now] = -1
    else:
        santa_alive[now] = 2
        # 그게 아니라면
        if graph[zx][zy] == -1:  # 움직였는데 빈공간 인경우
            santa[now] = [zx, zy]
            graph[zx][zy] = now
        elif graph[zx][zy] >= 1:
            # 이제 이동을 했는데 그렇게 산타와 겹친다면 상호 작용이 발생 하는 거임\
            move_each(zx, zy, dx[dir], dy[dir], now)
            # 산타는 충돌 하게 되었으니 이제 기절 해야 한다


def collision_santa_to_rou(nx, ny, now, dir):  # 루돌프 있는 지점,

    # 이제 이동 할 거임
    # 산타가 움직여서 충돌 일어난 것인데, 산타는 d만큼 점수 얻게되고 반대 방향
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = (dir + 2) % 4

    # 산타 반대 방향으로 d 칸만큼 이동 해야함
    zx = nx + dx[dir] * D
    zy = ny + dy[dir] * D
    if not (0 <= zx < n and 0 <= zy < n):
        # 밖에 벗어났으면 죽어야하고
        santa_alive[now] = -1
    else:
        santa_alive[now] = 2
        # 그게 아니라면
        if graph[zx][zy] == -1:  # 움직였는데 빈공간 인경우
            santa[now] = [zx, zy]
            graph[zx][zy] = now
        elif graph[zx][zy] >= 1:
            # 이제 이동을 했는데 그렇게 산타와 겹친다면 상호 작용이 발생 하는 거임\
            move_each(zx, zy, dx[dir], dy[dir], now)
            # 산타는 충돌 하게 되었으니 이제 기절 해야 한다


def move_santa(now):
    # 탈락하지 않은 산타중 가장 가까운 산타 향해 1칸 돌진한다
    check = sys.maxsize
    nx, ny = santa[now][0], santa[now][1]
    total = []
    # 이제 루돌프에게 가장 가까워 지는 방향으로 이동 해야한다
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    lx, ly = -1, -1
    dir = -1
    now_value = (nx - roux) ** 2 + (ny - rouy) ** 2
    # 이제 찾았으니 4방향중 가장 가까워 지는 방향을 찾으면 된다
    # 가장 가까워 지는 칸을 찾아보자
    for i in range(4):
        zx = dx[i] + nx
        zy = dy[i] + ny
        if not (0 <= zx < n and 0 <= zy < n):
            continue
        if graph[zx][zy] >= 1:
            #if not(zx == roux and zy == rouy) :
            continue
        te = (zx - roux) ** 2 + (zy - rouy) ** 2
        if te >= now_value:
            continue
        if te < check:
            check = te
            lx = zx
            ly = zy
            dir = i

    if lx == -1 and ly == -1:
        # 움직일 수 없는 상태
        return
    # 이제 움직일건데
    graph[nx][ny] = -1

    # 루돌프 인경우
    if lx == roux and ly == rouy:
        # 산타가 루돌프에 충돌 때린 상황
        scores[now] += D
        collision_santa_to_rou(lx, ly, now, dir)
    else:
        # 빈칸인 경우
        if graph[lx][ly] == -1:
            graph[lx][ly] = now
            santa[now] = [lx, ly]

# for l in graph:
#     for j in l:
#         if j==-1:
#             print("0"+" ",end=" ")
#         else:
#             print(str(j)+" ",end=" ")
#     print()
for l in range(m):

    # 우선 루돌프 부터 움직임
    nx, ny, dir = move_roudol()
    # 이제 움직일텐데
    # 충돌이 일어날 수도 일어나지 않을수도있다
    roux = nx
    rouy = ny
    #print(l + 1, roux, rouy)
    if l == 6:
        l = 6

    if graph[nx][ny] >= 1:
        # 루돌프가 돌진한상태임
        collision_rou_to_santa(nx, ny, dir)

    # 그후 산타들 순차적 움직임
    for i in range(1, p + 1):
        if santa_alive[i] == -1 or santa_alive[i] >= 1:
            continue
        # 이제 움직일 수 있는 산타들 움직 여야함
        move_santa(i)

    cou = 0
    # 기절한얘들 감소 시켜 줘야 함
    for i in range(1, p + 1):
        if santa_alive[i] >= 1:
            santa_alive[i] -= 1
    for i in range(1, p + 1):
        if santa_alive[i] == -1:
            cou += 1
            continue
        scores[i] += 1
    #print(santa, santa_alive, scores)
    if cou == p:
        break
    # for l in graph:
    #     for j in l:
    #         if j==-1:
    #             print("0"+" ",end=" ")
    #         else:
    #             print(str(j)+" ",end=" ")
    #     print()
    # print()
print(*scores[1:])
