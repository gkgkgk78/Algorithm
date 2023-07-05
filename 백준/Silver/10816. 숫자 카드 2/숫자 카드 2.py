import sys
from collections import Counter
input = sys.stdin.readline
n=int(input().rstrip())
e=list(map(int,input().split()))
c=Counter(e)
a1=int(input().rstrip())
g=list(map(int,input().split()))
for k in g:
    ee=c[k]
    print(c[k],end=" ")