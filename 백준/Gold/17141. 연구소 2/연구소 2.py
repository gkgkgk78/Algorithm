import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
total = []
wall_count = 0
for i in range(n):
    e = list(map(int, input().split()))
    for j in range(n):
        if e[j] == 2:
            total.append((i, j))
            e[j] = 0
    t = e.count(1)
    wall_count += t
    graph.append(e)

isselected = [0] * (m)
visit = [0] * (len(total))

ans = sys.maxsize


def bfs(no):
    global ans
    q = deque()
    visit1 = [[0] * (n) for _ in range(n)]
    nnow = n * n - wall_count
    for a1 in no:
        n1, n2 = total[a1]
        q.append((n1, n2))
        visit1[n1][n2] = 1
        nnow -= 1
    time = 0
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    while q:
        tempq = deque()
        while q:
            a1, a2 = q.popleft()
            for i in range(4):
                zx = a1 + dx[i]
                zy = a2 + dy[i]
                if 0 <= zx < n and 0 <= zy < n:
                    if visit1[zx][zy] == 0 and graph[zx][zy] != 1:
                        tempq.append((zx, zy))
                        visit1[zx][zy] = 1
                        nnow -= 1
        q = tempq
        time += 1
        if time>ans:
            return 
    if nnow == 0:
        ans = min(ans, time)


def comb(start, cnt, end):
    if cnt == m:
        bfs(isselected)
        return

    for i in range(start, end):
        if visit[i] == 1:
            continue
        isselected[cnt] = i
        comb(i + 1, cnt + 1, end)
        visit[i] = 0


comb(0, 0, len(total))
if ans == sys.maxsize:
    print(-1)
else:
    print(ans - 1)