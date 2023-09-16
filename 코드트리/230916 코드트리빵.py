#56분 걸림
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    e = list(map(int, input().split()))
    for j in range(n):
        if e[j] == 1:  # 베이스 캠프 지정해 주는 거임
            e[j] = 1
    graph.append(e)
people = [[[] for _ in range(n)] for _ in range(n)]
store = [-1]
for k in range(m):
    a1, a2 = map(int, input().split())
    store.append((a1 - 1, a2 - 1))

count = m
ans = 0
time = 1


def go_store(x, y, index):
    # 이제 최단 거리로 해서 움직 이고자 한다
    q = deque()
    visit = [[0] * (n) for _ in range(n)]
    right = [[[] for _ in range(n)] for _ in range(n)]
    visit[x][y] = 1
    lx, ly = store[index]
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    q.append((x, y))
    while q:
        a1, a2 = q.popleft()
        if a1 == lx and a2 == ly:
            break
        for i in range(4):
            zx = dx[i] + a1
            zy = dy[i] + a2
            if 0 <= zx < n and 0 <= zy < n and visit[zx][zy] == 0 and graph[zx][zy] != -1:
                q.append((zx, zy))
                visit[zx][zy] = 1
                right[zx][zy] = [a1, a2]

    # 이제 한칸 다음으로 이동 가능한거 찾기
    go = [(lx, ly)]
    while 1:

        go.append(right[lx][ly])
        lx, ly = right[lx][ly]
        if lx == x and ly == y:
            break
    return (go[-2])


def move_people(time):
    global ans, count
    last = []
    gogo = []
    t = store
    for i in range(n):
        for j in range(n):
            if len(people[i][j]) > 0:
                for i1 in people[i][j]:
                    # 이제 움직 여야 한다.
                    a1, a2 = go_store(i, j, i1)
                    # 이제 편의점에 도착 하게 되었다면
                    if (a1, a2) == store[i1]:
                        last.append((a1, a2))
                    else:
                        gogo.append((a1, a2, i1))
                people[i][j] = []

    for a1, a2 in last:
        graph[a1][a2] = -1
        ans += time
        count -= 1
    for a1, a2, a3 in gogo:
        people[a1][a2].append(a3)


def go_base(time):
    lx, ly = store[time]

    # 편의점과 가장 가까운 베이스 캠프에 가도록 하자
    q = deque()
    visit = [[0] * (n) for _ in range(n)]
    visit[lx][ly] = 1
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    temp = []
    q.append((lx, ly))
    while q:
        a1, a2 = q.popleft()
        for i in range(4):
            zx = dx[i] + a1
            zy = dy[i] + a2
            if 0 <= zx < n and 0 <= zy < n and visit[zx][zy] == 0 and graph[zx][zy] != -1:
                q.append((zx, zy))
                visit[zx][zy] = 1
                if graph[zx][zy] == 1:
                    temp.append((zx, zy))
        if len(temp) > 0:
            break
    # 이제 가장 가까운 베이스 캠프 하나 선정 하면된다
    temp = sorted(temp, key=lambda x: (x[0], x[1]))
    g1, g2 = temp[0]
    people[g1][g2].append(time)
    graph[g1][g2] = -1  # 이젠 다시 못가게 된다


while 1:

    # 이제 움직 이기 시작 한다
    move_people(time)
    # 이제 t<=m일시 편의점과 가장 가까운 베이스 캠프에 들어간다
    if time <= m:
        go_base(time)

    if count == 0:
        break
    time += 1
print(time)