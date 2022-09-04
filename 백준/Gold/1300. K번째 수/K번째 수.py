import sys, copy
from itertools import combinations

from collections import deque

input = sys.stdin.readline


n=int(input())
m=int(input())

ans=0
start=1
end=m
while start<=end:
    mid=(start+end)//2
    cnt=0
    for i in range(1,n+1):
        cnt+=min(mid//i,n)

    if cnt>=m:
        end=mid-1
        ans=mid
    else:
        start=mid+1
print(ans)
