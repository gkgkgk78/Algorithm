import sys
from collections import deque
import math

input=sys.stdin.readline


def bfs():
    q = deque()
    q.append(S)
    maps[S]=0

    while q:


        g1=q.popleft()

        if g1==G:
            print(maps[g1])
            exit(0)
            break
        dx = [U,-D ]
        for i in range (0,2):
                 x=g1+dx[i]
                 if  1<=x<=F   :
                    if maps[x]==-1:
                        maps[x]=maps[g1]+1
                        q.append(x)





F,S,G,U,D=map(int,input().split())


maps=[-1]*(F+1)
bfs()
print("use the stairs")