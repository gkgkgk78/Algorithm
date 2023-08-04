import sys
from collections import  deque
input = sys.stdin.readline

n,m,t=map(int,input().split())

graph=[]
visit=[ [ [0]*2for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs():
    can=0
    if graph[0][0]==2:
        visit[0][0][1]=-1
        can=1
    else:
        visit[0][0][0]=-1

    q=deque()
    q.append((0,0,can,0))
    dx=[0,-1,0,1]
    dy=[-1,0,1,0]
    while q:
        x,y,weapon,time=q.popleft()
        if time>t:
            break
        if x==n-1 and y==m-1:
            continue
        for i in range(4):
            zx=x+dx[i]
            zy=y+dy[i]
            if 0<=zx<n and 0<=zy<m:
                if graph[zx][zy]==1 and visit[zx][zy][1]==0:#벽
                    if weapon==1:
                        visit[zx][zy][weapon]=time+1
                        q.append((zx,zy,weapon,time+1))
                elif graph[zx][zy]==0:#빈칸
                    if visit[zx][zy][weapon] == 0:  # 벽
                        visit[zx][zy][weapon] = time + 1
                        q.append((zx, zy,weapon, time + 1))
                else:#검 찾음
                    if visit[zx][zy][0]==0:
                        visit[zx][zy][0]=time+1
                        visit[zx][zy][1] = time + 1
                        q.append((zx, zy, 1, time + 1))

bfs()
ans=sys.maxsize
if visit[n-1][m-1][0]!=0 or visit[n-1][m-1][1]!=0:
    if visit[n-1][m-1][0]!=0:
        ans=min(ans,visit[n-1][m-1][0])
    if visit[n-1][m-1][1]!=0:
        ans=min(visit[n-1][m-1][1],ans)
    print(ans)

else:
    print("Fail")