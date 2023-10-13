import sys
import math
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input().rstrip())


def check(now):
    for i in range(2, (int)(math.sqrt(now)) + 1):
        if now % i == 0:
            return -1
    return 1


def dfs(now):
    if len(now) == n:
        aa = check((int)(now))
        if aa == 1:
            print(now)
        return
    for i in range(0, 10):
        a = now + (str(i))
        aa = check((int)(a))
        if aa == 1:
            dfs(a)

dfs("2")
dfs("3")
dfs("5")
dfs("7")