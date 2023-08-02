import sys

input = sys.stdin.readline

n, k = map(int, input().split())
e = list(map(int, input().split()))
odd=0

left = 0
right = 0
ans=0
if e[0] % 2 == 1:
    odd += 1
ans = max(ans, right - left + 1 - odd)
while right+1 < n:
    right += 1

    if e[right] % 2 == 1:
        odd += 1
    if odd > k:
        while 1:
            if odd == k:
                break

            if e[left] % 2 == 1:
                odd -= 1
            left += 1
    ans=max(ans,right-left+1-odd)


print(ans)