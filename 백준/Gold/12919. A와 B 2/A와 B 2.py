import sys


input = sys.stdin.readline

from collections import deque

total = dict()

first = str(input().rstrip())
second = str(input().rstrip())

# 문자열 뒤에서 a를 제거 한다
# 문자열 뒤에 B를 제거한후 문자열을 뒤집는다

def find():
    total[second] = 1
    q = deque()
    q.append(second)
    while q:
        now = q.popleft()
        if now == first:
            return 1
        if len(now) == 1:
            continue
        if now[-1] == "A":
            n1 = now[:-1]
            if n1 not in total:
                q.append(n1)
        n2 = ""
        for i in range(len(now) - 1, -1, -1):
            n2 += now[i]
        if n2[-1] == "B":
            temp = n2[:-1]
            if temp not in total:
                q.append(temp)
    return 0

print(find())