import sys
import heapq
from collections import deque

input = sys.stdin.readline


def dijk(n, start, visit):
    q = []
    distance = [sys.maxsize] * (n + 1)
    heapq.heappush(q, ((0, start)))
    distance[start] = 0
    while q:
        value, vertex = heapq.heappop(q)
        if value > distance[vertex]:
            continue
        for ver, val in graph[vertex]:
            if visit[vertex][ver] == 1:
                continue
            if distance[ver] > val + value:
                distance[ver] = val + value
                heapq.heappush(q, (distance[ver], ver))

    return distance


def bfs(graphr, end, n1):
    q = deque()
    q.append((end))

    while q:
        first = q.popleft()
        for ver, val in graphr[first]:
            if n1[first] == n1[ver] + val and visit[ver][first]==0:
                visit[ver][first] = 1
                q.append(ver)


while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    start, end = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    graphr = [[] for _ in range(n + 1)]
    visit = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a1, a2, a3 = map(int, input().split())
        graph[a1].append((a2, a3))
        graphr[a2].append((a1, a3))

    n1 = dijk(n, start, visit)

    bfs(graphr, end, n1)
    n1 = dijk(n, start, visit)
    now1 = n1[end]  # 찾은 최초 최단 경로
    if now1 == sys.maxsize:
        print(-1)

    else:
        print(now1)