import sys,heapq
from collections import deque
input=sys.stdin.readline


n,m=map(int,input().split())

indegree=[0]*(n+1)
graph=[[]for _ in range(n+1)]

for _ in range(m):
    a1,a2=map(int,input().split())#a1이 먼저 a2가 후에 품
    graph[a1].append(a2)
    indegree[a2]+=1

q=[]
for i in range(1,n+1):
    if indegree[i]==0:
        heapq.heappush(q,i)

answer=deque()

while q:
    a1=heapq.heappop(q)
    answer.append(a1)
    for l in graph[a1]:
        indegree[l]-=1
        if indegree[l]==0:
            heapq.heappush(q,l)
print(*answer)