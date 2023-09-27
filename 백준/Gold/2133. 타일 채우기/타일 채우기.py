import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
dp = [0] * (31)
dp[0]=1
dp[1]=0
for i in range(2,31):
    if i%2==1:
        continue
    kk=i-4
    dp[i]+=dp[i-2]*3
    while kk>=0:
        dp[i]+=dp[kk]*2
        kk-=2
print(dp[n])