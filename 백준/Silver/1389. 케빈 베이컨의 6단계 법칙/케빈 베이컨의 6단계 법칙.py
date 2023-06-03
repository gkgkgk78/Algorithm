import sys
input = sys.stdin.readline

n,m=map(int,input().split())

graph=[[0]*(n) for _ in range(n)]
for _ in range(m):
    a1,a2=map(int,input().split())
    a1-=1
    a2-=1
    graph[a1][a2]=1
    graph[a2][a1]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if graph[i][k]>0 and graph[k][j]>0:

                if graph[i][j]==0:
                    graph[i][j]=graph[i][k]+graph[k][j]
                else:
                    graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

min=sys.maxsize
min_index=sys.maxsize
for l in range(n):
    now=sum(graph[l])

    if now<min:
        min=now
        min_index=l

print(min_index+1)