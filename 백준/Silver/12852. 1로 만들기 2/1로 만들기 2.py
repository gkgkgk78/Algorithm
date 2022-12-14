import sys
input=sys.stdin.readline

n=int(input().rstrip())

dp=[0  for _ in range(n+1)]
check=[[] for _ in range(n+1)]

check[1]=[1]


for i in range(2,n+1):
   if i==10:
       i=10
   to=i-1
   dp[i]=dp[i-1]+1

   if(i%3==0):

       if dp[i]>dp[i//3]+1:
           dp[i]=dp[i//3]+1
           to = i//3

   if (i%2==0):
       if dp[i] > dp[i // 2] + 1:
           dp[i] = dp[i // 2] + 1
           to = i // 2
   for l in check[to]:
       check[i].append(l)
   check[i].append(i)

print(dp[n])
for l in range(len(check[n])-1,-1,-1):
    print(check[n][l],end=" ")