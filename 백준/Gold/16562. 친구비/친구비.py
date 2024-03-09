import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
e = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
last = []
for _ in range(m):
    a1, a2 = map(int, input().split())
    graph[a1].append(a2)
    graph[a2].append(a1)
    last.append(a1)
    last.append(a2)
last = set(last)
total = []
for i in range(len(e)):
    total.append((e[i], i + 1))
total = sorted(total, key=lambda x: x[0])
visit = [0] * (n + 1)
now = 0

q = deque()
for a1, a2 in total:
    q.append((a1, a2))

while q:
    if now == k:
        break
    value, vertex = q.popleft()
    if visit[vertex] == 1:
        continue
    temp = deque()
    temp.append(vertex)
    if now + value > k:
        break
    now += value
    while temp:
        a1 = temp.popleft()
        for i in graph[a1]:
            if visit[i] == 0:
                visit[i] = 1
                temp.append(i)
flag = 0
for i in last:
    if visit[i] == 0:
        flag = 1
        break

if flag == 0:
    print(now)
else:
    print("Oh no")