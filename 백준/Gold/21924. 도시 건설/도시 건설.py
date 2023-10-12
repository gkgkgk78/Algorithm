import sys
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())
parents = [0] * (n + 1)

for i in range(1, n + 1):
    parents[i] = i
total = 0
start = []
for i in range(m):
    a1, a2, a3 = map(int, input().split())
    start.append((a3, a1, a2))
    total += a3
start.sort()


def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a1 = find(a)
    a2 = find(b)
    if a1 < a2:
        parents[a2] = a1
    else:
        parents[a1] = a2


nex = 0
for i in start:
    value, v1, v2 = i
    f1 = find(v1)
    f2 = find(v2)
    if f1 != f2:
        nex += value
        union(f1, f2)

check = 0
for i in range(1, n + 1):
    parents[i] = find(i)

for i in range(2, n):
    if parents[i] != parents[i - 1]:
        check = 1
        break

if check == 0:
    print(total - nex)
else:
    print(-1)