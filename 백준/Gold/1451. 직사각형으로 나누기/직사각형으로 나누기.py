import sys


input = sys.stdin.readline
n,m=map(int,input().split())

graph=[]
for i in range(n):
    e=list(map(int,input().rstrip()))
    graph.append(e)

#가로로 나누자
ans=-sys.maxsize
for i in range(n-2):
    first=0
    for j in range(0,i+1):
        first+=sum(graph[j])
    for j in range(i+1,n-1):
        second=0
        third=0
        for k in range(i+1, j+1):
            second += sum(graph[k])
        for k in range(j+1, n):
            third += sum(graph[k])

        ans=max(ans,first*second*third)

#세로로 나누자

for i in range(m-2):
    first=0
    for j in range(i+1):
        for k in range(n):
            first+=graph[k][j]
    for j in range(i+1,m-1):
        second=0
        third=0
        for k in range(i+1,j+1):
            for l in range(n):
                second+=graph[l][k]
        for k in range(j+1,m):
            for l in range(n):
                third+=graph[l][k]

        ans = max(ans, first * second * third)


for i in range(m-1):
    first=0
    for j in range(i+1):
        for k in range(n):
            first+=graph[k][j]
    for j in range(n-1):
        second=0
        third=0
        for k in range(j+1):
            for l in range(i+1,m):
                second+=graph[k][l]
        for k in range(j+1,n):
            for l in range(i+1,m):
                third+=graph[k][l]

        ans = max(ans, first * second * third)


for i in range(m-1,0,-1):
    first=0
    for j in range(m-1,i-1,-1):
        for k in range(n):
            first+=graph[k][j]
    for j in range(n-1):
        second=0
        third=0
        for k in range(j+1):
            for l in range(i):
                second+=graph[k][l]
        for k in range(j+1,n):
            for l in range(i):
                third+=graph[k][l]
        ans = max(ans, first * second * third)


for i in range(n-1):
    first=0
    for j in range(i+1):
        first+=sum(graph[j])
    for j in range(m-1):
        second=0
        third=0
        for k in range(i+1,n):
            for l in range(j+1):
                second+=graph[k][l]
        for k in range(i+1,n):
            for l in range(j+1,m):
                third+=graph[k][l]
        ans = max(ans, first * second * third)


for i in range(n-1):
    first=0
    for j in range(i+1,n):
        first+=sum(graph[j])
    for j in range(m-1):
        second=0
        third=0
        for k in range(i+1):
            for l in range(j+1):
                second+=graph[k][l]
        for k in range(i+1):
            for l in range(j+1,m):
                third+=graph[k][l]

        ans = max(ans, first * second * third)
print(ans)