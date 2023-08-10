import sys
import math
from collections import deque

n=int(input().rstrip())
m=int(input().rstrip())
if m>=n:
    print(0)
else:
    e=list(map(int,input().split()))
    e.sort()
    dp=[]
    for i in range(1,n):
        dp.append(e[i]-e[i-1])
    dp.sort(reverse=True)
    dp=deque(dp)

    #[1 3] [6 6 7 9] 로 2개로 나누게 되면은
    #구간이 몇개가 있든지 간에 1개는 제외 되야 한다
    #그때 최댓값을 제거 하자자
    for i in range(m-1):
        dp.popleft()

    print(sum(dp))