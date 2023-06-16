import sys

input = sys.stdin.readline

n, k, b = map(int, input().split())
total = [0] * (n + 1)
for _ in range(b):
    e = int(input().rstrip())
    total[e] = 1

left = 1
right = k
now = 0
ans = sys.maxsize
for l in range(1, right + 1):
    if total[l] == 1:
        now += 1
ans = min(ans, now)

while right + 1 <= n:
    right += 1
    if total[right] == 1:
        now += 1
    if total[left] == 1:
        now -= 1
    left += 1
    ans = min(ans, now)

print(ans)
