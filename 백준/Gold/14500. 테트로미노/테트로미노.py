import sys, copy
import heapq
from itertools import combinations
from collections import deque
input = sys.stdin.readline
n,m=map(int,input().split())
array=[list(map(int,input().split())) for _ in range(n)]
ans=0
gr=[[1]*m for _ in range(n)]
def dfs(x,y,now,cnt):
    global ans
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    if cnt==4:
        if now>ans:
            ans=now
        return
    for i in range(4):
        zx=dx[i]+x
        zy=dy[i]+y
        if 0<=zx<n and 0<=zy<m:
            if gr[zx][zy]==1:
                gr[zx][zy]=0
                dfs(zx,zy,now+array[zx][zy],cnt+1)
                gr[zx][zy] = 1
def gdfs(x,y):
    go=array[x][y]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    wings=0
    sum=0
    mins=1000000000000000
    for i in range(4):
        zx=dx[i]+x
        zy=dy[i]+y
        if 0<=zx<n and 0<=zy<m:
            sum+=array[zx][zy]
            mins=min(mins,array[zx][zy])
            wings+=1
    if wings==2:
        return 0
    else:
        if wings==4:
            sum-=mins
        return sum+go
for i in range(n):
    for j in range(m):
        gr[i][j]=0
        dfs(i,j,array[i][j],1)
        gr[i][j] = 1
        t=gdfs(i,j)
        ans=max(ans,t)
print(ans)