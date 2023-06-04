import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[sys.maxsize] * n for _ in range(n)]

for i in range(n):
    graph[i][i]=0

for _ in range(m):
    a1, a2, a3 = map(int, input().split())
    a1 -= 1
    a2 -= 1
    if a3 == 0:
        graph[a1][a2] = 0
        graph[a2][a1] = 1

    else:
        graph[a1][a2] = 0
        graph[a2][a1] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k]+graph[k][j]<graph[i][j]:
                graph[i][j]=graph[i][k]+graph[k][j]

k=int(input().rstrip())
for _ in range(k):
    a1,a2=map(int,input().split())
    print(graph[a1-1][a2-1])