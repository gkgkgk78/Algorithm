import sys
from collections import deque
input=sys.stdin.readline


n,m=map(int,input().split())
graph=[]
sumz=0
for _ in range(n):
    e=list(map(int,input().rstrip()))
    graph.append(e)
    sumz+=sum(e)
visit=[[1]*m for _ in range(n)]
dx=[-1,-1,0]
dy=[-1,0,-1]
if sumz==0:
    ans=0
else:
    ans=1
for i in range(n):
    for j in range(m):
        if graph[i][j]!=0:
            temp=0
            total=[]
            for k in range(3):
                zx=dx[k]+i
                zy=dy[k]+j
                if not(0<=zx<n and 0<=zy<m):
                    temp=1
                    break
                total.append(graph[zx][zy])
            if temp==0:
                graph[i][j]=min(total)+1
                ans=max(ans,graph[i][j])
print(ans*ans)