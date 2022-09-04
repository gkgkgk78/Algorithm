import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline

a=int(input().rstrip())

for i in range(a):
    n=int(input().rstrip())
    coins=map(int,input().split())
    fin=int(input().rstrip())
    hi=[0]*(fin+1)
    hi[0]=1
    for i in coins:
        for j in range(i,fin+1):
            if j>=i:
                hi[j]+=hi[j-i]
    print(hi[fin])


