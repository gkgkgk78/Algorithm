import sys
from collections import deque
from itertools import combinations
import math
input = sys.stdin.readline

def total_weight(value):

    now=0
    if value<=100:
        now+=2*(value)
        return now
    now=2*100
    if value<=10000:
        now += 3 * (value-100)
        return now
    now+=3*9900
    if value<=1000000:
        now += 5 * (value-10000)
        return now
    now+=5*990000

    now += 7 * (value - 1000000)
    return now


#우선 총 사용량 구한후에
def watt(value):
    if value<=200:
        return value//2
    if value<=29900:
        return (value-200)//3+100
    if value<=4979900:
        return (value-29900)//5+10000
    return (value-4979900)//7+1000000

#이분 탐색으로 해서 이웃과 전기 요금 차이 되는것을 구하도록 하자

while 1:
    a1,a2=map(int,input().split())
    if a1==0 and a2==0:
        break
    total=watt(a1)
    #이제 전체 와트를 구하게 되었다

    left=-1
    right=total
    tt=sys.maxsize
    while left+1<right:
        mid=(left+right)//2
        l=total_weight(mid)
        r=total_weight(total-mid)
        if abs(l-r)<a2:
            left=mid
        elif abs(l-r)>a2:
            right=mid
        else:
            tt=min(mid,total-mid)
            break
    print(total_weight(tt))