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

total=[]
left=0
right=0

mina=mina=sys.maxsize



for _ in range(n):
    total.append(int(input().rstrip()))
total.sort()
if n==1:
    print(0)
    exit(0)
while right<n and left<n:
    temp=total[right]-total[left]
    if(temp<m):
            right+=1
            continue
    else:       
        mina=min(mina,total[right]-total[left])
        if(total[right]-total[left])==m:
                print(m)
                exit(0)
        left += 1


print(mina)