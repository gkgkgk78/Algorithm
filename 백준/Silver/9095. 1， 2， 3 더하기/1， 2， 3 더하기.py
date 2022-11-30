import sys
input = sys.stdin.readline
n=int(input().rstrip())
dp=[0 for _ in range(12)]
dp[1]=1
dp[2]=2
dp[3]=4
ans=[]
for i in range(4,12):
    dp[i]=dp[i-3]+dp[i-2]+dp[i-1]

ti=-sys.maxsize

for _ in range(n):
    e=int(input().rstrip())
    ans.append(dp[e])
for l in ans:
    print(l)