import sys


a=[""]
b=[""]
a.extend(list(map(str,input().rstrip())))

b.extend(list(map(str,input().rstrip())))

dp=[[0]*(len(a))for _ in range(len(b))]

for i in range(len(b)):
    for j in range(len(a)):
        if i==0 or j==0:
            dp[i][j]=0
        else:
            if a[j]==b[i]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j] =max(dp[i-1][j],dp[i][j-1])
ans=-sys.maxsize
for i in dp:

    ans=max(ans,max(i))
print(ans)