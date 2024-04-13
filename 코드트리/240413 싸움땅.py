
#40분
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
players = []
players_gun = [0] * (m)  # 플레이어 들이 들고 있는 총을 의미함
guns = [[[] for _ in range(n)] for _ in range(n)]  # 총들이 위치 하고 있는 그래프
graph = [[-1]*(n) for _ in range(n)]  # 실제 플레이어가 위치 하고 있는 그래프
points = [0] * (m)

for i in range(n):
    e = list(map(int, input().split()))
    for j in range(n):
        if e[j] != 0:
            guns[i][j].append(e[j])
for i in range(m):
    x, y, d, s = map(int, input().split())
    players.append([x - 1, y - 1, d, s])
    graph[x - 1][y - 1]=i

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def move_loser(ind):
    x, y, dir, s = players[ind]
    zx = x + dx[dir]
    zy = y + dy[dir]
    graph[x][y]=-1
    if not (0 <= zx < n and 0 <= zy < n) or (graph[zx][zy]) !=-1:
        for i in range(3):
            dir = (dir + 1) % 4
            zx = x + dx[dir]
            zy = y + dy[dir]
            if 0 <= zx < n and 0 <= zy < n and (graph[zx][zy]) == -1:
                break
    # 이제 갈 방향 및 위치를 구했다

    if len(guns[zx][zy]) > 0:
        # 총이 있는 경우
        temp = guns[zx][zy]
        if players_gun[ind] != 0:
            temp.append(players_gun[ind])
        temp.sort(reverse=True)
        players_gun[ind] = temp[0]
        guns[zx][zy] = temp[1:]

    players[ind] = [zx, zy, dir, s]
    graph[zx][zy]=ind


def get_gun_winner(ind):
    x, y, dir, s = players[ind]
    temp = guns[x][y]
    if players_gun[ind] != 0:
        temp.append(players_gun[ind])
    temp.sort(reverse=True)
    players_gun[ind] = temp[0]
    guns[x][y] = temp[1:]
    graph[x][y]=ind


def move(ind):
    # 이제 순차적으로 이동을 해보도록 하자
    x, y, dir, s = players[ind]
    zx = x + dx[dir]
    zy = y + dy[dir]
    graph[x][y]=-1
    if not (0 <= zx < n and 0 <= zy < n):
        dir = (dir + 2) % 4
        zx = x + dx[dir]
        zy = y + dy[dir]
    # 이제 갈 방향 및 위치를 구했다
    if (graph[zx][zy]) == -1:
        # 플레이어가 없다면
        if len(guns[zx][zy]) > 0:
            # 총이 있는 경우
            temp = guns[zx][zy]
            if players_gun[ind] != 0:
                temp.append(players_gun[ind])
            temp.sort(reverse=True)
            players_gun[ind] = temp[0]
            guns[zx][zy] = temp[1:]
        players[ind] = [zx, zy, dir, s]
        graph[zx][zy]=ind
    else:
        players[ind] = [zx, zy, dir, s]
        # 플레이어가 있는 경우 이제 두 플레이어가 싸워야 한다
        second = graph[zx][zy]  # 이동한 방향에 있는 플레이어
        sx, sy, sdir, ss = players[second]
        winner = -1
        loser = -1
        # 이제 누가 더 큰지를 비교 해야 한다
        temp_one = s + players_gun[ind]
        temp_two = ss + players_gun[second]
        if temp_one > temp_two:
            winner = ind
            loser = second
        elif temp_one < temp_two:
            winner = second
            loser = ind
        else:
            if s > ss:
                winner = ind
                loser = second
            else:
                winner = second
                loser = ind
        # 이렇게 해서 승자 패자 다 정해짐
        points[winner] += abs(temp_two - temp_one)

        # 우선 진 사람이 총 내려놓고 이동하는거
        guns[sx][sy].append(players_gun[loser])
        players_gun[loser] = 0

        # 이제 이동을 해야 한다
        move_loser(loser)

        # 이긴 사람은 진 사람이 내려놓은 총 중 가장 높은거 획득
        get_gun_winner(winner)


for _ in range(k):
    for i in range(m):
        move(i)

print(*points)
