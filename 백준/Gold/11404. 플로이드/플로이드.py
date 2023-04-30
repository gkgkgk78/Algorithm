import sys

input=sys.stdin.readline
INF=sys.maxsize

n=int(input().rstrip())
m=int(input().rstrip())
graph=[[INF]*(n) for _ in range(n)]

for _ in range(m):
    a1,a2,a3=map(int,input().split())
    a1-=1
    a2-=1
    graph[a1][a2]=min(graph[a1][a2],a3)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                graph[i][j]=0
            else:
                if graph[i][k]+graph[k][j]<graph[i][j]:
                    graph[i][j]=graph[i][k]+graph[k][j]
for i in range(n):
    for j in range(n):
        if graph[i][j]==INF:
            graph[i][j]=0

for l in graph:
    print(*l)