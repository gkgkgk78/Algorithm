import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())  # 지역번호 수색범위 거리의수

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a1, a2, a3 = map(int, input().split())
    graph[a1].append((a2, a3))  # 도착지 + 가중치
    graph[a2].append((a1, a3))

dist = [sys.maxsize] * (n + 1)


def go(s1):
    q = []

    dist[s1] = 0
    heapq.heappush(q, (0, s1))  # 정점과 거리

    while q:
        distance, ver = heapq.heappop(q)
        if dist[ver] < distance:
            continue

        for a1, a2 in graph[ver]:
            if distance + a2 < dist[a1]:
                dist[a1] = distance + a2
                heapq.heappush(q, (dist[a1], a1))

go(1)
print(dist[n])