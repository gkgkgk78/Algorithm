import sys, copy,heapq
import heapq,math
from itertools import permutations,combinations,product
from collections import deque
#sys.setrecursionlimit(10**5)

# input = sys.stdin.readline
input=sys.stdin.readline

from bisect import bisect_right, bisect_left

n=int(input().rstrip())
e=list(map(int,input().split()))
visit=[[0 for _ in range(n)]for _ in range(n)]

def bfs(a,b):

    q=deque()
    q.append((a,b,0))
    dx=[-2,-2,0,0,2,2]
    dy=[-1,1,-2,2,-1,1]
    while q:
        g1,g2,c=q.popleft()
        visit[g1][g2]=1
        if g1==e[2] and g2==e[3]:
            print(c)
            exit(0)
        for k in range(6):
            zx=g1+dx[k]
            zy=g2+dy[k]
            if 0<=zx<n and 0<=zy<n:
                    if visit[zx][zy]==0:
                        q.append((zx,zy,c+1))
                        visit[zx][zy]=1

bfs(e[0],e[1])

print(-1)

















