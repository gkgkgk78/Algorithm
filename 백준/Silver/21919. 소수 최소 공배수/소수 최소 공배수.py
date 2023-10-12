import sys
from collections import deque
import math
input = sys.stdin.readline
int(input().rstrip())
e=list(map(int,input().split()))

check=0
lele=[]
for i in e:
    if i==1:
        continue
    ee=i
    cc=0
    for k in range(2,(int)(math.sqrt(i))+1):
        if ee%k==0:
            cc=1
            break

    if cc==0:
        lele.append(i)

if len(lele)==0:
    print(-1)
else:
    print(math.lcm(*lele))