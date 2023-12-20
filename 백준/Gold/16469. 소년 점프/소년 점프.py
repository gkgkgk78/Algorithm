import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    e=list(map(int,input().rstrip()))
    graph.append(e)

def bfs(x,y):
    visit=[[-1]*(m)for _ in range(n)]
    visit[x][y]=0
    q=deque()
    q.append((x,y))
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while q:
        a1,a2=q.popleft()
        for i in range(4):
            zx=a1+dx[i]
            zy=a2+dy[i]
            if 0<=zx<n and 0<=zy<m:
                if graph[zx][zy]==0 and visit[zx][zy]==-1:
                    visit[zx][zy]=visit[a1][a2]+1
                    q.append((zx,zy))

    return visit



total=[]

for _ in range(3):
    a1,a2=map(int,input().split())
    a1-=1
    a2-=1
    t=bfs(a1,a2)
    total.append(t)
answer=sys.maxsize
co=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            continue
        te=0
        for k in range(3):
            if total[k][i][j]==-1:
                te=-1
                break
            else:
                te=max(te,total[k][i][j])
        if te>=0:
            if answer==te:
                co+=1
            elif te<answer:
                answer=min(answer,te)
                co=1

if answer==sys.maxsize:
    print(-1)
else:
    print(answer)
    print(co)