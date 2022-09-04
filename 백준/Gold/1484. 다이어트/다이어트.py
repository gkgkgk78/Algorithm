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


n=int(input().rstrip())

l=1
r=2
t=0
while r<100000:
    m=r*r-l*l
    if(m==n):
        print(r)
        r+=1
        t=1
    elif(m<n):
        r+=1
    else:
        l+=1
if t==0:
    print(-1)