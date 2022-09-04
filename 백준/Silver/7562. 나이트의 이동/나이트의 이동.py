import sys
from collections import deque
import math

input=sys.stdin.readline


def bfs():
    q = deque()
    q.append([sx,sy])


    while q:


        g1,g2=q.popleft()

        if g1==tx and g2==ty:
            print(maps[g1][g2])
            break
        dx = [[g1-2,g2+1],[g1-2,g2-1],[g1-1,g2-2],[g1-1,g2+2],[g1+1,g2-2],[g1+1,g2+2],[g1+2,g2-1],[g1+2,g2+1] ]
        for i in range (0,8):
                 x,y=dx[i]
                 if  0<=x<k   :
                    if 0<=y<k :

                            if maps[x][y]==0:
                                maps[x][y]=maps[g1][g2]+1
                                q.append([x,y])





j=int(input())

while j>0:
    k=int(input())
    maps=[[0]*k for _ in range(0,k)]

    sx,sy=map(int,input().split())
    tx,ty=map(int,input().split())
    bfs()
    j=j-1





