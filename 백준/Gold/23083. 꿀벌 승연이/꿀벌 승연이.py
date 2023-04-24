import sys
input = sys.stdin.readline
test = 10 ** 9 + 7
n, m = map(int, input().split())
k = int(input().rstrip())
graph = [[0] * (m) for _ in range(n)]

for _ in range(k):
    a1, a2 = map(int, input().split())
    graph[a1 - 1][a2 - 1] = -1

dx = [-1, 0, 1]
dy = [0, -1,-1]
tx=[-1,-1,0]
ty=[0,-1,-1]

graph[0][0]=1
for j in range(0,m):

    for i in range(n):
        temp=0
        if i==0 and j==0:
            continue
        if graph[i][j]==-1:
            continue
        if j%2==1:
            for l in range(3):
                zx=i+dx[l]
                zy=j+dy[l]
                if 0<=zx<n and 0<=zy<m:
                    if graph[zx][zy]!=-1:
                        temp+=graph[zx][zy]
        else:
            for l in range(3):
                zx=i+tx[l]
                zy=j+ty[l]
                if 0<=zx<n and 0<=zy<m:
                    if graph[zx][zy]!=-1:
                        temp+=graph[zx][zy]
        graph[i][j]=temp%test

print(graph[n - 1][m - 1])