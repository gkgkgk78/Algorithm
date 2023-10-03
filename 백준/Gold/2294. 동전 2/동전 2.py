import sys
from collections import deque

input = sys.stdin.readline
n,m=map(int,input().split())
e=[]
for _ in range(n):
    e.append(int(input().rstrip()))
e.sort()
dp=[sys.maxsize]*(m+1)
dp[0]=0
for i in range(n):
    now=e[i]
    for j in range(now,m+1):
        dp[j]=min(dp[j],dp[j-now]+1)
if dp[m]==sys.maxsize:
    print(-1)
else:
    print(dp[m])