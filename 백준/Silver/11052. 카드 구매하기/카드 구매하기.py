import sys
input=sys.stdin.readline

n=int(input().rstrip())
price=list(map(int,input().split()))
price.insert(0,0)

dp=[0]*(n+1)
dp[1]=price[1]


for i in range(2,n+1):
    for j in range(0,i+1):
        dp[i]=max(dp[i],dp[j]+price[i-j])

print(dp[n])