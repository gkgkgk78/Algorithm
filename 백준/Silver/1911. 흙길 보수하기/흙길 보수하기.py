import sys

input = sys.stdin.readline
import math

n, l = map(int, input().split())

e = []
for _ in range(n):
    t = list(map(int, input().split()))

    e.append(t)

e = sorted(e, key=lambda x: (x[0]))

start = 0

ans = 0

for a1, a2 in e:

  if start>=a1:
      a1=start+1
      if a1>=a2:
          continue

  div= math.ceil((a2-a1)/l)
  ans+=div
  start=max(start,a1+div*l-1)

print(ans)