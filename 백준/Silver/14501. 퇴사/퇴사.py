import sys, copy
import heapq,math
from itertools import combinations,permutations
from collections import deque
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
import functools,operator

n=int(input().rstrip())
ti=[0]*(n+1)
pi=[0]*(n+1)
max_re=[0]*(n+1)

for i in range(n):
    a,b=map(int,input().split())
    ti[i]=a
    pi[i]=b

maxval=0
for j in range(n,-1,-1):
    time=ti[j]+j
    if time>n:
        max_re[j]=maxval
    else:
        max_re[j]=max(maxval,pi[j]+max_re[time])
        maxval=max_re[j]

print(maxval)
