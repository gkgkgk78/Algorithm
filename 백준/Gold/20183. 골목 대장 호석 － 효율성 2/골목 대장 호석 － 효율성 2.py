import sys
from collections import deque
import heapq
input = sys.stdin.readline

n,m,a,b,c=map(int,input().split())

graph=[[]for _ in range(n+1)]
left=0
right=-1
for _ in range(m):
    a1,a2,a3=map(int,input().split())
    graph[a1].append((a2,a3))
    graph[a2].append((a1,a3))
    right=max(right,a3)
right+=1

def bfs(mid):
    distance=[sys.maxsize]*(n+1)
    q=[]
    heapq.heappush(q,(0,a))
    distance[a]=0
    while q:
        value,vertex=heapq.heappop(q)
        if distance[vertex]<value:
            continue
        for a1,a2 in graph[vertex]:
            if a2>mid:
                continue
            nex=a2+value
            if nex<=c:
                if distance[a1]>nex:
                    distance[a1]=nex
                    heapq.heappush(q,(nex,a1))

    if distance[b]<=c:
        return 1
    else:
        return 0


ans=sys.maxsize
while left+1<right:
    mid=(left+right)//2
    a1=bfs(mid)
    if a1==1:
        right=mid
        ans=min(ans,right)
    else:
        left=mid
if ans==sys.maxsize:
    print(-1)
else:
    print(ans)