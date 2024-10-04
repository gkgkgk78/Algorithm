import sys

n, s = map(int, input().split())
e = list(map(int, input().split()))
answer = sys.maxsize
left = 0
right = 0
now = e[left]
if now >= s:
    answer = min(answer, right - left + 1)

while right < n:
    if right + 1 == n:
        break
    right+=1
    now+=e[right]
    if now>=s:
        #이제 빼야함
        if now >= s:
            answer = min(answer, right - left + 1)
        while left<right:
            if now>=s:
                answer = min(answer, right - left + 1)
                now-=e[left]
                left+=1
            else:
                break
            if left==right:
                break
    if now >= s:
        answer = min(answer, right - left + 1)
if answer==sys.maxsize:
    print(0)
else:
    print(answer)