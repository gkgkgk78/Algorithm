import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())  # 지역번호 수색범위 거리의수

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a1, a2, a3 = map(int, input().split())
    graph[a1].append((a2, a3))  # 도착지 + 가중치
    graph[a2].append((a1, a3))



q=[]
dist=[sys.maxsize]*(n+1)
dist[1]=0
heapq.heappush(q,(0,1,-1,-1))#가중치 시작정점 a,b
answer=[]
while q:
    value,start,ca,cb=heapq.heappop(q)

    if dist[start]<value:
        continue
    if ca!=-1 and cb!=-1:

        answer.append((ca,cb))

    for vertex,vvalue in graph[start]:
        if dist[vertex]>value+vvalue:
            dist[vertex]=value+vvalue
            heapq.heappush(q,(dist[vertex],vertex,start,vertex))

print(len(answer))

for a1,a2 in answer:
    print(str(a1)+" "+str(a2))