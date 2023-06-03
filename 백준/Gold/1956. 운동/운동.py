import sys

input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[sys.maxsize] * v for _ in range(v)]
for _ in range(e):
    a1, a2, a3 = map(int, input().split())
    a1 -= 1
    a2 -= 1
    graph[a1][a2] = a3

for k in range(v):
    for i in range(v):
        for j in range(v):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = sys.maxsize
for i in range(v):
    answer = min(answer, graph[i][i])

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)