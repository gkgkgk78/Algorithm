import sys

from collections import deque
import heapq

input = sys.stdin.readline

n,m=map(int,input().split())

data=[]

for _ in range(n):
    e=list(map(int,input().split()))
    e.sort()
    data.append(e)

answer=sys.maxsize

index=[]#배열 번호, 해당 배열의 인덱스
q=[]
maxValue=-1
for i in range(n):
    now=data[i]
    maxValue=max(maxValue,now[0])
    heapq.heappush(q,(now[0],i,0))

while q:
    now=heapq.heappop(q)
    leftValue,leftArray,leftIndex=now
    #왼쪽 오른쪽 정해짐
    answer=min(answer,maxValue-leftValue)
    if leftIndex+1==m:
        break
    heapq.heappush(q,(data[leftArray][leftIndex+1],leftArray,leftIndex+1))
    maxValue=max(maxValue,data[leftArray][leftIndex+1])
print(answer)