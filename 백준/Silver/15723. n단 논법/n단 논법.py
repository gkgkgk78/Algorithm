import sys
input = sys.stdin.readline

# ord(a) => 97임

graph = [[0] * 26 for _ in range(26)]

n = int(input().rstrip())
for _ in range(n):
    a1, a2, a3 = map(str, input().split())
    t1 = ord(a1) - 97
    t2 = ord(a3) - 97
    graph[t1][t2] = 1

for k in range(26):
    for i in range(26):
        for j in range(26):
            if i == j:
                continue
            if graph[i][j] == 1:
                continue
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j]=1

m = int(input().rstrip())

for _ in range(m):
    a1, a2, a3 = map(str, input().split())
    t1 = ord(a1) - 97
    t2 = ord(a3) - 97
    t3=graph[t1][t2]

    if t3==1:
        print("T")
    else:
        print("F")