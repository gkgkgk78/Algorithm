import sys, copy,heapq
a=int(input().rstrip())


heap=[]
for i in range(a):
    g=int(input().rstrip())
    heap.append(g)
heapq.heapify(heap)
result=0
while len(heap)>1:
    a=heapq.heappop(heap)+heapq.heappop(heap)
    result+=a
    heapq.heappush(heap,a)
print(result)