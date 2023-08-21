import sys

# https://ddiyeon.tistory.com/73
input = sys.stdin.readline

n = int(input().rstrip())
e = list(map(int, input().split()))
dp = [[0] * (n) for _ in range(n)]

for i in range(n):
    for j in range(i, i + 2):
        if j>=n:
            break
        if i == j:
            dp[i][j] = 1
        else:
            if e[i] == e[j]:
                dp[i][j] = 1

idx = 2
while 1:

    if idx >= n:
        break
    temp = idx
    for i in range(n):
        if temp>=n:
            break
        if e[i] == e[temp]:
            if dp[i+1][temp-1]==1:
                dp[i][temp]=1
        temp+=1
    idx += 1
m=int(input().rstrip())
for _ in range(m):
    a1,a2=map(int,input().split())
    print(dp[a1-1][a2-1])