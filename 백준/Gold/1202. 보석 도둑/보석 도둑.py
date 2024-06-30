import sys
from collections import deque
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
jew = []
bag = []
for _ in range(n):
    weight, value = map(int, input().split())
    heapq.heappush(jew, [weight, value])
for _ in range(k):
    bag.append(int(input().rstrip()))

bag.sort()
answer = 0
temp = []
for now in bag:
    while jew:
        first = heapq.heappop(jew)
        a = first[0]
        if first[0] <= now:
            heapq.heappush(temp, -first[1])
        else:
            heapq.heappush(jew, [first[0], first[1]])
            break
    if temp:
        answer += heapq.heappop(temp)
print(-answer)