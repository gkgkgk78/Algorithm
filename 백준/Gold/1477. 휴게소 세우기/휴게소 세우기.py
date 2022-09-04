import sys, copy, heapq
import heapq, math
from itertools import permutations, combinations, product
from collections import deque
from itertools import product
#sys.setrecursionlimit(10 ** 5)
#a=list(product(i,repeat=len(powers)))
#b=list(product(*a)) #리스트 안에 있는 원소들끼리 조합




from itertools import combinations_with_replacement as cwr
from collections import Counter
input = sys.stdin.readline

n,m,l=map(int,input().split())

store=list(map(int,input().split()))
store=[0]+store
store=store+[l]
store.sort()

left=1
right=l-1

result=0

while left<=right:
    mid=(left+right)//2
    count=0
    for i in range(1,len(store)):
        if store[i]-store[i-1]>mid:
           count+= (store[i]-store[i-1]-1)//mid

    if(count>m):
        left = mid + 1

    else:
        right=mid-1
        result=mid

print((result))