import sys


input = sys.stdin.readline
n=int(input().rstrip())
e=list(map(int,input().split()))

dp=[0]*(n+1)
dp[0]=e[0]
index=0
total=[-1]*(n)
total[0]=0
def binary(now):
    left=-1
    right=index+1
    while left+1<right:
        mid=(left+right)//2
        if now<=dp[mid]:
            right=mid
        else:
            left=mid
    return right

for i in range(1,n):
    now=e[i]
    if dp[index]<now:
        index+=1
        dp[index]=now
        total[i]=index
    else:
        h=binary(now)
        if h!=-1:
            total[i]=h
            dp[h]=now
last=[-1]*(index+1)
for i in range(len(total)):
    t=total[i]
    if last[t]==-1:
        last[t]=e[i]

print(index+1)