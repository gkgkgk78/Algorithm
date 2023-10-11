import sys
import math
from collections import deque
import heapq

input = sys.stdin.readline

n, x = map(int, input().split())
e = list(map(int, input().split()))


def check(now):
    q = []
    index = 0
    ma = 0
    for i in range(now):
        heapq.heappush(q, e[i])
        index += 1
    while q:
        a2 = heapq.heappop(q)
        ma = max(ma, a2)
        if index >= len(e):
            continue
        nex = a2 + e[index]
        index += 1
        heapq.heappush(q, nex)
    return ma


left = 0
right = n + 1

ans = sys.maxsize
while left + 1 < right:
    mid = (left + right) // 2
    aa = check(mid)

    if aa <= x:
        right = mid
        ans = min(ans, mid)
    else:
        left = mid

print(ans)