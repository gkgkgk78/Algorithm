import sys
from collections import deque
import heapq

input = sys.stdin.readline


n=int(input().rstrip())
e=list(map(int,input().split()))
dp=[0]*(n)
dp[0]=e[0]
total=[-1]*(n)

def bi(val,index):
    left=-1
    right=index+1

    while left+1<right:
        mid=(left+right)//2
        if dp[mid]>=val:
            right=mid

        else:
            left=mid

    return right
total[0]=0
index=0
for i in range(1,len(e)):
    now=e[i]
    if now>dp[index]:
        index+=1
        dp[index]=now
        total[i]=index
    else:
        a=bi(now,index)
        if a!=-1:
            dp[a]=now
            total[i] = a

print(index+1)

ne=[]
for i in range(len(total)-1,-1,-1):
    if total[i]==index:
        index-=1
        ne.append(e[i])
ne.reverse()
print(*ne)