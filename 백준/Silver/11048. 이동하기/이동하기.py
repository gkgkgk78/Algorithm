import sys
from collections import deque

input = sys.stdin.readline
q=deque()
n, m = map(int, input().split())
graph = []
visit = [[0] * m for _ in range(n)]
data = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))



q.append((0,0))
visit[0][0]=1
data[0][0]=graph[0][0]
dx=[1,0,1]
dy=[0,1,1]

while q:
    a1,a2=q.popleft()

    for l in range(3):
        zx=a1+dx[l]
        zy=a2+dy[l]

        if 0<=zx<n and 0<=zy<m:
            if visit[zx][zy]==0:
                visit[zx][zy]=1
                data[zx][zy]=graph[zx][zy]+data[a1][a2]
                q.append((zx,zy))
            else:
                if data[zx][zy]<graph[zx][zy]+data[a1][a2]:
                    data[zx][zy] = graph[zx][zy] + data[a1][a2]
                    q.append((zx, zy))

print(data[n-1][m-1])