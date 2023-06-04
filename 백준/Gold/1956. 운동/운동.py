import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
graph=[[]for _ in  range(v+1)]
dist = [[sys.maxsize] * v for _ in range(v)]
q=[]
for _ in range(e):
    a1, a2, a3 = map(int, input().split())
    a1 -= 1
    a2 -= 1
    graph[a1].append((a2,a3))
    dist[a1][a2]=a3
    heapq.heappush(q,(a3,a1,a2))


while q:
    a1,a2,a3=heapq.heappop(q)
    if a2==a3:
        print(a1)
        exit(0)

    if dist[a2][a3]<a1:
        continue


    for t1,t2 in graph[a3]:
        if a1+t2<dist[a2][t1]:
            dist[a2][t1]=a1+t2
            heapq.heappush(q,(a1+t2,a2,t1))

print(-1)