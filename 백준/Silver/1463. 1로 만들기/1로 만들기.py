import sys, copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n=int(input().rstrip())
d=[0]*(n+1)
jo=n

for i in range(2,n+1):

    d[i] = d[i-1]+1
    if i%3==0:
        k1=i//3
        d[i]=min(d[i],d[k1]+1)
    if i%2==0:
        k2=i//2
        d[i] = min(d[i], d[k2]+1)

print(d[n])

