import sys

input = sys.stdin.readline

s = list(map(str, input().rstrip()))
p = list(map(str, input().rstrip()))

total = dict()
for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        temp += s[j]
        if temp not in total:
            total[temp] = 1

left = 0
count = 0
ti = len(p)
while left < len(p):
    temp = ""
    j = left
    while j <= ti:
        temp += p[j]
        if temp not in total:
            break
        j += 1
        left = j
        if j == ti:
            break
    count += 1
    if left >= ti - 1:
        if left == ti - 1:
            count += 1
        break

print(count)