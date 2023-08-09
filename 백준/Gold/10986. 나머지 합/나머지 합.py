import sys
import math
from collections import Counter
n,m=map(int,input().split())
e=list(map(int,input().split()))
e[0]%=m
for i in range(1,n):
    e[i]+=e[i-1]
    e[i]%=m

ea=Counter(e)

ans=0
for a1,a2 in ea.items():
    ans+=math.comb(a2,2)
    if a1==0:
        ans+=a2
print(ans)