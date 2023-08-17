import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float("inf")

N = 1
Arr = []
DP = [[[INF] * 5 for _ in range(5)] for _ in range(100002)]
Cost = [
    [1, 2, 2, 2, 2],
    [2, 1, 3, 4, 3],
    [2, 3, 1, 3, 4],
    [2, 4, 3, 1, 3],
    [2, 3, 4, 3, 1]
]


def D(i, l, r):
    if i >= N:
        return 0
    if DP[i][l][r] != INF:
        return DP[i][l][r]
    rc = 0
    lc = 0
    if i + 1 < N:
        rc = Cost[r][Arr[i + 1]]
        lc = Cost[l][Arr[i + 1]]

    if Arr[i + 1] != r:
        DP[i][l][r] = min(DP[i][l][r], D(i + 1, Arr[i + 1], r) + lc)
    if Arr[i + 1] != l:
        DP[i][l][r] = min(DP[i][l][r], D(i + 1, l, Arr[i + 1]) + rc)
    return DP[i][l][r]


ee = list(map(int, input().split()))
Arr=[0]*(len(ee)+2)
for i in ee:
    if i == 0:
        break
    Arr[N] = i
    N += 1

print(D(0, 0, 0))