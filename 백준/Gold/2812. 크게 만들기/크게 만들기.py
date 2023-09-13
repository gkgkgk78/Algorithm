import sys
input = sys.stdin.readline
from collections import deque

n,k=map(int,input().split())
e=list(map(int,input().rstrip()))
co=0
stack=[]


for i in e:
    while(co<k and stack and stack[-1]<i):
        stack.pop()
        co+=1
    stack.append(i)
if k!=co:
    stack=stack[:-(k-co)]
an=""
for i in stack:
    an+=(str)(i)
print(an)