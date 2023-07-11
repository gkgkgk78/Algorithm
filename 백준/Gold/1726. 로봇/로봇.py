import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def di(s):
    if s == 1:
        return 0
    elif s == 2:
        return 2
    elif s == 3:
        return 1
    else:
        return 3


graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

sx, sy, sdir = map(int, input().split())
fx, fy, fdir = map(int, input().split())
sx -= 1
sy -= 1
sdir = di(sdir)
fx -= 1
fy -= 1
fdir = di(fdir)

ans = sys.maxsize


# 원하는 방향으로 바라보도록 하는데 최소 몇번의 명령이 필요한지 구하도록 하라


def rotate(dir):
    if dir == 0:
        return [1, 3]
    elif dir == 1:
        return [0, 2]
    elif dir == 2:
        return [1, 3]
    elif dir == 3:
        return [0, 2]


def ranged(x, y):
    if 0 <= x < n and 0 <= y < m:
        return 1
    return 0


def roro(a, f):
    co = 0
    t = a
    if a==f:
        return 0
    for i in range(3):
        co += 1
        t = (t + 1) % 4
        if t == f:
            break
    co1 = 0
    t = a
    for i in range(3):
        co1 += 1
        t-=1
        if t<0:
            t=3
        if t == f:
            break
    return min(co, co1)


# 이건 dfs로 해서 가야 겠는데
def bfs(graph, visit, x, y, dir, count):
    global ans
    q = deque()
    visit[x][y][dir] = 0
    q.append((x, y, dir, count))
    while q:
        x, y, dirs, count = q.popleft()
        if x == fx and y == fy:
            n_count = roro(dirs, fdir) + count
            ans = min(ans, n_count)
            continue
        temp = rotate(dirs)
        for a1 in temp:
            if visit[x][y][a1] == 0:
                visit[x][y][a1] = 1
                q.append((x, y, a1, count + 1))
        next = [dirs]
        for i in next:
            dirz = i
            # 가는 방향 유지
            # 이대로 쭉 가보자고
            for j in range(1, 4):
                zx = x + dx[dirz] * j
                zy = y + dy[dirz] * j
                if ranged(zx, zy) == 0 or graph[zx][zy] == 1:
                    break
                if visit[zx][zy][dirz] == 0:
                    visit[zx][zy][dirz] = 1

                    q.append((zx, zy, dirz, count + 1))


visit = [[[0] * (4) for _ in range(m)] for _ in range(n)]
bfs(graph, visit, sx, sy, sdir, 0)
print(ans)