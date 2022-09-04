import sys
numbers = int(input())
heap = []

for i in range(0,numbers):
    num = int(sys.stdin.readline())
    heap.append(num)

heap.sort()
for i in range(0,len(heap)):
    print(heap[i])