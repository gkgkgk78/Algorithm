import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n) for _ in range(n)]

for _ in range(m):
    a1, a2 = map(int, input().split())
    a1 -= 1
    a2 -= 1
    graph[a1][a2] = -1
    graph[a2][a1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == -1 and graph[k][j] == -1:
                graph[i][j] = -1
                graph[j][i] = 1


s=int(input().rstrip())
for _ in range(s):
    a1, a2 = map(int, input().split())
    a1 -= 1
    a2 -= 1
    print(graph[a1][a2])