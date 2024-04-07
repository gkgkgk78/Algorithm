import sys
from collections import deque
import heapq

input = sys.stdin.readline

# 1시간 30분 걸림
l, n, q = map(int, input().split())

bomb_graph = []
player_graph = [[0] * (l) for _ in range(l)]
answer = [0] * (n + 1)
player_list = [[]]
for _ in range(l):
    e = list(map(int, input().split()))
    bomb_graph.append(e)


def del_draw_player(x, y, h, w, now):
    # 그림 지우기
    tt = player_graph
    for i in range(x, x + h):
        for j in range(y, y + w):
            # if (0 <= i < l and 0 <= j < l):  # 방패는 해당 안된다고 파악함
            if player_graph[i][j] == now:
                player_graph[i][j] = 0


def draw_player(x, y, h, w, now):
    # 그림 칠하기
    for i in range(x, x + h):
        for j in range(y, y + w):
            # if (0 <= i < l and 0 <= j < l):  # 방패는 해당 안된다고 파악함
            player_graph[i][j] = now


for i in range(n):
    r, c, h, w, k = map(int, input().split())
    # h:세로 길이 w: 가로 길이
    r -= 1
    c -= 1
    player_list.append([r, c, h, w, k])
    # 이제 색깔 칠해야 함
    draw_player(r, c, h, w, i + 1)


def can_move(x, y, dir):
    q = deque()
    visit = [[0] * (l) for _ in range(l)]
    visit[x][y] = 1
    # 해당 되는 방향으로 모두 이동이 되어야 한다
    visit_player = [0] * (n + 1)
    visit_player[player_graph[x][y]] = 1  # 해당 되는 player는 방문을 했다
    q.append((player_graph[x][y]))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        now = q.popleft()
        r, c, h, w, k = player_list[now]  # 이렇게 해서 해당 되는 플레이어를 얻어오고
        # 이제 이동을 해야 한다
        r += dx[dir]
        c += dy[dir]
        if 0 <= r < l and 0 <= c < l:
            # 그럼 이제 해당 되는 방향으로 탐색을 해보도록 하자
            for i in range(r, r + h):
                for j in range(c, c + w):
                    if (0 <= i < l and 0 <= j < l):
                        # 해당 되는 범위 안에서만 탐색을 하고자 한다
                        if bomb_graph[i][j] == 2:
                            return 0
                        if player_graph[i][j] != 0 and visit_player[player_graph[i][j]] == 0:
                            visit_player[player_graph[i][j]] = 1
                            q.append(player_graph[i][j])
                    else:
                        return 0
        else:
            return 0
    return 1


def go_game(x, y, dir):
    q = deque()
    visit = [[0] * (l) for _ in range(l)]
    visit[x][y] = 1
    # 해당 되는 방향으로 모두 이동이 되어야 한다
    visit_player = [0] * (n + 1)
    visit_player[player_graph[x][y]] = 1  # 해당 되는 player는 방문을 했다
    q.append((player_graph[x][y]))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    start = player_graph[x][y]
    while q:
        now = q.popleft()
        r, c, h, w, k = player_list[now]  # 이렇게 해서 해당 되는 플레이어를 얻어오고
        r1, c1 = r, c
        # 이제 이동을 해야 한다
        r1 += dx[dir]
        c1 += dy[dir]
        # 그럼 이제 해당 되는 방향으로 탐색을 해보도록 하자
        check = 0
        for i in range(r1, r1 + h):
            for j in range(c1, c1 + w):
                if player_graph[i][j] != 0 and visit_player[player_graph[i][j]] == 0:
                    visit_player[player_graph[i][j]] = 1
                    q.append(player_graph[i][j])
                if bomb_graph[i][j] == 1:
                    check += 1
        del_draw_player(r, c, h, w, now)
        r, c = r1, c1
        draw_player(r, c, h, w, now)
        if now != start:
            k -= check
            answer[now] += check
        if k > 0:
            player_list[now] = [r, c, h, w, k]
        else:
            player_list[now] = []
            del_draw_player(r, c, h, w, now)


def game(num, to):
    # 기사 번호, 어느 방향으로 갈지
    # 0 1 2 3 위 오른 아래 왼쪽방향으로 한칸 이동 하면됨

    # 우선 이동 가능한지 파악을 해야 한다
    now = player_list[num]
    r, c, h, w, k = now
    check1 = can_move(r, c, to)

    if check1 == 1:
        go_game(r, c, to)


for _ in range(q):
    num, to = map(int, input().split())

    le = len(player_list[num])
    if le == 0:
        continue
    game(num, to)

ans = 0
for i in range(1, len(player_list)):
    if len(player_list[i]) > 0:
        ans += answer[i]
print(ans)