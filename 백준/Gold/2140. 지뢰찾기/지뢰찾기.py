import sys
from collections import deque

input = sys.stdin.readline

# 지뢰 찾기

n = int(input().rstrip())
graph = []
for _ in range(n):
    e = list(map(str, input().rstrip()))
    graph.append(e)

for i in range(n):
    for j in range(n):
        if "0" <= graph[i][j] <= "9":
            graph[i][j] = (int)(graph[i][j])
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(1, n - 1):
    for j in range(1, n - 1):
        co = 0
        x = i
        y = j
        for k in range(8):
            x = dx[k] + i
            y = dy[k] + j
            if 0 <= x < n and 0 <= y < n and graph[x][y] == 0:
                co += 1
        if co > 0:
            graph[i][j] = "X"
        else:
            for k in range(8):
                x = dx[k] + i
                y = dy[k] + j

                if 0 <= x < n and 0 <= y < n and (graph[x][y] != "#" and graph[x][y] != "X"):
                    if graph[x][y] > 0:
                        graph[x][y] -= 1

answer = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == "#":
            answer += 1
print(answer)