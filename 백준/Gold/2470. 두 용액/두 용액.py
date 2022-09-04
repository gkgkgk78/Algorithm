import sys, copy
from itertools import combinations

from collections import deque

input = sys.stdin.readline


n=int(input())


gr=list(map(int,input().split()))
gr.sort()
left=0
right=len(gr)-1
ans=[]
an=2147483647
while left<right:
    exp=gr[left]+gr[right]
    tr=abs(an)-0
    tr1=abs(exp)-0
    if tr1<=tr:
        an=tr1
        ans=[]
        ans.append(gr[left])
        ans.append(gr[right])
    if exp<0:
        left+=1
    else:
        right -= 1
print(*ans)