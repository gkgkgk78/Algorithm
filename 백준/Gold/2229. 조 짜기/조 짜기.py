import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
e=list(map(int,input().split()))
dp=[0]*(n)
for i in range(1,n):
    low=10001
    high=0
    for j in range(i,-1,-1):
        low=min(low,e[j])
        high=max(high,e[j])
        nex=0
        if j!=0:
            nex=dp[j-1]
        dp[i]=max(dp[i],high-low+nex)
print(dp[n-1])