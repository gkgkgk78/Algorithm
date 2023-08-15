import sys
input = sys.stdin.readline

t,w=map(int,input().split())
dp=[ [ [0]*(t+1)for _ in range(3)] for _ in range(w+1)]

e=[0]
for _ in range(t):
    e.append(int(input().rstrip()))

for i in range(w+1):
    for j in range(1,t+1):
        n1=0
        n2=0
        if e[j]==2:
            n2=1
        else:
            n1=1
        if i == 0:
            dp[i][1][j]=dp[i][1][j-1]+n1
            continue
        dp[i][1][j]=max(dp[i][1][j-1]+n1,dp[i-1][2][j-1]+n1)
        dp[i][2][j]=max(dp[i][2][j-1]+n2,dp[i-1][1][j-1]+n2)

ans=0
for i in range(w+1):
    for j in range(1,3):
        ans=max(ans,dp[i][j][t])
print(ans)