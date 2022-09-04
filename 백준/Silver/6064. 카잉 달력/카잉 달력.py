import sys, copy
import heapq
from itertools import combinations
from collections import deque
input = sys.stdin.readline
import math
a=int(input().rstrip())
from  math import gcd
for i in range(a):
    M, N, x, y = map(int, input().split())
    f = 1
    while (x <= M * N):
        if x % N == y % N:
            print(x)
            f = 0
            break
        x += M
    if f:
        print(-1)