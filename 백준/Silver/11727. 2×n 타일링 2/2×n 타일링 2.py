import sys

input = sys.stdin.readline



n=int(input().rstrip())

dp=[0 for _ in range(1002)]
dp[1]=1
dp[2]=3
if(n>=3):
    for i in range(3,n+1):
        dp[i]=(dp[i-1]%10007+(dp[i-2]*2)%10007)%10007
print(dp[n])