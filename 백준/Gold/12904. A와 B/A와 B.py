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


check=dict()
S=input().rstrip()
T=input().rstrip()
#주어진 조건을 이용하여서 가능한지 알아내야 하는데...
def bfs(T):
    q=deque()
    q.append(T)
    while len(q)>0:
        a1=q.popleft()
        if(a1==S):
            print(1)
            sys.exit()
        if(len(a1)<=0):
            break
        check[a1]=1
        if a1[-1]=="A":
            rev=a1[:-1]
            q.append(rev)
        if a1[-1]=="B":
            rev=a1[:-1]
            rev=rev[::-1]
            q.append(rev)

bfs(T)
print(0)