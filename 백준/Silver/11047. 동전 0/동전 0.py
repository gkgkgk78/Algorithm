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


n,m=map(int,(input().split()))


list=[]
count=0
for _ in range(n):
    list.append(int(input().rstrip()))
for l in range(n-1,-1,-1):
    count+=m//list[l]
    m=m%list[l]
print(count)