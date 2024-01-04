import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
e=list(map(int,input().split()))
total=[[]for _ in range(4)]

for i in e:
    temp=0
    for k in range(4):
        if len(total[k])==0:
            total[k].append(i)
            temp=1
        else:
            if total[k][-1]<i:
                total[k].append(i)
                temp=1
        if temp==1:
            break

last=n
answer="YES"
for l in range(n,0,-1):
    temp=0

    for k in range(4):
        if len(total[k])>0 and total[k][-1]==l:
            total[k].pop()
            temp=1
        if temp==1:
            break
    if temp==0:
        answer="NO"
        break
print(answer)