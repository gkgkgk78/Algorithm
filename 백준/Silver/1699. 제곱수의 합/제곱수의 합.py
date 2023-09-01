import sys

input = sys.stdin.readline

n = int(input().rstrip())
dp=[0]*(n+1)
for i in range(1,n+1):
    dp[i]=i

for i in range(2,n+1):
    for j in range(1,i+1):
        t=j*j
        if t>i:
            break
        if dp[i]>1+dp[i-j*j]:
            dp[i]=1+dp[i-j*j]
 
print(dp[n])