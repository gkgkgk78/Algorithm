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



sum1=1
for i in range(1,n+1):
    sum1*=i

sum2=1
sum3=1
for i in range(1,n-m+1):
    sum2*=i

for i in range(1,m+1):
    sum3*=i
print(sum1//(sum2*sum3))