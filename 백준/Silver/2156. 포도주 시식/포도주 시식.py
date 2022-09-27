import sys, copy, heapq
import heapq, math
from queue import PriorityQueue
from itertools import permutations, combinations, product
from collections import deque
from itertools import product

#sys.setrecursionlimit(10 ** 5)
#a=list(product(i,repeat=len(powers)))
#b=list(product(*a)) #리스트 안에 있는 원소들끼리 조합


from itertools import combinations_with_replacement as cwr
from collections import Counter
input = sys.stdin.readline



#정수 x가 줭졌을때, 연산 4개를 적절히 사용해서 1을 만들려고 한다.
#연산을 사용하는 횟수의 최솟ㄱ밧을 출력하시오!



x=int(input())

d=[0 for _ in range(x+1)]
total=[0 for _ in range(x+1)]

for i in range(1,x+1):
    d[i]=int(input().rstrip())

#최대로 마실수 있는 포도주의 양을 출력 하라
total[1]=d[1]
if x>1:
    total[2]=total[1]+d[2]

for i in range(3,x+1):
    total[i]=max((d[i]+d[i-1]+total[i-3]), total[i-2]+d[i],total[i-1] )

print(max(total))