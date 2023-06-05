import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input().rstrip())

graph = []
graph1 = []

for _ in range(n):
    e = list(map(int, input().split()))
    graph.append(e)

graph1 = deepcopy(graph)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if i == k or k == j:
                continue

            if graph[i][j] == graph[i][k] + graph[k][j]:
                graph1[i][j] = 0
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                print(-1)
                sys.exit()

answer = 0
for k in graph1:
    answer += sum(k)

print(answer // 2)