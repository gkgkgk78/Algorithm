import sys
input = sys.stdin.readline

m, s = map(int, input().split())
fish = []

# 물고기와 상어 방향,  ←, ↖, ↑, ↗, →, ↘, ↓, ↙

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
shark_x = -1
shark_y = -1
graph = [[[] for _ in range(4)] for _ in range(4)]  # x,y,방향
smell = [[-1] * (4) for _ in range(4)]
for _ in range(m):
    e = list(map(int, input().split()))
    for k in range(len(e)):
        e[k] -= 1
    e = ["fish"] + e
    fish.append(e)
    graph[e[1]][e[2]].append(e)

shark_x, shark_y = map(int, input().split())
shark_x -= 1
shark_y -= 1


def copp():
    temp = []
    for i in range(4):
        for j in range(4):
            if len(graph[i][j]) == 0:
                continue
            for k in graph[i][j]:
                if k[0] != "fish":
                    continue
                temp.append(k)

    return temp


def move():
    temp_before = []  # 물고기가 동시에 움직여야 하니, 전에 물고기가 위치 했던 좌표 넣어둠
    # 물고기가 상어랑 같이 있을수 있으니 물고기에 해당되는 것만 제거를 하도록 해야함

    temp_next = []
    for i in range(4):
        for j in range(4):
            if len(graph[i][j]) == 0:
                continue
            for k in range(len(graph[i][j])):
                fish, x, y, dir = graph[i][j][k]
                if fish != "fish":
                    continue
                # 물고기 이니 이제 이동을 할수 있다는 것을 의미를 함.
                temp_before.append((i, j))

                # 상어가 있는칸, 물고기 냄새가 있는칸, 격자의 범위 벗어나는 칸으로 이동 불가
                temp_dir = dir
                temp_check = 0
                temp_x = -1
                temp_y = -1
                for _ in range(8):

                    zx = x + dx[temp_dir]
                    zy = y + dy[temp_dir]
                    t_check = 0
                    if 0 <= zx < 4 and 0 <= zy < 4:
                        if zx == shark_x and zy == shark_y:
                            t_check = 1
                        if smell[zx][zy] >= 0:
                            t_check = 1
                        if t_check == 0:
                            temp_x = zx
                            temp_y = zy
                            temp_check = 1
                            break
                    temp_dir -= 1
                    if temp_dir == -1:
                        temp_dir = 7
                if temp_check == 0:  # 못찾은 경우를 의미를 함
                    temp_next.append([fish, x, y, dir])  # 우선은 이렇게 해보자구,방향 바꿔야 할수도 있음
                else:
                    temp_next.append([fish, temp_x, temp_y, temp_dir])

    for a1, a2 in temp_before:
        graph[a1][a2] = []

    for e in temp_next:
        graph[e[1]][e[2]].append(e)


fin = []
isselected = [0] * (3)


def shark_total(cnt):
    global fin
    if cnt == 3:
        temp = []
        for k in isselected:
            temp.append(k)
        fin.append(temp)
        return

    for i in range(1, 5):
        isselected[cnt] = i
        shark_total(cnt + 1)


shark_total(0)


def move_shark(i1):
    global shark_x, shark_y
    # 이제 상어가 이동 할수 있는지를 파악을 해봐야 함
    fx = [-1, -1, 0, 1, 0]
    fy = [-1, 0, -1, 0, 1]
    q = []
    visit = [[0] * 4 for _ in range(4)]
    check = -sys.maxsize
    for i in range(len(fin)):
        e = fin[i]

        # 상어가 현재 칸에서 상하 좌우로 이동 할수 있는지 파악을 하도록 한다.
        zx = shark_x
        zy = shark_y
        e_count = 0
        fish_count = 0
        ttemp = []

        for l in range(3):
            dir = e[l]
            zx += fx[dir]
            zy += fy[dir]
            if 0 <= zx < 4 and 0 <= zy < 4:
                for s in graph[zx][zy]:
                    if s[0] == "fish" and visit[zx][zy] == 0:
                        fish_count += len(graph[zx][zy])
                        visit[zx][zy] = 1
                        ttemp.append((zx, zy))
                        break
            else:
                e_count = 1
                break
        for k1, k2 in ttemp:
            visit[k1][k2] = 0

        if e_count == 0:
            if fish_count > check:
                check = fish_count
                q = []
                q.append([-fish_count, i, zx, zy])

    ccount, key1, zx, zy = q[0]
    tx = shark_x
    ty = shark_y
    for i in fin[key1]:
        tx += fx[i]
        ty += fy[i]
        if len(graph[tx][ty]) != 0:
            graph[tx][ty] = []
            smell[tx][ty] = 2
    shark_x = zx
    shark_y = zy


def delete_smell():
    for i in range(4):
        for j in range(4):
            if smell[i][j] == 0:
                smell[i][j] = -1
            elif smell[i][j] >= 1:
                smell[i][j] -= 1


def copy_fish(t):
    for e in t:
        graph[e[1]][e[2]].append(e)


for i1 in range(s):
    temp_fish = []
    # 1. 모든 물고기에게 복제 마법을 시전을 한다.
    temp_fish = copp()

    # 이제 모든 물고기가 이동을 하도록 할거임

    move()

    # 이제 상어가 연속해서 3칸 이동을 할거임
    move_shark(i1)

    # 이제 두번 전 연습에서 생긴 물고기의 냄새를 제거 하도록 해야함

    delete_smell()

    copy_fish(temp_fish)

ans = 0
for i in range(4):
    for j in range(4):
        for e in graph[i][j]:
            if e[0] == "fish":
                ans += 1

print(ans)