import sys, copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline



n, m = map(int, input().split())

a = set()
for i in range(n):
    a.add(input())

b = set()
for i in range(m):
    b.add(input())

result = sorted(list(a & b))

print(len(result))

for i in result:
    g=i
    g=g.rstrip()
    print(g)
