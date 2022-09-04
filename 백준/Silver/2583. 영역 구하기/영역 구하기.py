import sys
from collections import deque

input=sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(t1,t2):

    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    maps[t1][t2]=1
    anss = 1
    for i in range (0,4):
        x1=dx[i]+t1
        y1=dy[i]+t2
        if 0<=x1<a and 0<=y1<b:
            if maps[x1][y1]==0:
                tt=dfs(x1,y1)
                anss=anss+tt

    return anss



a,b,c=map(int,input().split())

maps=[[0]*b for _ in range(a)]


for i in range (c):
    y1,x1,y2,x2=map(int,input().split())
    for t1 in range(x1,x2):
        for t2 in range(y1,y2):
            maps[t1][t2]=1
jj=[]
for i in range (a):
    for j in range (b):
        if maps[i][j]==0:
            m=dfs(i,j)
            jj.append(m)
print(len(jj))
jj.sort()
print(*jj)