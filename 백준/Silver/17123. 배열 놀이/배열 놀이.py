import sys
input = sys.stdin.readline

t=int(input().rstrip())

for _ in range(t):
    n,m=map(int,input().split())
    graph=[]
    test=[[0]*(n+1) for _ in range(n+1)]
    for l in range(n):
        graph.append(list(map(int,input().split())))
    if n==2:
        n=2

    for l in range(m):
        r1,c1,r2,c2,v=map(int,input().split())
        r1-=1
        c1-=1
        r2-=1
        c2-=1
        test[r1][c1]+=v
        test[r2+1][c2+1]+=v
        test[r1][c2+1]-=v
        test[r2+1][c1]-=v

    for i in range(n):
        for j in range(n):
            test[i][j+1]+=test[i][j]

    for i in range(n):
        for j in range(n):
            test[j+1][i] += test[j][i]

    for i in range(n):
        for  j in range(n):
            graph[i][j]+=test[i][j]
    row=[]
    col=[]
    for l in range(n):
        tt=sum(graph[l])
        row.append(tt)
    for i in range(n):
        temp=0
        for j in range(n):
            temp+=graph[j][i]
        col.append(temp)
    print(*row)
    print(*col)