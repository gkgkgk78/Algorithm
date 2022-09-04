import sys, copy, heapq
import heapq, math
from itertools import permutations, combinations, product
from collections import deque
from itertools import product


#input = sys.stdin.readline
#01020306523합격8


def bfs(a,b):
    q=deque()
    q.append((a,b))
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    de=[]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    while q:
        x,y=q.popleft()
        visit[x][y]=1
        for i in range(4):
            zx=x+dx[i]
            zy=y+dy[i]
            if 0<=zx<n and 0<=zy<m:
                if graph[zx][zy]==0 and visit[zx][zy]==0:
                    q.append((zx,zy))
                    visit[zx][zy]=1
                if graph[zx][zy]==1 and visit[zx][zy]<1:
                    visit[zx][zy]+=1
                if graph[zx][zy]==1 and visit[zx][zy]==1:
                    de.append((zx,zy))
                    visit[zx][zy]+=1
    return de

n,m=map(int,input().split())


graph=[]
for _ in range(n):
    mm=list(map(int,input().split()))
    graph.append(mm)
pp=0
for i in range(n):
    e=graph[i]
    pp+=sum(e)

time=0
ge=[]
while 1:
    t=[]
    t=bfs(0,0)
    z=0
    time += 1
    for i in range(len(t)):
        g,h=t[i]
        graph[g][h]=0
    for i in range(n):
        e=graph[i]
        z+=sum(e)
    ge.append(z)
    if z==0:
        print(time)
        if time==1:
            print(pp)
        else:
            print(ge[len(ge)-2])
        break








