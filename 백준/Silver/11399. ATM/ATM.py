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
m=list(map(int,input().split()))

sumz=0
m.sort()
for l in range(len(m)):
    sumz+=sum(m[0:l+1])
print(sumz)