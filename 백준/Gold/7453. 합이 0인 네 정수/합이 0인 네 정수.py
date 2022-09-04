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

a=[]
b=[]
c=[]
d=[]


n=int(input().rstrip())
for _ in range(n):
    a1,a2,a3,a4=(map(int,input().split()))
    a.append(a1)
    b.append(a2)
    c.append(a3)
    d.append(a4)

sum1=dict()
sum2=dict()

for l in range(len(a)):
    su=a[l]
    for j in range(len(b)):
        if su+b[j] not in sum1:
            sum1[su+b[j]]=1
        else:
            sum1[su + b[j]] += 1

count=0
for l in range(len(c)):
    su=c[l]
    for j in range(len(d)):
        t=su+d[j]
        if t*-1 in sum1 and sum1[-t]>0 :
            count+=sum1[-t]


print(count)