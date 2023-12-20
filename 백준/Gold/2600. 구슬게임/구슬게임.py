import sys
input = sys.stdin.readline
e = list(map(int, input().split()))

dp = [[0] * (501) for _ in range(501)]


def game(x, y):
    if dp[x][y] > 0:
        return dp[x][y]

    for i in range(3):
        if e[i] <= x and game(x - e[i], y) == 0:
            dp[x][y] = 1
            return dp[x][y]
    for i in range(3):
        if e[i] <= y and game(x, y - e[i]) == 0:
            dp[x][y] = 1
            return dp[x][y]

    return dp[x][y]


for _ in range(5):
    a1, a2 = map(int, input().split())
    aa=game(a1,a2)
    if aa==1:
        print("A")
    else:
        print("B")