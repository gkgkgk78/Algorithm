import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a1, a2, a3 = map(int, input().split())
    graph[a1].append((a2, a3))

# n명의 학생중 가장 오래걸리는 학생의 소요 시간을 구하자

INF = sys.maxsize


def dijk(start):
    distance = [INF] * (n + 1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        val, ver = heapq.heappop(q)
        if distance[ver] < val:
            continue

        for vertex, value in graph[ver]:
            next = value + val
            if distance[vertex] > next:
                distance[vertex] = next
                heapq.heappush(q, (next, vertex))
    return distance

a2 = dijk(x)
ans = -sys.maxsize
for i in range(1, n + 1):
    a1 = dijk(i)
    ne = a1[x] + a2[i]
    ans = max(ans, ne)
print(ans)