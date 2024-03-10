import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
parents = [0] * (n + 1)


def make():
    for i in range(1, n + 1):
        parents[i] = i


def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]


def union(u, v):
    a1 = find(u)
    a2 = find(v)
    if a1 != a2:
        if a1 < a2:
            parents[a2] = a1
        else:
            parents[a1] = a2


graph = [[] for _ in range(n + 1)]
make()
for _ in range(m):
    e = list(map(str, input().split()))
    a1, a2 = (int)(e[1]), (int)(e[2])
    if e[0] == "F":
        union(a1, a2)
    else:
        graph[a1].append(a2)
        graph[a2].append(a1)

# 이제 1부터시작 하면서 원수의 원수 찾으면 됨

for i in range(1, n + 1):
    if len(graph[i]) > 0:
        # 여기는 원수
        for j in graph[i]:
            for k in graph[j]:
                union(i, k)
for i in range(1, n + 1):
    parents[i] = find(i)

now = set(parents)
print(len(now) - 1)