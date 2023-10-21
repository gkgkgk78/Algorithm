import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
jew = dict()
ind = 0
for _ in range(k):
    i = int(input().rstrip())
    jew[i] = ind
    ind += 1

for _ in range(m):
    a1, a2, a3 = map(int, input().split())
    graph[a1].append((a2, a3))
    graph[a2].append((a1, a3))

visit = [[0] * (1 << 14) for _ in range(n + 1)]

ans = -1


def bfs():
    global ans
    q = deque()
    visit[1][0] = 1
    q.append((1, 0, 0))  # 방문 한거임
    if 1 in jew:
        a = jew[1]
        visit[1][1 << a] = 1
        q.append((1, 1, 1 << a))
    while q:
        a1, a2, cou = q.popleft()
        if a1 == 1:
            ans = max(ans, a2)
        for ver, val in graph[a1]:
            # 보석이 있다면
            if ver in jew:
                now = jew[ver]
                co = a2
                if (cou >> now) & (1) == 0:
                    co += 1
                nex = (1 << now) | cou
                if a2 <= val and visit[ver][nex] == 0:
                    visit[ver][nex] = 1
                    q.append((ver, co, nex))
            if a2 <= val and visit[ver][cou] == 0:
                visit[ver][cou] = 1
                q.append((ver, a2, cou))

bfs()
print(ans)