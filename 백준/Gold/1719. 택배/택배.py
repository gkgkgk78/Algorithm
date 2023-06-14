import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())  # 지역번호 수색범위 거리의수

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a1, a2, a3 = map(int, input().split())
    graph[a1].append((a2, a3))  # 도착지 + 가중치
    graph[a2].append((a1, a3))


def go(s1):
    q = []
    dist = [sys.maxsize] * (n + 1)
    dist[s1] = 0
    last = [0] * (n + 1)
    for k in range(1, n + 1):
        last[k] = k
    heapq.heappush(q, (0, s1, -1))  # 정점과 거리

    while q:
        distance, ver, start = heapq.heappop(q)
        if dist[ver] < distance:
            continue
        last[ver] = start
        for a1, a2 in graph[ver]:
            if distance + a2 < dist[a1]:
                dist[a1] = distance + a2
                if ver == s1:
                    heapq.heappush(q, (dist[a1], a1, a1))
                else:
                    heapq.heappush(q, (dist[a1], a1, start))
    for i in range(1, n + 1):
        if i == s1:
            print("-", end=" ")
        else:
            print(last[i], end=" ")
    print()


for i in range(1, n + 1):
    go(i)