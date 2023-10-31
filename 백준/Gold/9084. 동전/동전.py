import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

t=int(input().rstrip())
for _ in range(t):
    _=int(input().rstrip())
    e=list(map(int,input().split()))
    l=int(input().rstrip())
    dp=[0]*(l+1)
    dp[0]=1
    for i in e:
        for j in range(i,l+1):
            dp[j]+=dp[j-i]
    print(dp[l])