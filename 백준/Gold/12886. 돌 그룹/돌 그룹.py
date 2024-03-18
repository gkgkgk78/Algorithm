import sys
from collections import deque
import heapq

input = sys.stdin.readline

a, b, c = map(int, input().split())
la = a + b + c
if la % 3 != 0:
    print(0)
    sys.exit()
visit = [[0] * (la + 1) for _ in range(la + 1)]
q = deque()
a1 = max(a, b, c)
a2 = min(a, b, c)
visit[a1][a2] = 1

q.append((a1, a2))

while q:
    a1, a2 = q.popleft()
    a3 = la - a1 - a2
    if a1 == a2 == a3:
        print(1)
        sys.exit(0)
    for z1, z2 in [(a1, a2), (a1, a3), (a2, a3)]:
        if z1 == z2:
            continue
        if z1 < z2:
            z1,z2=z2,z1
        z1 -= z2
        z2 += z2
        z3 = la - z1 - z2
        l1 = max(z1, z2, z3)
        l2 = min(z1, z2, z3)

        if  visit[l1][l2] == 0:
            visit[l1][l2] = 1
            q.append((l1, l2))

print(0)
sys.exit()