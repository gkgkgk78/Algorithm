import sys
from collections import deque
import heapq

input = sys.stdin.readline


n,m=map(int,input().split())


distance=[sys.maxsize]*(n)
wall=list(map(int,input().split()))
wall[-1]=0
for i in range(1,len(wall)-1):
    if wall[i]==1:
        distance[i]=-1
graph=[[]for _ in range(n)]

q=[]
for i in range(m):
    a1,a2,a3=map(int,input().split())
    graph[a1].append([a2,a3])
    graph[a2].append([a1,a3])

distance[0]=0
heapq.heappush(q,[0,0])

while q:
    value,vertex=heapq.heappop(q)
    if distance[vertex]<value:
        continue

    for ver,val in graph[vertex]:
        temp=val+value
        if distance[ver] > temp and wall[ver]==0:
            heapq.heappush(q,[temp,ver])
            distance[ver]=temp


if distance[-1]!=sys.maxsize:
    print(distance[-1])
else:
    print(-1)