import sys, copy,heapq
import heapq,math
from itertools import permutations,combinations,product
from collections import deque
sys.setrecursionlimit(10**5)

# input = sys.stdin.readline
input=sys.stdin.readline

from bisect import bisect_right, bisect_left

n = int(input())
# 1이라면 시작과 동시에 종료
if n == 1:
    print(0)
    sys.exit()

arr = list(map(int, input().split()))
visited = [0] * n
q = deque([(0, arr[0])])  # 현재 위치, 점프 가능 거리

while q:
    pos, jump = q.popleft()
    for i in range(1, jump + 1):
        if pos + i >= n or visited[pos + i]:
            continue
        visited[pos + i] = visited[pos] + 1
        q.append((pos + i, arr[pos + i]))
print(visited[-1] if visited[-1] else -1)








