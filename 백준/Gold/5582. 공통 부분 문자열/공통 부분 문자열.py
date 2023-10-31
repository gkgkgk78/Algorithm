import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
a1=[0]
a2=[0]

a1.extend(list(map(str,input().rstrip())))
a2.extend(list(map(str,input().rstrip())))
dp=[[0]*(len(a2)+1)for _ in range(len(a1)+1)]

for i in range(1,len(a1)):
    for j in range(1,len(a2)):
        if i==0 or j==0:
            dp[i][j]=0
        elif a1[i]==a2[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=0
ee=0
for i in dp:
    ee=max(ee,max(i))
print(ee)