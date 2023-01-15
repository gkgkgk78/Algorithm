import sys
input = sys.stdin.readline

s=input().rstrip()
arr=[[0]*(26) for _ in range(len(s))]

arr[0][ord(s[0]) - 97] = 1
for i in range(1, len(s)):
    arr[i][ord(s[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i - 1][j]
q = int(input())

for _ in range(q):
    alp, l, r = input().split()
    l=(int)(l)
    r=(int)(r)
    left=0
    right=0
    if l==0:
        left=0
    else:
        left=arr[l-1][ord(alp)-97]
    right=arr[r][ord(alp)-97]
    print(right-left)