import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n,k=map(int,input().split())


e=[]
for _ in range(n):
    e.append(int(input().rstrip()))
e.sort()
dp=[sys.maxsize]*(k+1)
dp[0]=0
for i in e:
    for j in range(i,k+1):
        dp[j]=min(dp[j-i]+1,dp[j])
if dp[k]==sys.maxsize:
    print(-1)
else:
    print(dp[k])