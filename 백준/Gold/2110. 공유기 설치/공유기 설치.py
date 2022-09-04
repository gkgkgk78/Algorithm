import sys, copy, heapq
import heapq, math
from itertools import permutations, combinations, product
from collections import deque
from itertools import product

#a=list(product(i,repeat=len(powers)))
#b=list(product(*a)) #리스트 안에 있는 원소들끼리 조합


#input = sys.stdin.readline
#01020306523합격8

n,x=map(int,input().split())
tot=[]
for _ in range(n):
    a=int(input().rstrip())
    tot.append(a)
tot.sort()

start=0
end=max(tot)-tot[0]
gap=0
while start<=end:
    mid=(start+end)//2
    count=1
    value=tot[0]
    for l in range(1,len(tot)):
        if tot[l]>=value+mid:
            value=tot[l]
            count+=1
    if count>=x:
        gap=mid
        start=mid+1
    else:
        end=mid-1
print(gap)

















