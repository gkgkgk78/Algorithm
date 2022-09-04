import sys,copy
from itertools import combinations

from collections import deque

input=sys.stdin.readline

def check(num):

    t=str(num)
    for i in t:
        if i in s:
            return False
    return True



n = int(input())
m = int(input())
s = list(input().strip())
result = abs(n - 100)

for i in range(1000001):
    if check(i):
        result=min(result,len(str(i))+abs(n-i))
print(result)



