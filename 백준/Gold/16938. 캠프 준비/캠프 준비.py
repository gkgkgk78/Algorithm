import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n,l,r,x=map(int,input().split())
e=list(map(int,input().split()))
ans=0
#2개부터 해서 고르도록 하자
if len(e)>=2:
    for i in range(2,len(e)+1):
        aa=list(combinations(e,i))
        for k in aa:
            if sum(k)>=l and sum(k)<=r:
                if max(k)-min(k)>=x:
                    ans+=1
    print(ans)
else:
    print(0)