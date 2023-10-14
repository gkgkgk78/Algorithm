import sys
import heapq

input = sys.stdin.readline

v, e, p = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a1,a2,a3=map(int,input().split())
    graph[a1].append((a2,a3))
    graph[a2].append((a1,a3))


#이제 1에서 시작해서 마지막 까지 가는거 가야 함

def dijk(start,last):
    q=[]
    distance=[sys.maxsize]*(v+1)
    distance[start]=0
    heapq.heappush(q,(start,0))
    while q:
        vertex,value=heapq.heappop(q)
        if distance[vertex]>value:
            continue
        for ver,val in graph[vertex]:
            nex=val+value
            if distance[ver]>nex:
                distance[ver]=nex
                heapq.heappush(q, (ver, nex))

    return distance[last]



a1=dijk(1,v)
a2=dijk(1,p)
a3=dijk(p,v)

if a1==a2+a3:
    print("SAVE HIM")
else:
    print("GOOD BYE")