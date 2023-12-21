import sys
input = sys.stdin.readline
n=int(input().rstrip())
graph=[]
for _ in range(n):
    e=list(map(int,input().split()))
    graph.append(e)
dp=[[0]*(n)for _ in range(n)]

for i in range(1,n):
    temp = 0
    if graph[0][i - 1] <= graph[0][i]:
        temp = graph[0][i] + 1 - graph[0][i-1]
    dp[0][i]=temp+dp[0][i-1]
for i in range(1,n):
    temp = 0
    if graph[i - 1][0] <= graph[i][0]:
        temp = graph[i][0] + 1 - graph[i - 1][0]
    dp[i][0] = temp + dp[i-1][0]

for i in range(1,n):
    for j in range(1,n):
        if i==n-1 and j==1:
            j=1
        temp1 = 0
        if graph[i-1][j] <= graph[i][j]:
            temp1 = graph[i][j] + 1 - graph[i-1][j]
        temp2=0
        if graph[i][j-1]<=graph[i][j]:
            temp2=graph[i][j]+1-graph[i][j-1]
        dp[i][j]=min((dp[i-1][j]+temp1),(dp[i][j-1]+temp2))
print(dp[n-1][n-1])