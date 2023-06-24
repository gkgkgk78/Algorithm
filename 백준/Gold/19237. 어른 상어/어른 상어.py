import sys

input = sys.stdin.readline

# 향기를 나타내는 것은 상어의 번호도 같이 가지고 있어야 함
# 이동을 하려고 할시에 갈수 있는 칸이 여러개라면은 그때 우선순위가 작동 되는 것임

n, m, k_smell = map(int, input().split())  # k는 향기
shark = [[-1, -1, -1, -1]]  # 상어누군지, x,y,방향
smell_graph = [[[] for _ in range(n)] for _ in range(n)]  # 어떤 상어 건지, 지금 남은 카운트

for i in range(n):
    e = list(map(int, input().split()))
    for j in range(len(e)):
        if e[j] != 0:
            shark.append([e[j], i, j])
            smell_graph[i][j] = [e[j], k_smell]

# 위 아래 왼쪽 오른쪽
# 1,2,3,4
go = list(map(int, input().split()))
shark_count = m
shark = sorted(shark, key=lambda x: x[0])
for l in range(1, m + 1):
    shark[l].append(go[l - 1])
shark_prio = [[]]
for l in range(1, m + 1):
    temp = [[]]
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    shark_prio.append(temp)

for l in shark:
    l.pop(0)

time = 0

dx = [0, -1, 1, 0, 0]  # 위 아래 왼쪽 오른쪽
dy = [0, 0, 0, -1, 1]


def move(shark_vertex):
    x, y, dir = shark[shark_vertex]
    # 이제 상하 좌우로 모든 상어가 동시에 이동을 하고자 함
    # 그렇게 하고 난후에 자신의 냄새를 그칸에 뿌림

    nextx = -1
    nexty = -1
    next_dir = -1
    can_next = -1
    # 우선 인접한 칸중 아무 냄새가 없는 칸이 있는지 확인
    around = []
    for i in range(1, 5):
        zx = x + dx[i]
        zy = y + dy[i]

        if 0 <= zx < n and 0 <= zy < n:
            if len(smell_graph[zx][zy]) == 0:
                around.append((zx, zy))
                can_next = i
    # 칸이 존재 한다면 그리고 여러개라면 우선 순위 정함
    if len(around) > 0:
        if len(around) >= 2:
            # 우선 순위에 따라 정해야 함
            check_go = shark_prio[shark_vertex][dir]
            for l in range(4):
                fx = x + dx[check_go[l]]
                fy = y + dy[check_go[l]]
                if (fx, fy) in around:
                    nextx, nexty = fx, fy
                    next_dir = check_go[l]
                    break

        else:
            nextx, nexty = around[0]
            next_dir = can_next

    else:
        # 인접한 칸이 없다면, 자신의 냄새가 있는 칸을 정함
        for i in range(1, 5):
            zx = x + dx[i]
            zy = y + dy[i]

            if 0 <= zx < n and 0 <= zy < n:
                if len(smell_graph[zx][zy]) != 0:
                    smell_who, smell_count = smell_graph[zx][zy]
                    if smell_who == shark_vertex:
                        around.append((zx, zy))
                        can_next = i
        if len(around) >= 2:
            check_go = shark_prio[shark_vertex][dir]
            for l in range(4):
                fx = x + dx[check_go[l]]
                fy = y + dy[check_go[l]]
                if (fx, fy) in around:
                    nextx, nexty = fx, fy
                    next_dir = check_go[l]
                    break
        else:

            nextx, nexty = around[0]
            next_dir = can_next
    shark[shark_vertex] = [nextx, nexty, next_dir]


while 1:

    for l in range(1, m + 1):
        if len(shark[l]) == 0:
            continue
        move(l)

    # 향기 제거 작업
    for i in range(n):
        for j in range(n):
            if len(smell_graph[i][j]) > 0:
                if smell_graph[i][j][1] <= 1:
                    smell_graph[i][j] = []
                else:
                    smell_graph[i][j][1] -= 1

    # 향기 배치 시작
    for l in range(1, m + 1):

        if len(shark[l]) == 0:
            continue
        nx, ny, dir = shark[l]
        for kk in range(l + 1, m + 1):

            if len(shark[kk]) == 0:
                continue
            nowx, nowy, nowdir = shark[kk]
            # 만약 그렇지 않다면 향기 그래프 에도 추가를 해주고, 상어의 위치 방향을 변경 해 주면 된다
            if nowx == nx and nowy == ny:
                shark[kk] = []
                shark_count -= 1

    for l in range(1, m + 1):

        if len(shark[l]) == 0:
            continue
        nx, ny, dir = shark[l]
        smell_graph[nx][ny] = [l, k_smell]

    time += 1
    # 상어 가운트가 1이 되면은 넘추면 됨
    if shark_count == 1:
        break
    if time > 1000:
        break

if time <= 1000:
    print(time)
else:
    print(-1)