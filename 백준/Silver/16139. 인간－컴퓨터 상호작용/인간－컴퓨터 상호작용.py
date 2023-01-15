import sys
input = sys.stdin.readline

s=input().rstrip()
arr=[[0]*(26) for _ in range(len(s))]

for i in range(len(s)):
    for j in range(i, len(s)):
        arr[j][ord(s[i]) - 97] += 1
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