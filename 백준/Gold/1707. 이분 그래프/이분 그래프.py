import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())


def bfs(vertex, check, graph, v):
    q = deque()
    visit = [0] * (v + 1)
    visit[vertex] = 1
    check[vertex] = 0
    q.append(vertex)
    while q:
        a1 = q.popleft()
        n1 = check[a1]
        tt = -1
        if n1 == 0:
            tt = 1
        else:
            tt = 0
        for t1 in graph[a1]:
            if visit[t1] == 0 and check[t1] == -1:
                visit[t1] = 1
                q.append(t1)
                check[t1] = tt


for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    nex = []
    for _ in range(e):
        a1, a2 = map(int, input().split())
        graph[a1].append(a2)
        graph[a2].append(a1)
        nex.append((a1, a2))
    check = [-1] * (v + 1)
    for i in range(1, v + 1):
        if check[i] != -1:
            continue
        bfs(i, check, graph, v)

    ans = "YES"
    for i in range(e):
        a1, a2 = nex[i]
        if check[a1] == check[a2]:
            ans = "NO"
            break
    print(ans)