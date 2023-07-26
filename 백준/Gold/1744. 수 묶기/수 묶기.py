import sys
from collections import deque

input = sys.stdin.readline

e = []
ans = 0
n = int(input().rstrip())
plus = []
minus = []
zero = []
for _ in range(n):
    a1 = int(input().rstrip())
    if a1 == 0:
        zero.append(a1)
    elif a1 > 0:
        plus.append(a1)
    else:
        minus.append(a1)
plus.sort(reverse=True)
minus.sort()

# 우선 양수 부터 처리를 하자

plus = deque(plus)
minus = deque(minus)
zero = deque(zero)
while plus:
    ne = 0
    if len(plus) >= 2:
        a1 = plus.popleft()
        a2 = plus.popleft()
        if a1+a2>a1*a2:
            ne=a1+a2
        else:
            ne = a1 * a2
    else:
        ne = plus.popleft()
    ans += ne

while minus:
    ne = 0
    if len(minus) >= 2:
        a1 = minus.popleft()
        a2 = minus.popleft()
        ne = a1 * a2
    else:
        if len(zero) > 0:
            minus.popleft()
            zero.popleft()
            ne = 0
        else:
            ne = minus.popleft()
    ans += ne

print(ans)