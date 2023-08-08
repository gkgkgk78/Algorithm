import sys
input = sys.stdin.readline
n,m=map(int,input().split())
dp=[1]*(m+1)
for i in range(2,m+1):
    t=i
    while 1:
        if t>m:
            break
        dp[t]+=1
        t+=i

for i in range(n,m+1):
    if dp[i]==2:
        print(i)