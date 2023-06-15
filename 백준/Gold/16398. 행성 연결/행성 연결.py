import sys
input = sys.stdin.readline
n = int(input().rstrip())
graph = []
q = []
for i in range(n):
    e = list(map(int, input().split()))
    for j in range(n):
        if i != j:
            q.append((e[j], i, j))
    graph.append(e)

parents = [0] * (n + 1)


def make():
    for i in range(1, n + 1):
        parents[i] = i


def find(i):
    if parents[i] == i:
        return i
    parents[i] = find(parents[i])
    return parents[i]


def union(a1, a2):
    s1 = find(a1)
    s2 = find(a2)

    if s1 == s2:
        return 0

    if s1 < s2:
        parents[s2] = s1
    else:
        parents[s1] = s2
    return 1


make()
ans = 0
q.sort()
for a1, a2, a3 in q:

    z2 = find(a2)
    z3 = find(a3)
    if z2 != z3:
        ans += a1
        union(a2, a3)

print(ans)
