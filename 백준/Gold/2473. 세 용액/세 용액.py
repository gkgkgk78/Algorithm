import sys, copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline


n=int(input().rstrip())

g=list(map(int,input().split()))

g.sort()

left=0
right=n-1
result=-50000000000000
ans=[]
if n == 3:
    print(*sorted(g))
    sys.exit()

for i in range(0,n-2):
    mid=i+1
    right=n-1
    left=i
    while mid<right:
        tmp=g[right]+g[mid]+g[left]
        if abs(tmp) <abs(result):
                ans=[]
                ans.append(g[left])
                ans.append(g[mid])
                ans.append(g[right])
                result=g[right]+g[mid]+g[left]
                if result==0:
                    print(*ans)
                    exit(0)

        if g[right]+g[mid]+g[left]<0:
                mid=mid+1
        elif g[right]+g[mid]+g[left]>0:
                right-=1
        else:
            print(*ans)
            exit(0)


print(*ans)







