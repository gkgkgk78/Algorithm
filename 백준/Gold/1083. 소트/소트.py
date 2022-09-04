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

tt=list(map(int,input().split()))
final=int(input().rstrip())
count=1

zw=0
ind=0
op=[]

while final!=0:
    aa=max(tt[ind:ind+final+1])
    if(ind==n-1):#뒤에 더 큰게 없을시에는 멈추면 됨
        break
    oa=0
    if(tt.index(aa)-ind<=final and tt[ind]!=aa):#뒤에 있는 것 중에서 가장 큰게 있을시에는 가져오고
        for l in range(tt.index(aa),ind,-1):
            if(tt[l]>tt[l-1]):
                hi=tt[l-1]
                tt[l-1]=tt[l]
                tt[l]=hi
                final-=1
                oa=1
                if(final==0):
                    break
    else:
        oa = 1
    if(oa==1):
        ind+=1


print(*tt)