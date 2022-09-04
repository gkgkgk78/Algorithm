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
stack=[]

po=list(map(int,input().split()))
jo=max(po)
answer=[-1 for i in range(n)]
for i in range(n):

    count=0
    while stack and po[stack[-1]]<po[i]:
        answer[stack.pop()]=po[i]
    stack.append(i)
print(*answer)