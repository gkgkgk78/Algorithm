import sys
import heapq

n = int(input().rstrip())
e = list(map(int, input().split()))
e.sort()
answer=sys.maxsize
left=0
right=n-1
last=[-1,-1]
while left<right:
    mid=e[left]+e[right]
    if abs(mid)<abs(answer):
        answer=mid
        last[0]=e[left]
        last[1]=e[right]
    if mid<0:
        left+=1
    elif mid>0:
        right-=1
    else:
        break
print(*last)