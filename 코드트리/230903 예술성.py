# 50분
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n = int(input().rstrip())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

ans = 0


def find(x, y, visit, co):
    q = deque()
    visit[x][y] = co
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    count = 1
    now = graph[x][y]
    q.append((x, y))
    while q:
        a1, a2 = q.popleft()
        for i in range(4):
            zx = a1 + dx[i]
            zy = a2 + dy[i]
            if 0 <= zx < n and 0 <= zy < n:
                if graph[zx][zy] == now and visit[zx][zy] == 0:
                    visit[zx][zy] = co
                    count += 1
                    q.append((zx, zy))

    return count


def flower(v1, v2, group_vertex, group_count, visit):
    global ans
    # 이제 두개의 정점을 통하여서 맞닿은 변의 수를 구하도록 하자
    visit1 = [[0] * (n) for _ in range(n)]
    h1, h2 = group_vertex[v1]
    visit1[h1][h2] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((h1, h2))
    anan = 0
    while q:
        a1, a2 = q.popleft()
        for i in range(4):
            zx = a1 + dx[i]
            zy = a2 + dy[i]
            if 0 <= zx < n and 0 <= zy < n:
                if visit[zx][zy] == v1 and visit1[zx][zy] == 0:
                    visit1[zx][zy] = 1
                    q.append((zx, zy))
                if visit[zx][zy] == v2:
                    anan += 1

    if anan != 0:
        u1, u2 = group_vertex[v1]
        f1, f2 = group_vertex[v2]
        last = (group_count[v1] + group_count[v2]) * graph[u1][u2] * graph[f1][f2] * anan
        ans += last


def rotate_sqare(x, y, ne, temp):
    before = [[0] * (ne) for _ in range(ne)]
    next = [[0] * (ne) for _ in range(ne)]
    a1 = 0
    a2 = 0
    for i in range(x, x + ne):
        for j in range(y, y + ne):
            before[a1][a2] = graph[i][j]
            a2 += 1
        a1 += 1
        a2 = 0
    # 이제 회전 시켜보자
    for i in range(ne):
        for j in range(ne):
            next[i][j] = before[ne - j - 1][i]

    a1 = 0
    a2 = 0
    for i in range(x, x + ne):
        for j in range(y, y + ne):
            temp[i][j] = next[a1][a2]
            a2 += 1
        a1 += 1
        a2 = 0


def triple(be, ne, temp, l, dir):
    bx, by = be
    nx, ny = ne

    for i in range(l):
        temp[nx][ny] = graph[bx][by]
        if dir == 0:
            bx -= 1
            ny -= 1
        elif dir == 1:
            by -= 1
            nx += 1
        elif dir == 2:
            bx += 1
            ny += 1
        else:
            by += 1
            nx -= 1


for _ in range(4):
    visit = [[0] * (n) for _ in range(n)]
    group = []
    group_vertex = [[]]  # 해당 되는 그룹의 정점 하나
    group_count = [0]  # 해당 그룹의 속한 칸 개수
    co = 1
    # 그룹 분리
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                e1 = find(i, j, visit, co)
                group_count.append(e1)
                group_vertex.append([i, j])
                group.append(co)
                co += 1

    # 나눈 그룹에 대해서 조화 로움 찾아야 함
    ok = list(combinations(group, 2))

    # 이제 시작을 하도록 해보자
    for a1, a2 in ok:
        flower(a1, a2, group_vertex, group_count, visit)

    temp = [[0] * (n) for _ in range(n)]
    # 회전 하기

    # 각 4개의 정사각형을 회전 시키면 된
    ne = (n - 1) // 2
    pe = [(0, 0), (0, ne + 1), (ne + 1, 0), (ne + 1, ne + 1)]
    for a1, a2 in pe:
        rotate_sqare(a1, a2, ne, temp)

    # 십자 모양의 경우의 회전과
    pe = [(ne - 1, ne), (ne, ne - 1), (ne + 1, ne), (ne, ne + 1)]
    for i in range(4):
        be = pe[i]
        nel = []
        if i == 3:
            nel = pe[0]
        else:
            nel = pe[i + 1]
        triple(be, nel, temp, ne, i)
    temp[ne][ne] = graph[ne][ne]
    graph = temp

print(ans)