import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline
import math

a=int(input().rstrip())

gg=list(map(int,input().split()))
arr2=sorted(list(set(gg)))


erf={arr2[i] : i for i in range(len(arr2))}

for i in gg:
    print(erf[i],end=" ")