import sys
from collections import deque

input=sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs():

    dx = (-1, -1, -1, 0, 1, 1, 1, 0)
    dy = (-1, 0, 1, 1, 1, 0, -1, -1)
    anss=0

    while q:
        g1,g2=q.popleft()

        for i in range (0,8):
            hx=g1+dx[i]
            hy=g2+dy[i]
            if 0<=hx<a and 0<=hy<b:
                if maps[hx][hy]==0 and check[hx][hy]==-1:
                    check[hx][hy]=check[g1][g2]+1
                    q.append([hx,hy])
                    anss=max(anss,check[hx][hy])
    return anss

a,b=map(int,input().split())
check=[[-1]*b for _ in range(a)]
maps=[]
q=deque()
for i in range (0,a):
    h=list((map(int,input().split())))
    for j in range (b):
        if h[j]==1:
            q.append([i,j])
            check[i][j]=0
    maps.append(h)
ans=dfs()
print(ans)
