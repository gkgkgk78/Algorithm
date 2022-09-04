
import sys,itertools
#sys.stdin = open("input.txt")
from itertools import combinations #순열 함수

a,b=map(int,input().split())

per=list(map(int,input().split()))

count=0
for i  in range(1,a+1):
    sum=0
    for e in combinations(per,i):
       sum=0
       #print(len(e))
       #print(e)
       for k in range(len(e)):
          # print(e[k])
           sum+=e[k]
       #print()
       if(sum==b):
           count=count+1


print(count)

