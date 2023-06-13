import sys
import heapq

input = sys.stdin.readline

n, m, r = map(int, input().split())  # 지역번호 수색범위 거리의수
vertex = list(map(int, input().split()))
vertex.insert(0, 0)

graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a1, a2, a3 = map(int, input().split())
    graph[a1].append((a2, a3))  # 도착지 + 가중치
    graph[a2].append((a1, a3))



answer = -sys.maxsize

for l in range(1, n + 1):  # 지정되는 각 정점에서 돌아가며 체크를 해보도록 하자
    dist = [sys.maxsize] * (n + 1)
    dist[l] = 0
    q = []
    heapq.heappush(q,(0, l))  # 정점과 거리

    while q:
        distance, ver = heapq.heappop(q)
        if dist[ver] < distance:
            continue

        for a1, a2 in graph[ver]:
            if distance + a2 < dist[a1]:
                dist[a1] = distance + a2
                heapq.heappush(q,(dist[a1],a1))
    temp = 0
    for k in range(1,n+1):
        if dist[k] <=m:
            temp += vertex[k]

    answer = max(answer, temp)

print(answer)