import sys, copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
time = sorted(list(int(input()) for _ in range(N)))

start = 0
# time의 최소값 * 사람 수 => 최대 시간
end = min(time) * M
result = 0
count=0
while start <=end:
    mid=(start+end)//2
    qu=0
    for i in time:
        qu+=mid//i

    if qu>=M:
        end=mid-1
        if count==0:
            result=mid
            count+=1
        if result>mid:
            result=mid
    else:
        start=mid+1
print(result)