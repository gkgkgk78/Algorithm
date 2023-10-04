import sys
from collections import deque

input = sys.stdin.readline
t = int(input().rstrip())


def bfs(graph, go, m):
    # go는 순서를 의미 한다
    q = deque()

    for i in range(1, m + 1):
        e = go[i]
        if e[0] == 1:
            inin[i] = 0
            q.append(i)
    temp = deque()
    while 1:
        if len(q) == 0:
            break

        while q:
            a1 = q.popleft()
            if go[a1][1] >= 2:
                go[a1][0] += 1
            before = go[a1][0]
            for i in graph[a1]:
                if go[i][0] < before:
                    go[i] = [before, 1]
                elif go[i][0] == before:
                    go[i][1] += 1
                inin[i] -= 1
                if inin[i] == 0:
                    temp.append(i)

        while temp:
            q.append(temp.popleft())


for _ in range(t):
    k, m, p = map(int, input().split())
    graph = [[] for _ in range(m + 1)]
    inin = [0] * (m + 1)
    for i in range(p):
        a1, a2 = map(int, input().split())
        inin[a2] += 1
        graph[a1].append(a2)
    go = [[0, 0] for _ in range(m + 1)]
    for i in range(1, m + 1):
        if inin[i] == 0:
            go[i] = [1, 1]
    bfs(graph, go, m)

    #go = sorted(go, key=lambda x: -x[0])
    #print(go)
    print(k, go[m][0])