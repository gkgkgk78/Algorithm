import sys
from collections import deque

input = sys.stdin.readline

ans = sys.maxsize
n, s = map(int, input().split())
e = list(map(int, input().split()))

left = 0
right = 1
sumz = e[0] + e[1]

while right < n:
    if sumz >= s:
        while sumz >= s:
            ans = min(ans, right - left + 1)
            sumz -= e[left]
            left += 1
            if left == right:
                break
    else:
        right += 1
        if right == n:
            break
        sumz += e[right]
for i in e:
    if i >= s:
        ans = 1
        break
if ans == sys.maxsize:
    print(0)
else:
    print(ans)
