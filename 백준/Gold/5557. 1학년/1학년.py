import sys

input = sys.stdin.readline

n=int(input().rstrip())
e=list(map(int,input().split()))

dp=[[[0] for _ in range(21)] for _ in range(n-1)]

dp[0][e[0]]=[1]



for i in range(1,n-1):
    now=e[i]
    for j in range(21):
        if dp[i-1][j][0]>0:
            next=j+now
            next1=j-now
            if 0<=next<=20:
                dp[i][next][0]+=dp[i-1][j][0]

            if 0 <= next1 <= 20:
                dp[i][next1][0] += dp[i-1][j][0]

print(*dp[n-2][e[-1]])