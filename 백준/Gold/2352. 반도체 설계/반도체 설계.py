import sys
input = sys.stdin.readline
n = int(input().rstrip())
dp = [0] * (n + 1)
now = [0] * (n + 1)
index = 1
e = [0] + list(map(int, input().split()))
dp[1] = e[1]
now[1] = 1


def find(h):
    left = 0
    right = index + 1

    while left + 1 < right:
        # upper bound를 찾아서 가장 큰얘들중 가장 작은걸 찾자
        mid = (left + right) // 2

        if dp[mid] >= h:
            right = mid
        else:
            left = mid

    return right


for i in range(2, n + 1):
    nn = e[i]
    if nn > dp[index]:
        index += 1
        dp[index] = nn
        now[i] = index
    else:
        fi = find(nn)
        dp[fi] = nn
        now[i] = fi

print(index)