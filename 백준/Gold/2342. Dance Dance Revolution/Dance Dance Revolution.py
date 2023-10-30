import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dp = [[[sys.maxsize] * 5 for _ in range(5)] for _ in range(100001)]
cost = [
    [1, 2, 2, 2, 2],
    [2, 1, 3, 4, 3],
    [2, 3, 1, 3, 4],
    [2, 4, 3, 1, 3],
    [2, 3, 4, 3, 1]
]
e = list(map(int, input().split()))
e = e[:-1]


def dfs(cnt, left, right):

    if cnt == len(e):
        # 이때는 무언갈 하겠지
        return 0

    if dp[cnt][left][right] != sys.maxsize:
        return dp[cnt][left][right]

    l=cost[left][e[cnt]]
    r=cost[right][e[cnt]]

    if e[cnt]!=right:
        dp[cnt][left][right]=min(dp[cnt][left][right],dfs(cnt+1,e[cnt],right)+l)
    if e[cnt]!=left:
        dp[cnt][left][right]=min(dp[cnt][left][right],dfs(cnt+1,left,e[cnt])+r)

    return dp[cnt][left][right]

print(dfs(0,0,0))