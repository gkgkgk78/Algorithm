import sys
from collections import deque
import math

input=sys.stdin.readline


def bfs():
    while q:
        g1,g2,g3=q.popleft()
        dx = [ [g1-1,g2,g3],[g1+1,g2,g3],[g1,g2+1,g3],[g1,g2-1,g3],[g1,g2,g3+1],[g1,g2,g3-1]]
        for i in range (0,6):
                 x,y,z=dx[i]
                 if  0<=x<l   :
                    if 0<=y<m :
                        if 0<=z<n:
                            if a[x][y][z]==0:
                                q.append([x,y,z])
                                a[x][y][z]=a[g1][g2][g3]+1


q=deque()

n,m,l = map(int,input().split())

# a = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(l)]
a=[]
check_reap=0
ans=-1
for e in range(l):
    tmp=[]
    for i in range(0, m):
            kt=list(map(int,input().split()))
            tmp.append(kt)
            for j1 in range(0,n):
                if kt[j1]==0:
                    check_reap=1
                elif kt[j1]==1:
                    q.append([e,i,j1])
    a.append(tmp)

if check_reap==0:
    print(0)
    exit(0)
else:
    bfs()
    for e in a:
        for i in  e:
            for jk in i:
                if jk==0:
                    print(-1)
                    exit(0)
                if jk>ans:
                    ans=jk



print(ans-1)


