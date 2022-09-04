import heapq
import sys
a=int(input())
heap = []
for i in range(0,a):
    b = int(sys.stdin.readline())
    if b==0:
        if len(heap)==0:
            print(0)
        else:
            print(heap[0])
            heapq.heappop(heap)
    else:
        heapq.heappush(heap, b)

