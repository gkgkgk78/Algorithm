import sys

input = sys.stdin.readline

n,k=map(int,input().split())
e=list(map(int,input().split()))
left=1
right=10**5*20
ans=0
while left+1<right:

    mid=(left+right)//2
    count=0
    temp=0
    for l in range(n):
        temp+=e[l]
        if temp>=mid:
            count+=1
            temp=0

    if count>=k:
        left=mid
    else:
        right=mid

print(left)