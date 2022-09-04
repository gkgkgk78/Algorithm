import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline
import math

a,b,v=map(int,input().split())


ch=0
count=0
dev=(v-a)/(a-b)
print(math.ceil(dev)+1)


