import sys
from collections import deque
input = sys.stdin.readline


n,k = map(int, input().split())
dp=[0]*(n+1)
e=list(map(int,input().split()))

sumz=e[0]
left=0
right=1
while right<=n:
    if sumz>=k:
        while sumz>=k:
            dp[right]=max(dp[right],dp[left]+sumz-k)
            sumz-=e[left]
            left+=1
    else:
        dp[right]=max(dp[right],dp[right-1])
        if right==n:
            break
        sumz+=e[right]
        right+=1
print(dp[n])