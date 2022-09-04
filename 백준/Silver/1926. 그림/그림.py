import sys,copy
from collections import deque

input=sys.stdin.readline
sys.setrecursionlimit(10**5)

#한 물통이 비거나 , 다른 한 물통이 가득 찰 때까지 물을 붓는다




def dfs(g1,g2):
    q = deque()
    q.append((g1,g2))
    ho=1
    while q:
        x,y=q.popleft()
        check[x][y]=1
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

        for i in range(0,4):
            zx=x+dx[i]
            zy=y+dy[i]

            if 0<=zx<a and 0<=zy<b and check[zx][zy]==0 and graph[zx][zy]==1:
                q.append((zx,zy))
                check[zx][zy]=1
                ho=ho+1

    return ho





a,b=map(int,input().split())


graph=[]
ch=0

check=[[0]*b for _ in range(a)]
for i in range (a):
    tmp=list(map(int, input().split()))
    for j in range(b):
        if tmp[j]==1:

            ch=1
    graph.append(tmp)

kk=0
size=0
if ch==0:
    print(0)
    print(0)
else:
    for i in range(0,a):
        for j in range(0,b):
            if graph[i][j]==1 and check[i][j]==0:
                ll=dfs(i,j)
                kk=kk+1
                size=max(size,ll)

    print(kk)
    print(size)


