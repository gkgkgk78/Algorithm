import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a1, a2 = map(int, input().split())
    graph[a1].append(a2)
    graph[a2].append(a1)


def bfs(i):
    q = deque()
    visit = [0] * (n + 1)
    visit[i] = 1
    ans = [-1] * (n + 1)
    q.append((i, 0))
    while q:
        ver, cou = q.popleft()
        ans[ver] = cou
        for k in graph[ver]:
            if visit[k] == 0:
                visit[k] = 1
                q.append((k, cou + 1))

    return ans


k = int(input().rstrip())
for _ in range(k):

    ans = [0]
    tt = 0
    a1, a2, a3 = map(int, input().split())
    if a1 == 1:
        graph[a2].append(a3)
        graph[a3].append(a2)
        aa = bfs(1)
    else:
        graph[a2].remove(a3)
        graph[a3].remove(a2)
        aa = bfs(1)

    print(*aa[1:])