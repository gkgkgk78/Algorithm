import sys
from collections import deque

input = sys.stdin.readline

n,m,k=map(int,input().split())
total=[]
dp=[[0]*(m+1)for _ in range(n+1)]
graph=[[[]for _ in range(n+1)]for _ in range(n+1)]

for _ in range(k):
    a1,a2,a3=map(int,input().split())
    if a1>=a2:
        continue
    if len(graph[a1][a2])==0:
        graph[a1][a2]=[a3]
    else:

        if a3>graph[a1][a2][0]:
            graph[a1][a2]=[a3]
    total.append([a1,a2,a3])

for a1,a2,a3 in total:
    if a1!=1:
        continue
    dp[a2][2]=max(dp[a2][2],a3)

for i in range(2,m):
    for j in range(1,n+1):
        if dp[j][i]!=0:
            #이제 증가 해봐야 한다
            for k in range(1,n+1):
                if len(graph[j][k])>0:
                    ne=graph[j][k][0]
                    dp[k][i+1]=max(dp[k][i+1],dp[j][i]+ne)
print(max(dp[n]))