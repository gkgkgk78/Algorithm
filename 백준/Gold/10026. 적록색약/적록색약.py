import sys,copy
from collections import deque

input=sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(t1,t2,g,at):

    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)



    for i in range(0,4):
        zx=dx[i]+t1
        zy=dy[i]+t2
        if 0<=zx<a and 0<=zy<a:
            if g[zx][zy]==at :
                g[t1][t2] = 1
                dfs(zx,zy,g,at)


    g[t1][t2]=1




a=int(input())

g=[]
g1=[]
for i in range(0,a):
    hh=list(input().rstrip('\n'))
    g.append(hh)
    h2=copy.deepcopy(hh)
    for j in range(0,a):
        if h2[j]=='G':
            h2[j]='R'
    g1.append(h2)

count=0

for i in range(0,a):
    for j in range(0,a):
        if g[i][j]=='R'or g[i][j]=='B'or g[i][j]=='G':
            dfs(i,j,g,g[i][j])
            count=count+1

count1=0
for i in range(0,a):
    for j in range(0,a):
        if g1[i][j]=='R'or g1[i][j]=='B':
            dfs(i,j,g1,g1[i][j])
            count1=count1+1
print(count,count1)