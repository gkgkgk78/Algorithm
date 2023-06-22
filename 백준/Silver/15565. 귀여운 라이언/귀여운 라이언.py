import sys

input = sys.stdin.readline

n,k=map(int,input().split())
e=list(map(int,input().split()))
one=0
two=0
left=0
right=0
ans=sys.maxsize
if e[left]==1:
    one+=1
if one>=k:
    ans = min(ans, right - left + 1)

while right<n:
    #ans=min(ans,right-left+1)
    right+=1
    if right>=n:
        break

    if e[right]==1:
        one+=1

    if one>=k:
        ans = min(ans, right - left + 1)

        if one>=k:
            temp_check=0
            while left<right:
                if e[left]==1:
                    one-=1
                    temp_check+=1
                    if temp_check==2:
                        one+=1
                        break
                left+=1

if ans==sys.maxsize:
    print(-1)
else:
    print(ans)