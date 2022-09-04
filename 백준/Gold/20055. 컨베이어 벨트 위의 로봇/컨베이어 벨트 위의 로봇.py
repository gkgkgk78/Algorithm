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

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([0]*n)

level=1
count=0
while 1:
    #1의 단계임
    belt.rotate(1)
    robots.rotate(1)
    robots[n-1]=0
    #2

    if(sum(robots)>0):
        for i in range(n-2,-1,-1):

            if belt[i+1]>0  and robots[i+1]==0 and robots[i]==1:
                    robots[i+1]=robots[i]
                    robots[i]=0

                    belt[i+1]-=1
    robots[-1]=0



    #3
    if (belt[0]>0 and robots[0]==0):
        robots[0]=1
        belt[0]-=1



    if(belt.count(0)>=k):
        print(level)
        exit(0)
    level+=1