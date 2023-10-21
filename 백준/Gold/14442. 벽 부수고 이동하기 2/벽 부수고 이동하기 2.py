import sys
from collections import deque
import heapq

input = sys.stdin.readline

n, m,k = map(int, input().split())
graph = []
for _ in range(n):
    a1 = list(map(int, input().rstrip()))
    graph.append(a1)
visit = [ [ [sys.maxsize] * (k+1) for _ in range(m)] for i in range(n)]

def bfs():
    q=deque()
    q.append((0,0,0))

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    visit[0][0][0]=1

    while q:
        x,y,count=q.popleft()
        now=visit[x][y][count]
        for i in range(4):
            zx=x+dx[i]
            zy=y+dy[i]
            if 0<=zx<n and 0<=zy<m:
                if zx==n-1 and zy==m-1 and visit[zx][zy][count]==sys.maxsize:
                    visit[zx][zy][count]=now+1
                    continue
                if graph[zx][zy]==0:
                    if visit[zx][zy][count]==sys.maxsize:
                        visit[zx][zy][count]=now+1
                        q.append((zx,zy,count))

                else:
                    if count <k:
                        if visit[zx][zy][count+1] == sys.maxsize:
                            visit[zx][zy][count+1]=now+1
                            q.append((zx, zy, count+1))


bfs()
ans=sys.maxsize
for i in visit[n-1][m-1]:
    if i==sys.maxsize:
        continue
    ans=min(ans,i)
if ans==sys.maxsize:
    print(-1)
else:
    print(ans)