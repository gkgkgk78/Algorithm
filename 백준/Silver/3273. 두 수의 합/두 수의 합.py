import sys

input = sys.stdin.readline

n=int(input().rstrip())
e=list(map(int,input().split()))
x=int(input().rstrip())
e.sort()
left=0
right=n-1
count=0
while left<right:

    now=e[left]+e[right]

    if now>=x:
        if now==x:
            count+=1
        right-=1
    else:
        left+=1

print(count)