import sys
#sys.stdin = open("input.txt")

A = list(input())
B = list(input())
A.insert(0,0)
B.insert(0,0)
A_len = len(A)
B_len = len(B)
#print(A)
#현재 문자열을 비교하는 과정: 이전의 과정이 LCS[i-1][j], LCS[i][j-1]
LCS = [[0] * (A_len) for _ in range(B_len)]

for i in range(1,len(B)):

    for j in range(1,len(A)):

        if A[j] == B[i]:
            LCS[i][j] = LCS[i-1][j-1]+1
        else :
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

# mx = -1
# for i in LCS:
#     if mx < max(i):
#         mx = max(i)
print(LCS[-1][-1])

#print(LCS)