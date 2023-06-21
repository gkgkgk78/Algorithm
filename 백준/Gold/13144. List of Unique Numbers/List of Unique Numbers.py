import sys

input = sys.stdin.readline

n = int(input().rstrip())
e = list(map(int, input().split()))

total = [0] * (n + 1)
count = 0
left = 0
right = 0
ans = 0

total[e[right]] += 1

while right < n and left <= right:

    ans += (right - left + 1)
    right += 1
    if right >= n:
        break
    total[e[right]] += 1

    while total[e[right]] >= 2:
        total[e[left]] -= 1
        left += 1

print(ans)