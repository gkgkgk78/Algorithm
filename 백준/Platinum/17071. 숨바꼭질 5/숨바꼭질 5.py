import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
time = 1
odd = [0] * (500001)
even = [0] * (500001)
even[n] = 1

if n == k:
    print(0)

else:
    q = deque()
    q.append(n)
    next = 1
    tt = [-1, 1]
    while 1:

        temp = deque()
        fin = []
        if time % 2 == 0:
            fin = even
        else:
            fin = odd
        while q:
            a1 = q.popleft()

            for i in range(3):
                zx = 0
                if i <= 1:
                    zx = a1 + tt[i]
                else:
                    zx = a1 * 2
                if zx > 500000 or zx < 0:
                    continue
                if fin[zx] == 0:
                    temp.append(zx)
                    fin[zx] = 1

        k += next
        if k > 500000:
            print(-1)
            sys.exit()
        if fin[k] == 1:
            print(time)
            sys.exit()
        next += 1
        time += 1
        q = temp