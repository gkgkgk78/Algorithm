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

d=[[0]*3 for _ in range(100001)]
d[1][0]=1
d[1][1]=1
d[1][2]=1

for i in range(2,x+1):
    d[i][0]=(d[i-1][1]+d[i-1][2])%9901
    d[i][1] = (d[i - 1][0] + d[i - 1][2]) % 9901
    d[i][2] = (d[i - 1][0] + d[i - 1][1]+d[i - 1][2]) % 9901
print(sum(d[x])%9901)