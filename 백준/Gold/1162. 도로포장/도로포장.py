import sys
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a1, a2, a3 = map(int, input().split())
    graph[a1].append((a2, a3))
    graph[a2].append((a1, a3))

# n명의 학생중 가장 오래걸리는 학생의 소요 시간을 구하자

INF = sys.maxsize


def dijk(start):
    distance = [[INF for _ in range(k + 1)] for _ in range(n + 1)]

    distance[start][0] = 0

    q = []
    heapq.heappush(q, (0, 0, start))  # 가중치, 사용한 포장 개수, 정점

    while q:
        val, delete, ver = heapq.heappop(q)
        if distance[ver][delete] < val:
            continue
        for vertex, value in graph[ver]:
            next = value + val
            if distance[vertex][delete] > next:
                distance[vertex][delete] = next
                heapq.heappush(q, (next, delete, vertex))
            if delete + 1 <= k:
                if distance[vertex][delete + 1] > val:
                    distance[vertex][delete + 1] = val
                    heapq.heappush(q, (val, delete + 1, vertex))

    return distance


ans = sys.maxsize
a1 = dijk(1)
for i in range(k + 1):
    ans = min(ans, a1[n][i])
print(ans)