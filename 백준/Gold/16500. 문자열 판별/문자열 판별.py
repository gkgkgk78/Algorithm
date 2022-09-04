import sys,copy
from itertools import combinations

from collections import deque

input=sys.stdin.readline


def sol(idx):
    global result

    if idx == len(S):
        result = 1
        return
    if dp[idx]==1:
        return
    dp[idx] = 1
    j=0
    for i in range(len(A)):
        if len(S[idx:]) >= len(A[i]):
            for j in range(len(A[i])):
                if A[i][j] != S[idx + j]:
                    break
            else: #for문이 끝까지 다 실행 되었을때를 의미
                    sol(idx + len(A[i]))
    return


S = input().rstrip()
A = []
dp = [0] * 101
for _ in range(int(input())):
    A.append(input().rstrip())

result = 0
sol(0)
print(result)






























