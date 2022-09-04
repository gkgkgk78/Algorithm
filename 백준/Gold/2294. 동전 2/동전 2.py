n, k = map(int, input().split())
c = []
dp = [100001] * (k+1)
dp[0]=0
for i in range(n):
    c.append(int(input().rstrip()))

for i in range(1,k+1):
    for j in c:
        if i>=j:
            dp[i]=min(dp[i],dp[i-j]+1)
if dp[k]==100001:
    print(-1)
else:
    print(dp[k])