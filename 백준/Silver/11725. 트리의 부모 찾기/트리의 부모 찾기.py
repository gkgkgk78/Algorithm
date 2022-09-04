import sys,copy
from collections import deque

input=sys.stdin.readline
sys.setrecursionlimit(10**9)



def dfs(v):

    for i in graph[v]:
        if visit[i]==0:
            visit[i]=v
            dfs(i)




h=int(input())
graph=[[0] for _ in range(0,h+1)]
visit=[0]*(h+1)
gg=h

while gg>1:
    f1,f2=map(int,input().split())
    graph[f1].append(f2)
    graph[f2].append(f1)
    gg=gg-1

visit[1]=1
dfs(1)


for i in range(2,h+1):
    print(visit[i])












