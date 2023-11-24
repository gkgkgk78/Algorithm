import sys

input = sys.stdin.readline
n = int(input().rstrip())
e = list(map(int, input().split()))
answer=sys.maxsize
e.sort()

ans=[-1,-1,-1]
for i in range(1, n - 1):

    left = 0
    right = n - 1
    now = e[i]+e[left]+e[right]

    while 1:
        if now == 0:
            print(e[left], e[i], e[right])
            sys.exit(0)
        else:
            if abs(now) < answer:
                answer = abs(now)
                ans[0] = e[left]
                ans[1] = e[i]
                ans[2] = e[right]
        if now<0:
            now-=e[left]
            left+=1
            if left==i:
                break
            now+=e[left]
        elif now>0:
            now -= e[right]
            right -= 1
            if right == i:
                break
            now += e[right]

print(*ans)