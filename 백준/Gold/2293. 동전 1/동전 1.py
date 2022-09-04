n, k = map(int, input().split())
c = []
dp = [0] * (k+1)
dp[0]=1
for i in range(n):
    c.append(int(input().rstrip()))

for i in c:
    for j in range(i,k+1):
        dp[j]+=dp[j-i]
if dp[k]==100001:
    print(-1)
else:
    print(dp[k])