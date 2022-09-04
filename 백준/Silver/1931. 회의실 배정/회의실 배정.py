import sys, copy
from itertools import combinations

from collections import deque
input = sys.stdin.readline
a=int(input().rstrip())

s=[]
for i in range(a):
   s1,s2=map(int,input().split())
   s.append([s1,s2])


s=sorted(s,key=lambda a : a[0])
s=sorted(s,key=lambda a : a[1])

last=0
cnt=0
for i,j in s:
    if i>=last:
        cnt+=1
        last=j
print(cnt)





