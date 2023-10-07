import sys
import heapq

input = sys.stdin.readline

n, m, start, last, value = map(int, input().split())
graph = [[] for _ in range(n + 1)]
before = [[] for _ in range(n + 1)]

for _ in range(m):
    a1, a2, a3 = map(int, input().split())
    graph[a1].append((a2, a3))
    graph[a2].append((a1, a3))

distance = [sys.maxsize] * (n + 1)


def dijk(start, last):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        val, ver = heapq.heappop(q)
        if distance[ver] < val:
            continue
        for go, va in graph[ver]:
            if va + val <= value:
                if distance[go] > va + val:
                    distance[go] = va + val
                    before[go].append(ver)
                    if go != last:
                        heapq.heappush(q, (va + val, go))


dijk(start, last)
ans = sys.maxsize
kk = sys.maxsize


def dfs(be, next):
    global kk
    if be == start:
        return
    for a1, a2 in graph[be]:
        if a1 == next:
            kk = max(kk, a2)
            for j in before[a1]:
                dfs(a1, j)
            break

for i in before[last]:
    kk = -sys.maxsize
    dfs(last, i)
    ans = min(ans, kk)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)