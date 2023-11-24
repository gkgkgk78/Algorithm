import sys

input = sys.stdin.readline

n, s = map(int, input().split())
e = list(map(int, input().split()))

left = 0
right = 0
now = e[0]

ans = sys.maxsize
if now >= s:
    ans = min(ans, right - left + 1)

while right < n:
    right += 1
    if right == n:
        break
    now+=e[right]
    if now>=s:
        while 1:
            if now >= s:
                ans = min(ans, right - left + 1)
            if left == right:
                break
            now-=e[left]
            left+=1
            if now<s:
                break
if ans==sys.maxsize:
    print(0)
else:
    print(ans)