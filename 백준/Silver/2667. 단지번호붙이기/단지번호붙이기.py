import sys
from collections import deque
import math

input=sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(t1,t2):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    hh=0
    for i in range(0, 4):
        x = t1 + dx[i]
        y = t2 + dy[i]
        if 0 <= x < h1 and 0 <= y < h1:
            if g[x][y] == '1' and visit[x][y] == 0:
                visit[x][y] = 1
                hh=hh+1
                h=dfs(x, y)
                hh=hh+h

    return  hh





h1= int(input())
t2=h1
g=[]
visit=[[0]*h1 for  _ in range(h1)]
while t2>0:
    y=input().rstrip('\n')

    g.append(list(y))
    t2=t2-1
k=[]
count=0
for i in range(0,h1):
    for j in range(0,h1):
        if g[i][j]=='1' and visit[i][j]==0:
            jj=dfs(i,j)
            
            if jj==0:
                jj=1
            k.append(jj)
            count=count+1

print(count)


k.sort()
for i in range(len((k))):
    print(k[i])
