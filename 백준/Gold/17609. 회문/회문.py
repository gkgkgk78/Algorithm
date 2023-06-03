import sys

input = sys.stdin.readline

n=int(input().rstrip())

def check(e,left,right):

    while left<right:
        if e[left]==e[right]:
            left+=1
            right-=1
        else:
            return 0
    return 1


for _ in range(n):
    e=list(map(str,input().rstrip()))
    left=0
    right=len(e)-1

    count=0
    while left<right:
        if e[left]==e[right]:
            left += 1
            right -= 1
        else:
            a1=check(e,left+1,right)
            a2=check(e,left,right-1)
            if a1 or a2:
                count=1
                break
            else:
                count=2
                break

    print(count)