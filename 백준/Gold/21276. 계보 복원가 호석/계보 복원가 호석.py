import sys
import math
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

indegree = dict()
graph = dict()
e = list(map(str, input().split()))
total = dict()
for i in e:
    indegree[i] = 0
    graph[i] = []
    total[i] = []

k = int(input().rstrip())
for _ in range(k):
    a1, a2 = map(str, input().split())
    graph[a2].append(a1)
    indegree[a1] += 1
first = []
for now, val in indegree.items():
    if val == 0:
        first.append(now)
first.sort()
print(len(first))
print(*first)


def bfs(now):
    q = deque()
    q.append(now)
    while q:
        a1 = q.popleft()
        for i in graph[a1]:

            indegree[i] -= 1
            if indegree[i] == 0:
                total[a1].append(i)
                q.append(i)

for i in first:
    bfs(i)
a1 = total.keys()
a1 = sorted(a1)
for i in a1:
    nn = total[i]
    nn.sort()
    print(i, len(nn), *nn)