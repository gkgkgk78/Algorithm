import sys
import math
input = sys.stdin.readline

m,n=map(int,input().split())

def check(m):

    for i in range(2,int(math.sqrt(m))+1):
        if m%i==0:
            return 0
    return 1



for l in range(m,n+1):
    if l==1:
        continue
    now=check(l)
    if now==1:
        print(l)