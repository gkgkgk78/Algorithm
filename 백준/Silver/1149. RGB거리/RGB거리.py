import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline

a=int(input().rstrip())

house=[[0,0,0] for _ in range(1001)]


for i in range(1,a+1):
    a1,a2,a3=map(int,input().split())
    house[i][0]=min(house[i-1][1],house[i-1][2])+a1
    house[i][1] = min(house[i - 1][0], house[i - 1][2]) + a2
    house[i][2] = min(house[i - 1][1], house[i - 1][0]) + a3

print(min(house[a][0],house[a][1],house[a][2]))

