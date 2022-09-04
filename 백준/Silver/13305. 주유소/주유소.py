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
road=list(map(int,input().split()))#도로
price=list(map(int,input().split()))#각 주유소의 기름값

total=price[0]*road[0]

i=1
#비교해서 가보도록 하자

mina=price[0]

for i in range(1,n-1):
    temp=road[i]*mina
    if(price[i]<mina):
        mina=price[i]
    total+=road[i]*mina
print(total)