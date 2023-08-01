import sys

input = sys.stdin.readline

n = int(input().rstrip())


e = [0]
for i in range(n):
    t=int(input().rstrip())
    e.append(t)


dp = [0] * (n+1)
index = 1
dp[1] = e[1]
total = [-1] * (n+1)
total[1] = 1


def bi(i):
    left = -1
    right = index + 1
    while left + 1 < right:
        mid = (left + right) // 2
        if dp[mid] >= i:
            right = mid
        else:
            left = mid

    return right


for i in range(1, n+1):
    now = e[i]
    if dp[index] < e[i]:
        index += 1
        dp[index] = now
        total[i] = index
    else:
        ii = bi(now)
        dp[ii] = now
        total[i] = index



print(n - index)