import sys, copy
import heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline
import math

a,b,c=map(int,input().split())
t=2**a

result=0
def st(x,y,n):
    global result

    if x==b and y==c :
        print(result)
        exit(0)
    if (x<=b<x+n and y<=c<y+n):
        st(x,y,n//2)
        st(x, y + n // 2, n // 2)
        st(x+n // 2, y, n // 2)
        st(x+n//2,y+n//2,n//2)
    else:
        result+=n*n
a=2**a
st(0,0,a)
