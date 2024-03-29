import sys
import heapq

input = sys.stdin.readline

n, m, start, last, value = map(int, input().split())
graph = [[] for _ in range(n + 1)]

right=-1
for _ in range(m):
    a1, a2, a3 = map(int, input().split())
    right=max(right,a3)
    graph[a1].append((a2, a3))
    graph[a2].append((a1, a3))




def dijk(start, last, tt):

    q = []
    distance = [sys.maxsize] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        val, ver = heapq.heappop(q)
        if distance[ver] < val:
            continue
        for go, va in graph[ver]:
            if va > tt:
                continue
            if va + val <= value:
                if distance[go] > va + val:
                    distance[go] = va + val
                    if go != last:
                        heapq.heappush(q, (va + val, go))

    return distance[last]


left = 0
right+=1
ans = sys.maxsize
while left + 1 < right:

    mid = (left + right) // 2
    aa = dijk(start, last, mid)
    if aa <= value:
        right = mid
        ans = min(ans, mid)
    else:
        left = mid

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)