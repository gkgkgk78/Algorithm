import sys
import heapq
input = sys.stdin.readline

n=int(input().rstrip())
minus=[]
plus=[]
zero=[]
one=[]
for i in range(n):
    e=int(input().rstrip())
    if e<0:
        minus.append(e)
    elif e>1:
        plus.append(e)
    elif e==1:
        one.append(e)
    else:
        zero.append(e)
minus.sort()
plus.sort()
ans=0
n1=len(minus)
if len(minus)%2==1:
    if len(zero)==0:
        ans+=minus[-1]
    n1-=1

index=0
for _ in range(n1//2):
    nn=minus[index]*minus[index+1]
    ans+=nn
    index+=2

index=0
n1=len(plus)
if len(plus)%2==1:
    ans+=plus[0]
    n1-=1
    index=1
for _ in range(n1//2):
    nn=plus[index]*plus[index+1]
    ans+=nn
    index+=2
ans+=len(one)
print(ans)