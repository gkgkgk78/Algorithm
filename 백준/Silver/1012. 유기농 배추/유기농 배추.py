import sys
from collections import deque
import math

input=sys.stdin.readline
sys.setrecursionlimit(10000)
def dfs(t1,t2):
    visit_list[t1][t2]=1

    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    for i in range(0,4):
        x=t1+dx[i]
        y=t2+dy[i]
        if 0<=x<n and 0<=y<m:
            if graph[x][y]==1 and visit_list[x][y]==0:
                visit_list[x][y]=1
                dfs(x,y)

stst=int(input())

while stst>0:
    n, m, v = map(int, input().split())

    graph = [[0] * (m) for _ in range(n)]
    visit_list = [[0] * (m) for _ in range(n)]

    for i in range(0, v):
        t1, t2 = map(int, input().split())
        graph[t1][t2] = 1
    count=0
    for  i  in  range(0,n):
        for j in    range (0,m):
            if graph[i][j]==1 and visit_list[i][j]==0:
                dfs(i,j)
                count= count+1
    print(count)
    stst=stst-1












