import sys
from collections import deque

input = sys.stdin.readline

n=int(input().rstrip())
e=[]
for i in range(n):
    a1,a2=map(str,input().split())
    e.append([(int)(a1),a2,i])

e=sorted(e,key=lambda x:(x[0],x[2]))

for a1,a2,a3 in e:
    print(a1,a2)