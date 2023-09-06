import sys
import heapq
input = sys.stdin.readline

n,m,k=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a1,a2,a3=map(int,input().split())
    graph[a2].append((a1,a3))
distance=[sys.maxsize]*(n+1)

e=list(map(int,input().split()))


def dijk():
    q=[]
    for i in e:
        distance[i]=0
        for a1,a2 in graph[i]:
            if a2<distance[a1]:
                distance[a1]=a2
                heapq.heappush(q,(a1,a2))
    while q:
        vertex,dis=heapq.heappop(q)
        if distance[vertex]<dis:
            continue
        for a1,a2 in graph[vertex]:
            if a2+dis<distance[a1]:
                distance[a1]=a2+dis
                heapq.heappush(q,(a1,a2+dis))

dijk()
ans=-sys.maxsize
index=-1
for i in range(1,n+1):
    if distance[i]==sys.maxsize:
        continue
    if distance[i]>ans:
        ans=distance[i]
        index=i
print(index)
print(ans)