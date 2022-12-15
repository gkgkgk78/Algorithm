import sys
from collections import deque
input=sys.stdin.readline


e=list(input().rstrip())
test=list(input().rstrip())

last=test[-1]
leng=len(test)
stack=[]
for i in e:
    stack.append(i)
    if i==last and len(stack)>=leng:
        la=len(stack)
        tt=0
        check=0
        if la-leng>=0:
            for k in range(la-leng,la):
                if test[tt]!=stack[k]:
                    check=1
                    break
                tt += 1
            if check==0:
                for k in range(len(test)):
                    stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")