import sys, copy
from itertools import combinations

from collections import deque

input = sys.stdin.readline


n=int(input().rstrip())


for i in range(n):

    l=int(input().rstrip())
    n=list(map(int,input().split()))
    n.sort()
    jo=[0]*len(n)
    gg=0
    left=0
    right=len(n)-1

    for i in range(len(n)//2):
            jo[left]=n[gg]
            jo[right]=n[gg+1]
            left+=1
            right-=1
            gg=gg+2
    if  len(n)%2==1:
        je= len(n)//2
        jo[je]=n[len(n)-1]
    ans=0

    for i in range(len(jo)-1):
        ans=max(ans,abs(jo[i]-jo[i+1]))
    ans=max(ans,abs(jo[len(jo)-1]-jo[0]))
    print(ans)