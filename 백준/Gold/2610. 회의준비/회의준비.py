import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())

graph = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
parents = [0] * (n + 1)

def make():
    for i in range(1, n + 1):
        parents[i] = i

def find(i):
    if parents[i] == i:
        return i
    parents[i] = find(parents[i])
    return parents[i]

for i in range(1,n+1):
    graph[i][i]=0

def union(a1, a2):
    v1 = find(a1)
    v2 = find(a2)
    if v1 == v2:
        return
    if v1 < v2:
        parents[v2] = v1
    else:
        parents[v1] = v2
make()
for _ in range(k):
    a1, a2 = map(int, input().split())
    graph[a1][a2] = 1
    graph[a2][a1] = 1
    union(a1, a2)

total = dict()
for l in range(1, n + 1):
    parents[l] = find(parents[l])
    if parents[l] not in total:
        total[parents[l]] = []
    total[parents[l]].append(l)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
answer = []
for a1, a2 in total.items():
    max_val = sys.maxsize
    max_index = -1
    for i in a2:
        temp = -1
        for k in range(1, n + 1):
            if graph[i][k] != sys.maxsize:
                if graph[i][k]>temp:
                    temp=graph[i][k]

        if temp<max_val:
            max_index=i
            max_val=temp

    if max_index==-1:
        max_index=a2[0]
    answer.append(max_index)
answer.sort()
print(len(answer))
for k in answer:
    print(k)