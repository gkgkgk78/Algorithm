import sys

input = sys.stdin.readline

t=int(input().rstrip())
for _ in range(t):
    int(input().rstrip())
    e=list(map(int,input().split()))
    n=int(input().rstrip())
    dp=[0]*(n+1)
    dp[0]=1
    for i in e:
        for j in range(i,n+1):
            dp[j]+=dp[j-i]
    print(dp[n])