import sys
from collections import deque
import heapq

input = sys.stdin.readline

n, k, s = map(int, input().split())

left = []
right = []
for i in range(n):
    position, value = map(int, input().split())
    if position < s:
        heapq.heappush(left, (position - s, position, value))
    elif position > s:
        heapq.heappush(right,(s - position, position, value))

answer = 0


def go(arr):
    global answer
    while 1:
        if len(arr) == 0:
            break
        temp = 0
        count=0
        last = []
        while arr:
            v1, position, value = heapq.heappop(arr)
            temp = max(temp, abs(position - s))
            before=k-count
            count+=value
            if count>=k:
                count=k
            if (value - before) > 0:
                last.append((v1, position, value - before))
            if count >= k:
                break
        answer += temp*2
        for i in last:
            heapq.heappush(arr,i)

go(left)
go(right)
print(answer)