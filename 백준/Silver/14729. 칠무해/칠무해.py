import sys
import heapq

input = sys.stdin.readline
n=int(input().rstrip())
e=[]
for _ in range(n):
    heapq.heappush(e,float(input().rstrip()))


for i in range(7):
    print("{:.3f}".format(heapq.heappop(e)))