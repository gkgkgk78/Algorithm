import sys, copy
from itertools import combinations

from collections import deque

input = sys.stdin.readline

n = int(input())

count = 1
stack = []
result = []

for i in range(n): # 데이터 갯수만큼 반복
    t=int(input())

    while count<=t:
        stack.append(count)
        count=count+1
        result.append("+")
    if stack[-1]==t:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)





print('\n'.join(result)) # 가능한 경우