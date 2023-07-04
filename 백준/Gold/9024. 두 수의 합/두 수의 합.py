import sys

input = sys.stdin.readline

n=int(input().rstrip())

for _ in range(n):
    a1,a2=map(int,input().split())
    e=list(map(int,input().split()))
    e.sort()

    left=0
    right=len(e)-1
    ans=sys.maxsize
    count=0
    while left<right:
        now=abs(e[left]+e[right]-a2)
        if now<ans:
            count=1
            ans=now
        elif now==ans:
            count+=1
        if e[left]+e[right]-a2>=0:
            right-=1
        else:
            left+=1
    print(count)