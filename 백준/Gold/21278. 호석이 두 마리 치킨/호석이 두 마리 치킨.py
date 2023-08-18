import sys
from itertools import combinations

input = sys.stdin.readline

from collections import deque

n,m=map(int,input().split())

graph=[[]for _ in range(n+1)]

total=[]

for i in range(1,n+1):
    total.append(i)
nex=list(combinations(total,2))

for _ in range(m):
    a1,a2=map(int,input().split())
    graph[a1].append(a2)
    graph[a2].append(a1)

ans=sys.maxsize
index=0
def bfs(start):
    q=deque()
    visit=[0]*(n+1)
    for i in start:
        visit[i]=-1
        q.append((i,0))
    while q:
        a1,now=q.popleft()
        for i in graph[a1]:
            if visit[i]==0:
                visit[i]=now+1
                q.append((i,now+1))
    return sum(visit)*2+4

for i in range(len(nex)):
    a1,a2=nex[i]
    tt=[a1,a2]
    a2=bfs(tt)
    if a2<ans:
        ans=a2
        index=i

print(nex[index][0],nex[index][1],ans)