import sys

input = sys.stdin.readline

t = int(input().rstrip())

for i in range(t):
    n, m, k = map(int, input().split())
    e = list(map(int, input().split()))
    left = 0
    right = m - 1
    now = sum(e[:right + 1])
    ans = 0
    if now < k:
        ans += 1
    while left + 1 < n and n!=m:

        right += 1
        if right == n:
            right = 0
        now += e[right]
        now -= e[left]
        left += 1
        if now < k:
            ans += 1
    print(ans)