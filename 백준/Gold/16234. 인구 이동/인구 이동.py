import sys, copy, heapq
import heapq, math
from itertools import permutations, combinations, product
from collections import deque
sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
def dfs(a,b):
    global t
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    if visit[a][b]==0:
        t+=1
        visit[a][b]=t
        check.append(1)
    for i in range(4):
        x=a+dx[i]
        y=b+dy[i]
        if x>=0 and x<n and y>=0 and y<n:
            gy=abs(graph[x][y]-graph[a][b])
            if gy>=l and gy<=r and visit[x][y]==0:
                visit[x][y]=visit[a][b]

                check[visit[a][b]]+=1
                dfs(x,y)
t=0
graph=[]
check=[]
n,l,r=map(int,input().split())
for i in range(n):
    graph.append(list(map(int,input().split())))

visit=[[0 for i in range(n)]for i in range(n)]
cont=0
while 1:
    t=0
    g=0
    check = []
    check.append(0)
    for i in range(n):
        for j in range(n):
            if visit[i][j]==0:
                dfs(i,j)
    #print(visit,check)
    for i in range(0,len(check)):
        if check[i]>1:
            g=1
            e=[]
            for ie in range(n):
                for je in range(n):
                    if visit[ie][je]==i:
                        e.append((ie,je))
            sumz=0
            for k in e:
                a1,a2=k
                sumz+=graph[a1][a2]
            sumz=sumz//len(e)
            for k in e:
                a1,a2=k
                graph[a1][a2]=sumz
    if g==0:
        print(cont)
        break
    else:
        cont+=1
    visit = [[0 for i in range(n)] for i in range(n)]