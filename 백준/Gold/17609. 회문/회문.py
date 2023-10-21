import sys
from collections import deque
import heapq

input = sys.stdin.readline

n=int(input().rstrip())

def check(e):

    if len(e)%2==0:
        left=e[:len(e)//2]
        right=e[len(e)//2:]
        right=right[::-1]
        if left==right:
            return 1
    else:
        left=e[:len(e)//2]
        right=e[len(e)//2+1:]
        right=right[::-1]
        if left==right:
            return 1
    return 0

for _ in range(n):
    e=str(input().rstrip())
    a1=check(e)
    if a1==1:
        print(0)
        continue

    left=0
    right=len(e)-1
    tt=0
    while left<right:

        if e[left]==e[right]:
            left+=1
            right-=1
        else:
            #왼쪽 제거
            now=e[:left]+e[left+1:]
            #오른쪽 제거
            now1 = e[:right] + e[right + 1:]
            a1=check(now)
            a2=check(now1)
            if a1==1 or a2==1:
                print(1)
                tt=1
            break
    if tt==0:
        print(2)