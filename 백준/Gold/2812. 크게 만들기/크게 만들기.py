import sys
input = sys.stdin.readline
from collections import deque

n,k=map(int,input().split())
e=list(map(str,input().rstrip()))
co=0
stack=[]


for i in e:
    while(co<k and stack and (int)(stack[-1])<(int)(i)):
        stack.pop()
        co+=1
    stack.append(i)
if k!=co:
    stack=stack[:-(k-co)]

print(''.join(stack))