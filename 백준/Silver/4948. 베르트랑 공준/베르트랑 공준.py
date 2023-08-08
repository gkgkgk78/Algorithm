import sys

input = sys.stdin.readline

m=123456*2+1
dp=[1]*(m)
for i in range(2,m):
    t=i
    while 1:
        if t>m:
            break
        dp[t]+=1
        t+=i

while 1:
    a1=int(input().rstrip())
    if a1==0:
        break
    ans = 0
    for i in range(a1+1,a1*2+1):
        if dp[i]==2:
            ans+=1
    print(ans)