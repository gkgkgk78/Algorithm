import sys
from collections import deque
import math

input=sys.stdin.readline


def bfs(t1,t2):
    visit = [[0] * v for _ in range(s)]
    q.append([t1,t2])
    kk=0
    while q:
        g1,g2=q.popleft()
        visit[t1][t2]=1

        dx = [[g1-1,g2],[g1,g2+1],[g1+1,g2],[g1,g2-1] ]
        for i in range (0,4):
                 x,y=dx[i]
                 if  0<=x<s and 0<=y<v :
                    if maps[x][y]=="L":
                        if visit[g1][g2]+1>visit[x][y] and visit[x][y]==0:
                            visit[x][y]=visit[g1][g2]+1
                            q.append([x,y])
                            kk=max(kk,visit[x][y])

    return kk



s,v=map(int,input().split())
q = deque()
t=0
maps=[]

while t<s:
    g=input().rstrip('\n')

    for j in range(v):
        if g[j]=="L":
            q.append([t,j])

    maps.append(list(g))
    t=t+1
cnt=0
for i in range (0,s) :
    for j  in range (0,v):
        if maps[i][j]=="L":
            cnt=max(cnt,bfs(i,j))




print(cnt-1)