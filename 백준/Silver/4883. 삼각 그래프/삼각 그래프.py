import sys
from collections import deque

input = sys.stdin.readline

te=1
while 1:
    n = int(input().rstrip())
    dp = [[sys.maxsize]*(3)for _ in range(n)]
    if n==0:
        break
    graph=[]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    dp[0][0]=sys.maxsize
    dp[0][1]=graph[0][1]
    dp[0][2]=graph[0][2]+dp[0][1]
    for i in range(1,n):
        dp[i][0] = graph[i][0]+min(dp[i-1][0],dp[i-1][1])
        dp[i][1] = graph[i][1]+min(dp[i-1][0],dp[i-1][1],dp[i-1][2],dp[i][0])
        dp[i][2] = graph[i][2]+min(dp[i-1][1],dp[i-1][2],dp[i][1])

    print(str(te)+"."+" " +str(dp[n-1][1]))
    te+=1