import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())  # 지역번호 수색범위 거리의수

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a1, a2, a3 = map(int, input().split())
    graph[a1].append((a2, a3))  # 도착지 + 가중치
    graph[a2].append((a1, a3))

l1, l2 = map(int, input().split())


def go(s1):
    q = []
    dist = [sys.maxsize] * (n + 1)
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

    return dist


first = go(1)
v1 = go(l1)
v2 = go(l2)

now1 = first[l1] + v1[l2] + v2[n]
now2 = first[l2] + v2[l1] + v1[n]

if now1 < sys.maxsize or now2 < sys.maxsize:
    print(min(now1, now2))
else:
    print(-1)