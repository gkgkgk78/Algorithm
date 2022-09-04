import sys, copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def isValid(midValue):
    high=arr[0]
    low=arr[0]
    d=0
    for i in arr:
        if i>high:
            high=i
        if low>i:
            low=i
        if high-low>midValue:
            d+=1
            low=i
            high=i

    return d


n, m = map(int, input().split())
arr = list(map(int, input().split()))
r = max(arr)
l = 0
result = r

while l<=r:
    mid=(l+r)//2
    aa=isValid(mid)
    if m>aa:
        r=mid-1
        result=min(result,mid)
    else:
        l=mid+1
print(result)
