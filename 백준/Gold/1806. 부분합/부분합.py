import sys

input = sys.stdin.readline

n, s = map(int, input().split())
e = list(map(int, input().split()))

left = 0
right = 0

now = e[0]

total = sys.maxsize
if now >= s:
    total = min(total, right - left + 1)


while left <= right:

    if now < s:
        right += 1
        if right>=n:
            break
        now += e[right]
    else:
        now -= e[left]
        left += 1

    if now >= s:
        total = min(total, right - left+1)

if total == sys.maxsize:
    print(0)
else:
    print(total)