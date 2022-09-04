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

n,m=map(int,input().split())

t=list(map(int,input().split()))

sumz=sum(t)
left=max(t)
right=sumz


def check():
    coount=0
    add=0

    for i in range(n):

        if(t[i]+add)>mid:
            add=0
            coount+=1
        add+=t[i]
    if(add)>0:
        coount+=1

    # coount += 1 if add else 0

    return coount


while left<=right:
    mid=(left+right)//2
    e=check()
    if(e>m):
        left = mid + 1
    else:
        right = mid - 1

print(left )