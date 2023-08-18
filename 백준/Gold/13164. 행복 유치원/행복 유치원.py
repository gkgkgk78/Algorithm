import sys
import heapq
input = sys.stdin.readline
n,k=map(int,input().split())

e=list(map(int,input().split()))
e1=[]
for i in range(n-1):
    heapq.heappush(e1,-(e[i+1]-e[i]))

for i in range(k-1):
    heapq.heappop(e1)

print(-sum(e1))