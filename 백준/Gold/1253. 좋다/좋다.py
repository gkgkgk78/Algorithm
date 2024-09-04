import sys
input = sys.stdin.readline

n=int(input().rstrip())
e=list(map(int,input().split()))
answer=0

e.sort()
for i in range(n):
    left=0
    right=n-1
    now=e[i]
    while left<right:
        temp=e[left]+e[right]
        if temp==now:
            if left==i:
                left+=1
            elif right==i:
                right-=1
            else:
                answer+=1
                break
        elif temp>now:
            right-=1
        else:
            left+=1

print(answer)