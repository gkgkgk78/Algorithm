import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

t = int(input().rstrip())
e = list(map(int, input().split()))
if len(e) != 3:
    ne = [0] * (3 - len(e))
    e += ne

visit = [ [ [0] * (61)for _ in range(61)] for _ in range(61)]

a1 = e[0]
a2 = e[1]
a3 = e[2]


def bfs(a1, a2, a3):
    q = deque()
    visit[a1][a2][a3] = 1
    q.append((a1, a2, a3))
    tt = [-9, -3, -1]
    tt = list(permutations(tt, 3))
    while q:
        a1, a2, a3 = q.popleft()
        if a1 == 0 and a2 == 0 and a3 == 0:
            return
        for i1, i2, i3 in tt:
            z1 = i1 + a1
            z2 = i2 + a2
            z3 = i3 + a3
            if z1 < 0:
                z1 = 0
            if z2 < 0:
                z2 = 0
            if z3 < 0:
                z3 = 0
            if visit[z1][z2][z3]==0:
                visit[z1][z2][z3]=visit[a1][a2][a3]+1
                q.append((z1,z2,z3))
bfs(a1,a2,a3)
print(visit[0][0][0]-1)