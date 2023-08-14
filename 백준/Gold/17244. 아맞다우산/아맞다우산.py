import sys
from collections import deque
input=sys.stdin.readline

m,n = map(int, input().split())
graph = []
sx = -1
sy = -1
key = []
fx = -1
fy = -1

for i in range(n):
    e = list(map(str, input().rstrip()))

    for j in range(m):
        if e[j] == "S":
            sx = i
            sy = j
            e[j]="."
        elif e[j] == "X":
            key.append((i, j))
        elif e[j] == "E":
            fx = i
            fy = j
    graph.append(e)

def bfs(x, y):
    q = deque()
    visit = [[[0] * (1<<len(key)) for _ in range(m)] for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q.append((x,y,0))
    visit[x][y][0]=1
    while q:
        x,y,count=q.popleft()

        if x==fx and y==fy:
            if count==(1<<len(key))-1:
                gg=1
                return visit[x][y][count]
            continue
        for i in range(4):
            zx=dx[i]+x
            zy=dy[i]+y
            if 0<=zx<n and 0<=zy<m and graph[zx][zy]!="#":
                if graph[zx][zy]=="X":
                    nex=count|(1<<key.index((zx,zy)))
                    if visit[zx][zy][nex]==0:
                        visit[zx][zy][nex]=visit[x][y][count]+1
                        q.append((zx,zy,nex))
                else:
                    if visit[zx][zy][count]==0:
                        visit[zx][zy][count]=visit[x][y][count]+1
                        q.append((zx,zy,count))


aa=bfs(sx, sy)
print(aa-1)