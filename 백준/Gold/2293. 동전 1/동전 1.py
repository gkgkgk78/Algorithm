import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n,k=map(int,input().split())


e=[]
for _ in range(n):
    e.append(int(input().rstrip()))

dp=[0]*(k+1)
dp[0]=1
for i in e:
    for j in range(i,k+1):
        dp[j]+=dp[j-i]
print(dp[k])